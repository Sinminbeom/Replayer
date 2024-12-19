from abc import abstractmethod

from MultiProcess.cMultiProcesser import cMultiProcesser


from App.Common.cStepProcess import abStepProcess
from App.Common.eventBus import cInnerQueueBus
from App.Protocols.Protocol import cProtocolRapper


class cQueueControlProcess(abStepProcess):

    def __init__(self ,_app_name, _process_nm ,_cateRegKey=None , _queue_ex_name=None ):
        abStepProcess.__init__(self,_app_name,_process_nm , _queue_ex_name)
        self.innerQueueBus=None
        self.handler=None
        self.group_receive_handler = None
        self.protocol_pair=None

        self.cateRegKey=_cateRegKey

        self.processCate=None


        self.inrMatcher=None


    def BUILDER_InrMatcherEnable(self):

        from App.Protocols.InrProtocolMatcher.InrProtocolMatcher import cInrProtocolMatcher
        self.inrMatcher = cInrProtocolMatcher()

        return self
    def InrMatcher_Append(self , _protocol_message , _pair_packet_size = 0 ):

        if self.inrMatcher == None:
            return

        protocol_message , protocol_dto = self.inrMatcher.appendBroad(_protocol_message,_pair_packet_size)

        if protocol_message == None:
            return

        self.__InrMatcher_OnGroupInrMessageHandler( protocol_dto )

    def __InrMatcher_OnGroupInrMessageHandler(self , _protocol_dto ):

        ## if message_direction == E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        if _protocol_dto.GetMessageDirection() != E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
            return

        pairState = self.inrMatcher.GetBroadPairState( _protocol_dto.GetProtocolGroupID() )

        from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer


        # print(f""" ================ pair state : {pairState} """)

        if pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR:



            callback = self._getGroupHandlerCallBack( _protocol_dto.GetProtocolID() )
            callback(  self , pairState , self.inrMatcher.GetResponseDTOLists(  _protocol_dto.GetProtocolGroupID() ) )


            pass
        elif pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE:
            callback = self._getGroupHandlerCallBack(_protocol_dto.GetProtocolID())
            callback(  self , pairState , self.inrMatcher.GetResponseDTOLists(  _protocol_dto.GetProtocolGroupID() ) )
            pass

    def OnHandler(self,_protocol_message_string):

        protocol_rapper , protocol_message = cProtocolRapper.DecodeProtocolRapperWithMessageProtocol(_protocol_message_string)
        callback=self._getHandlerCallBack(protocol_rapper.protocol_id)
        return callback(self,protocol_rapper,protocol_message)


    @abstractmethod
    def OnInit(self):

        if self.cateRegKey != None:
            from App.Category.cCateGory import cProcessCate
            cProcessCate.instance().GetCateCallback(self.cateRegKey)()
            self.processCate = cProcessCate.instance()

        from App.Protocols.ProtocolPair.cProtocolPair import cProtocolPair
        self.protocol_pair=cProtocolPair()

        self.innerQueueBus=cInnerQueueBus(self)
        self.innerQueueBus.Start()

    def GetProcessCate(self):
        return self.processCate
    #
    # def GetProcessCateNameLits(self):
    #
    #     if self.processCate == None:
    #         return None
    #
    #
    #     self.processCate.GetProcessNameList(  )
    #
    #
    #     return self.processCate

    @abstractmethod
    def OnProcOnce(self):
        pass

    def GetProtocolPair(self):
        return self.protocol_pair

    def OnRegisterHandler(self,_handler ):
        self.handler=_handler

    def OnRegisterGroupReceiveHandler(self,_group_receive_handler ):
        self.group_receive_handler=_group_receive_handler

    def _IsContainHandler(self , _protocol_id):
        if _protocol_id in self.handler:
            return True

        return False

    def _IsContainGrouprReceiveHandler(self , _protocol_id):
        if _protocol_id in self.group_receive_handler:
            return True

        return False

    def IsIgnoreProtocol(self,_e_communication_type, _protocol_message_string):

        splitsProtocolMessage = cProtocolRapper.GetSplitProtocolMessage(_protocol_message_string)

        communication_symbol = cProtocolRapper.GetCommunicationTypeWithSplitsProtocolMessage(splitsProtocolMessage)

        from App.cDefine import E_COMMUNICATION_TYPE
        communication_type = E_COMMUNICATION_TYPE.getSymbolToE_Type( communication_symbol )

        if communication_type != _e_communication_type:
            print(f" IsIgnoreProtocol > communication_type  > logic {_e_communication_type} | protocol {communication_type} ) Is Not Match ")
            return True

        protocol_id = cProtocolRapper.GetProtocolIDWithSplitsProtocolMessage(splitsProtocolMessage)

        try:
            if self._IsContainHandler(protocol_id) == False:
                print(f" IsIgnoreProtocol > protocol_id:( {protocol_id} ) Is Not Mine ")
                return True
        except Exception as e:
            o=10
            pass


        receiver = cProtocolRapper.GetProtocolReceiverWithSplitsProtocolMessage(splitsProtocolMessage)
        from App.Protocols.cProtocolOwner import cProtocolName
        protocol_name_object = cProtocolName()
        protocol_name_object.SetNameByProtocolName(receiver)

        if not protocol_name_object.IsOwner(self.GetAppName(), self.GetName()):
            # print(f" IsIgnoreProtocol > myNM  {protocol_name_object.GetAppName()} , pnm {protocol_name_object.GetProcessName()} "
            #       f" [RECV]  appName: {self.GetAppName()} ProcessName:{self.GetName()} Is Not Mine ")
            return True

        return False

    def _getHandlerCallBack(self,_protocol_id):
        try:
            return self.handler[_protocol_id][self.GetAppName()]
        except Exception as e:
            raise Exception( f"ControlProcess Handler Not Found Error!! protocol_id [{_protocol_id}] ownerNm : [{self.GetAppName()}]" )
        pass

    def _getGroupHandlerCallBack(self,_protocol_id):
        try:

            from App.Protocols.cProtocolMeta import cProtocolMeta
            return cProtocolMeta.GetInrGroupReceiveHandler( _protocol_id , self.GetAppName() )

            # return self.handler[_protocol_id][self.GetAppName()]
        except Exception as e:
            raise Exception( f"ControlProcess Group Handler Not Found Error!! protocol_id [{_protocol_id}] ownerNm : [{self.GetAppName()}]" )
        pass
    #
    # @abstractmethod
    # def OnProcEveryFrame(self):
    #     super().OnProcEveryFrame()
    #     pass

    @abstractmethod
    def BridgeMessage(self,_message):
        print( "== cQueueControlProcess : ",_message)
        pass

    ##TODO 101
    def SendMessageInnerQueue(self,_process_name,_message):
        self.innerQueueBus.sendMessqageInnerQueue(  _process_name,_message)

    def SendMessageInnerQueue2(self,_process_name,_message):
        self.innerQueueBus.sendMessqageInnerQueue2(  _process_name,_message)

    ## Append sendMessage

    def SendMessqageReqInnerQueue(self,_protocol_id ,  _receiver_process_name,  *_message_args):
        self.innerQueueBus.sendMessqageReqInnerQueue(_protocol_id, _receiver_process_name,  *_message_args)
        pass

    from App.Protocols.cResponseCode import cResponseCode
    def SendMessqageRepInnerQueue(self,_protocol_id  ,_receiver_process_name,   *_message_args , _response_code=cResponseCode.FactoryOK()):
        self.innerQueueBus.sendMessqageRepInnerQueue(_protocol_id  ,_receiver_process_name,   *_message_args , _response_code=_response_code)


    ##cMessageReceiverContainer
    from App.Common.cMessageReceiverContainer import cMessageReceiverContainer
    def BroadCastMessqageInnerQueue(self,_protocol_id ,  _message_receiver_container : cMessageReceiverContainer ):
        self.innerQueueBus.broadCastMessqageInnerQueue(_protocol_id, _message_receiver_container)





class simcQueueControlProcess ( cQueueControlProcess):

    def __init__(self , _process_nm , ):
        cQueueControlProcess.__init__(self,_process_nm)
        pass

    @abstractmethod
    def OnInit(self):
        cQueueControlProcess.OnInit(self)
        pass

    @abstractmethod
    def OnProcEveryFrame(self):

        pass
def main():

    mp = cMultiProcesser(3)
    chnm = "news"


    p=simcQueueControlProcess("p1" )
    mp.Append( p )
    mp.IsRunning()
    mp.RunAsync()


    loopCount=0

    while True:
        # loopCount=loopCount+1
        #
        # if loopCount == 90:
        #     mp.Stop()

        pass


if __name__ == '__main__':
    main()





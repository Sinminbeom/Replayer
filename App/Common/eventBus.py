from abc import abstractmethod
import time
from ThreadUtils.abThreading import abThreading
from ThreadUtils.cThreadController import cThreadController

from App.Common.cTaskThread import cTaskThread


class cListenThread(abThreading):
    def __init__(self, _parent_process):
        abThreading.__init__(self)
        self.parent_process = _parent_process

    @abstractmethod
    def Action(self):
        pass


class cInnerQueueListenThread(cListenThread):

    def __init__(self, _parent_process):
        cListenThread.__init__(self, _parent_process)
        pass

    @abstractmethod
    def Action(self):

        from Log.cLogger import cLogger
        from Log.cLogger import E_LOG
        # cLogger.instance().Print(E_LOG.DEBUG,f" =================== 11111111111111111 cInnerQueueListenThread")
        # cLogger.instance().Print(E_LOG.DEBUG,f"<<<<<<<<<<<<<<<<<<<<<<<<<<  000000000000000 ")
        message_list = self.parent_process._shardQueuePopWithLockSelf()
        # cLogger.instance().Print(E_LOG.DEBUG,f"<<<<<<<<<<<<<<<<<<<<<<<<<<  1111111111111 ")
        time.sleep(0.005)
        # cLogger.instance().Print(E_LOG.DEBUG,f" =================== 222222222222222222 cInnerQueueListenThread")
        for message in message_list:
            from App.cDefine import E_COMMUNICATION_TYPE
            if self.parent_process.IsIgnoreProtocol(E_COMMUNICATION_TYPE.PROCESS, message) == True:
                # print("error ::cInnerQueueListenThread :: Action COMMUNICATION_TYPE Miss Match!! ")
                return

            cLogger.instance().Print(E_LOG.DEBUG, f" <<<<<<<<<<<<<<<<<<<<< [RECV] cInnerQueueListenThread {message} ")

            # print(f" [RECV] cInnerQueueListenThread {message}")

            ##TODO kk
            ## 여기서도 inr 을 부모 에게 위임 한다.

            ##TODO 101
            ## 이부분에서
            ## self.parent_process.OnHandler(message)  -> 부모에게 물어 여기를 통과 시킬지 말지 결정 한다.

            cLogger.instance().Print(E_LOG.DEBUG,
                                     f" <<<<<<<<<<<<<<<<<<<<< [RECV] InrMatcher_Append cInnerQueueListenThread {message} ")

            # self.parent_process.InrMatcher_Append(message)

            self.parent_process.OnHandler(message)
            self.parent_process.BridgeMessage(message)

            # from App.Protocols.Protocol import cProtocolRapper
            # protocol_rapper, protocol_message = cProtocolRapper.DecodeProtocolRapperWithMessageProtocol(
            #     message)

            self.parent_process.InrMatcher_Append(message)


class cImdgListenThread(cListenThread):

    def __init__(self, _pubsub, _parent_process):
        cListenThread.__init__(self, _parent_process)
        self.pubsub = _pubsub

    @abstractmethod
    def Action(self):
        try:
            for message in self.pubsub.listen():
                if message['type'] == 'message':
                    messageData = message["data"].decode("utf-8")

                    from App.cDefine import E_COMMUNICATION_TYPE
                    if self.parent_process.IsIgnoreProtocol(E_COMMUNICATION_TYPE.IMDG, messageData) == True:
                        # print("error ::cImdgListenThread :: Action COMMUNICATION_TYPE Miss Match!! ")
                        # print(f" err ::cImdgListenThread {messageData} ")
                        return

                    print(f" RECV BusBridgeMessage : {messageData}")
                    self.parent_process.OnHandler(messageData)
                    self.parent_process.BusBridgeMessage(messageData)

                    # print(f'Received message: { messageData}')
        except Exception as e:
            print(f" P:[{self.parent_process.GetName()}] Event Bus Error : ", str(e))
            # self.Stop()
            return
            # raise e


class cEventBus:

    def __init__(self, _parent_process):
        self.parent_process = _parent_process
        self.listenThread = None

    def Start(self):
        self.listenThread.Start()

    @abstractmethod
    def sendMessqageInnerQueue(self, _name, _message):
        print(f"message [{_name}] Send  : {_message}")
        pass

    @abstractmethod
    def sendMessqageInnerQueue2(self, _name, _message):
        print(f"message [{_name}] Send  : {_message}")
        pass

    @abstractmethod
    def sendMessqageReqInnerQueue(self, _protocol_id, _receiver_process_name, *_message_args):
        print(f"message [{_protocol_id}] Send  : {_receiver_process_name}")
        pass

    from App.Protocols.cResponseCode import cResponseCode
    @abstractmethod
    def sendMessqageRepInnerQueue(self, _protocol_id, _receiver_process_name, *_message_args,
                                  _response_code=cResponseCode.FactoryOK()):
        print(f"message [{_protocol_id}] Send  : {_receiver_process_name}")
        pass

    @abstractmethod
    def broadCastMessqageInnerQueue(self, _protocol_id, _message_receiver_container):
        pass

    #####################################################################################

    #######################################################################################

    @abstractmethod
    def sendMessqageImdgQueue(self, _message):
        print(f"message Send  : {_message}")
        pass


class cInnerQueueBus(cEventBus):
    def __init__(self, _bus_process):
        cEventBus.__init__(self, _bus_process)
        self.listenThread = cInnerQueueListenThread(_bus_process)

    ##TODO 101

    @abstractmethod
    def sendMessqageInnerQueue(self, _name, _message):
        ##TODO 101
        # self.parent_process.GetProtocolPair().Pair(_message)
        self.parent_process._shardQueuePutWithLock(_name, _message)

    ## lambda _sender, _receiver,   _vehicleId, _sensorIdList, _startTime, _endTime: pdPlayAbleListReq(
    ## sendMessqageReqInnerQueue ( _receiver_processname , PD_PLAYABLE_LIST_REQ , _vehicleId, _sensorIdList, _startTime, _endTime )

    @abstractmethod
    def sendMessqageReqInnerQueue(self, _protocol_id, _receiver_process_name, *_message_args):
        process_nm = self.parent_process.GetName()
        app_nm = self.parent_process.GetAppName()

        from App.Protocols.cProtocolMeta import cProtocolMeta
        sender = cProtocolMeta.GetProtocolOwnerName(app_nm, process_nm)
        receiver = cProtocolMeta.GetProtocolOwnerName(app_nm, _receiver_process_name)

        message = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id)(
            sender,
            receiver,
            *_message_args
        )
        protocol_packet_message = cProtocolMeta.GetProtocolPacketMessage(message)

        self.parent_process._shardQueuePutWithLock(_receiver_process_name, protocol_packet_message)

    def __sendMessqageReqInnerQueue(self, _protocol_id, _receiver_process_name, _pair_packet_size, *_message_args):
        process_nm = self.parent_process.GetName()
        app_nm = self.parent_process.GetAppName()

        from App.Protocols.cProtocolMeta import cProtocolMeta
        sender = cProtocolMeta.GetProtocolOwnerName(app_nm, process_nm)
        receiver = cProtocolMeta.GetProtocolOwnerName(app_nm, _receiver_process_name)

        message = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id)(
            sender,
            receiver,
            *_message_args
        )
        protocol_packet_message = cProtocolMeta.GetProtocolPacketMessage(message)

        ## TODO kk
        ## 여기서 부모프로세스에서 inr send를 위임한다...
        self.parent_process.InrMatcher_Append(protocol_packet_message, _pair_packet_size)
        self.parent_process._shardQueuePutWithLock(_receiver_process_name, protocol_packet_message)

    from App.Protocols.cResponseCode import cResponseCode
    @abstractmethod
    def sendMessqageRepInnerQueue(self, _protocol_id, _receiver_process_name, *_message_args,
                                  _response_code=cResponseCode.FactoryOK()):
        process_nm = self.parent_process.GetName()
        app_nm = self.parent_process.GetAppName()

        from App.Protocols.cProtocolMeta import cProtocolMeta
        sender = cProtocolMeta.GetProtocolOwnerName(app_nm, process_nm)
        receiver = cProtocolMeta.GetProtocolOwnerName(app_nm, _receiver_process_name)

        message = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id)(
            sender,
            receiver,
            *_message_args,
            _response_code
        )
        protocol_packet_message = cProtocolMeta.GetProtocolPacketMessage(message)
        self.parent_process._shardQueuePutWithLock(_receiver_process_name, protocol_packet_message)

    ## cMessageReceiverContainer
    @abstractmethod
    def broadCastMessqageInnerQueue(self, _protocol_id, _message_receiver_container):
        ii = len(_message_receiver_container.GetQueue())

        for mr in _message_receiver_container.GetQueue():
            self.__sendMessqageReqInnerQueue(_protocol_id,
                                             mr.GetReceiver(),
                                             len(_message_receiver_container.GetQueue()),
                                             *mr.GetMessage())

    @abstractmethod
    def sendMessqageInnerQueue2(self, _name, _message):
        ##TODO 101
        # self.parent_process.GetProtocolPair().Pair(_message)

        from Log.cLogger import cLogger
        from Log.cLogger import E_LOG

        cLogger.instance().Print(E_LOG.DEBUG,
                                 f"############################# 000000000000000 _name:{_name} MMMMMMMMMMMMMMMMMMM : {_message} ")
        self.parent_process._shardQueuePutWithLock(_name, _message)
        cLogger.instance().Print(E_LOG.DEBUG,
                                 f"#############################  11111111111 _name:{_name} MMMMMMMMMMMMMMMMMMM : {_message} ")


class cImdgBus(cEventBus):

    def __init__(self, _imdg, _channel_name, _bus_process):
        cEventBus.__init__(self, _bus_process)
        self.imdg = _imdg
        self.channel_name = _channel_name
        self.pubsub = _imdg.pubsub()
        self.pubsub.subscribe(_channel_name)
        self.listenThread = cImdgListenThread(self.pubsub, _bus_process)

    @abstractmethod
    def sendMessqageImdgQueue(self, _message):
        self.imdg.publish(self.channel_name, _message)

    ## _receiver_app_process_nm = cProtocolMeta.GetProtocolOwnerName(E_CATE.WEB_T, E_CATE.E_WEB_T.E_COMMON.WEB_T_MANAGER)
    @abstractmethod
    def sendMessqageReqImdgQueue(self, _protocol_id, _receiver_app_process_nm, *_message_args):
        app_nm = self.parent_process.GetAppName()

        from App.Protocols.cProtocolMeta import cProtocolMeta
        sender = cProtocolMeta.GetProtocolOwnerName(app_nm, None)

        packetObject = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id) \
                (
                sender, _receiver_app_process_nm,
                *_message_args
            )

        pkmessage = cProtocolMeta.GetProtocolPacketMessage(packetObject)

        self.imdg.publish(self.channel_name, pkmessage)

    from App.Protocols.cResponseCode import cResponseCode
    @abstractmethod
    def sendMessqageRepImdgQueue(self, _protocol_id, _receiver_app_process_nm, *_message_args,
                                 _response_code=cResponseCode.FactoryOK()):
        app_nm = self.parent_process.GetAppName()

        from App.Protocols.cProtocolMeta import cProtocolMeta
        sender = cProtocolMeta.GetProtocolOwnerName(app_nm, None)

        packetObject = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id) \
                (
                sender, _receiver_app_process_nm,
                *_message_args,
                _response_code
            )

        pkmessage = cProtocolMeta.GetProtocolPacketMessage(packetObject)

        self.imdg.publish(self.channel_name, pkmessage)

    #
    # @abstractmethod
    # def sendMessqageImdgQueue(self, _message):
    #     self.imdg.publish(self.channel_name, _message)


def main():
    pass


if __name__ == '__main__':
    main()


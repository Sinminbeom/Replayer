from App.Protocols.InrProtocolMatcher.IEventQueue import IEventQueue
from App.cDefine import IENUM


class cInrProtocolContainer(IEventQueue):
    class E_PROTOCOL_PAIR_STATE(IENUM):
        WAIT="WAIT"
        COMPLEATE="COMPLEATE"
        ERROR = "ERROR"
        ERROR_REMAIN = "ERROR_REMAIN"

    def __init__(self, _protocol_dto , _size):
        ## QD - protocol dto matcher
        self.inr_protocol_queue = {}
        self.protocol_pair_size = _size

        self.state=cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT

        self.Append(_protocol_dto)
        pass

    def _setProtocolPairSize(self , _protocol_pair_size ):
        self.protocol_pair_size = _protocol_pair_size

    def _getQueueSize(self):
        return len(self.inr_protocol_queue)

    ## TODO KK 여기에 여러개의 pair container 가 있다
    ## 종합하여 계산을 수행 한다...


    ## size 만큼 왔고 모두가 compleate 인가?
    ## 중간에 ERROR 이 있나?

    ## append 로직에서 처리를 한다.

    ## append 로직이 갈때 마다.
    ## err

    #
    # def __IsContainErrorState(self):
    #
    #     for pairContainer in self.inr_protocol_queue.values():
    #         if pairContainer.GetPairState() == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR :
    #             return True
    #
    #     return False


    ##Priority ->   ERROR -> ERROR_REMAIN -> WAIT -> COMPLEATE
    def __GetProtocolPairElementsPriorityState(self):


        bError = False
        bErrorRemain = False
        bWait = False
        bCompleate = False


        for pairContainer in self.inr_protocol_queue.values():
            if pairContainer.GetPairState() == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR :
                bError = True
            elif pairContainer.GetPairState() == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN:
                bErrorRemain = True
            elif pairContainer.GetPairState() == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT:
                bWait = True
            elif pairContainer.GetPairState() == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE:
                bCompleate = True

        if bError == True:
            return cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR
        if bErrorRemain == True:
            return cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN
        if bWait == True:
            return cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT
        if bCompleate == True:
            return cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE


    def __processingProtocolPair(self):

        elements_state = self.__GetProtocolPairElementsPriorityState()

        # if elements_state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR:
        #     self.state = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN
        #     return

        if self.state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT:
            self.__processingProtocolPair_Wait(elements_state)
        elif self.state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE:
            self.__processingProtocolPair_Compleate(elements_state)
        elif self.state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR:
            self.__processingProtocolPair_Error(elements_state)
        elif self.state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN:
            self.__processingProtocolPair_ErrorRemain(elements_state)


    ##TODO KK ERROR_REMAIN -> ERROR
    def __processingProtocolPair_Wait(self , _elements_state):

        if _elements_state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR:
            # self.state = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN
            self.state = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR
            return
        elif _elements_state == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE:
            if self.protocol_pair_size == self._getQueueSize() :
                self.state = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE

                return

    def __processingProtocolPair_Compleate(self, _elements_state):

        pass

    def __processingProtocolPair_Error(self, _elements_state):
        self.state = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN
        pass

    def __processingProtocolPair_ErrorRemain(self, _elements_state):

        pass


    def IsContainQD(self , _protocol_dto ):

        qdps = _protocol_dto.GetQPHash()

        qdpsKey = qdps.GetHashKey()

        if qdpsKey not in self.inr_protocol_queue:
            return False

        self.inr_protocol_queue[qdpsKey].IsContainQD( _protocol_dto.GetQD() )


        pass


    def Append(self , _protocol_dto ):
        v=_protocol_dto.GetQD()
        v1=_protocol_dto.GetPS()

        qdps=_protocol_dto.GetQPHash()

        qdpsKey=qdps.GetHashKey()

        from App.Protocols.InrProtocolMatcher.cProtocolPairContainer import cProtocolPairContainer

        if qdpsKey not in self.inr_protocol_queue:
            self.inr_protocol_queue[qdpsKey] = cProtocolPairContainer(_protocol_dto)
        else:
            self.inr_protocol_queue[qdpsKey].Append(_protocol_dto)

        # print(" QD : " , v , " PS : " , v1, "  qdpsKey :  " , qdpsKey)

        self.__processingProtocolPair()
        #
        # md=_protocol_dto.GetMessageDirection()
        # self.inr_protocol_queue[md]=_protocol_dto


    def GetResponseDTOLists(self):

        responseLists=[]

        for pair in self.inr_protocol_queue.values():
            responsePacket=pair.GetResponsePacketDTO()
            if responsePacket != None:
                responseLists.append( pair.GetResponsePacketDTO() )

        return responseLists

    def GetPairState(self):
        return self.state

        #
        # for pairContainer in self.inr_protocol_queue.values():
        #     print( pairContainer.GetPairState() )
        #
        #     # print(value)
        #
        # pass


    # def toString(self):

        # ret=""
        # for k , v in self.inr_protocol_queue.items():
        #     ret = ret + f""" k : {k} , v : {v.} """



        pass



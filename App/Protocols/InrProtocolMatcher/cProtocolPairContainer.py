from App.Common.cDto import IDTO
from App.cDefine import IENUM


class E_PROTOCOL_DIRECTION_SYMBOL(IENUM):
    QD = 0
    PS = 1
    MAX = 2


class cProtocolPairContainer(IDTO):



    def __init__(self , _protocol_dto):
        super().__init__()
        self.queue={}
        self.__init()
        self.Append(_protocol_dto)

    def __init(self):

        from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
        self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD]=None
        self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = None
        self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT


    ##############################################################################################
    # class cProtocolDTO(cProtocolPairDTO):
    #
    #     def __init__(self, _protocol_id, _communication_type,
    #                  _message_direcion,
    #                  _sender, _receiver,
    #                  _return_code_dto):
    #         super().__init__(_protocol_id, _communication_type, _message_direcion)
    #
    #         self.sender = _sender
    #         self.receiver = _receiver
    #
    #         self.return_code_dto = _return_code_dto
    ##############################################################################################

    def IsContainQD(self , _qd ):

        if self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] == None:
            return False

        if self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD].GetQD() == _qd:
            return True

        return False

    def __AppendWait(self , _protocol_dto , _hash):

        if _hash.sy == E_PROTOCOL_DIRECTION_SYMBOL.QD:
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] = _protocol_dto
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = None
            from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
            self.pairState =cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT
        else:
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = _protocol_dto
            retCode = _protocol_dto.GetReturnCode()
            from App.Protocols.cProtocolCodeMeta import cProtocolCodeMeta
            if retCode != cProtocolCodeMeta.E_CODE.OK:
                from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
                self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR

                return

        if self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] != None and self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] != None :
            from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
            self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE
            return

    def __AppendCompleate(self, _protocol_dto, _hash):
        if _hash.sy == E_PROTOCOL_DIRECTION_SYMBOL.QD:
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] = _protocol_dto
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = None
            from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
            self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT

    def __AppendError(self, _protocol_dto, _hash):
        if _hash.sy == E_PROTOCOL_DIRECTION_SYMBOL.QD:
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] = _protocol_dto
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = None
            from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
            self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT

    def __AppendErrorRemain(self, _protocol_dto, _hash):
        if _hash.sy == E_PROTOCOL_DIRECTION_SYMBOL.QD:
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.QD] = _protocol_dto
            self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] = None
            from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
            self.pairState = cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT


    def Append(self , _protocol_dto ):

        from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer

        hs = _protocol_dto.GetQPHash()

        if self.pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.WAIT:
            self.__AppendWait(_protocol_dto,hs)
        elif self.pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.COMPLEATE:
            self.__AppendCompleate(_protocol_dto,hs)
        elif self.pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR:
            self.__AppendError(_protocol_dto, hs)
        elif self.pairState == cInrProtocolContainer.E_PROTOCOL_PAIR_STATE.ERROR_REMAIN:
            self.__AppendErrorRemain(_protocol_dto, hs)

    def GetResponsePacketDTO(self):

        if self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS] == None:
            return None

        return self.queue[E_PROTOCOL_DIRECTION_SYMBOL.PS].GetPacket()

    def GetPairState(self):
        return self.pairState



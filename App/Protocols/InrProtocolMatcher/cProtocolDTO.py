from App.Protocols.ProtocolPair.cProtocolPairDTO import cProtocolPairDTO


class cProtocolDTO(cProtocolPairDTO):

    def __init__(self, _protocol_id, _communication_type,
                 _message_direcion ,
                 _sender , _receiver ,
                 _ppacket ,
                 _return_code_dto ):
        super().__init__(_protocol_id, _communication_type,  _message_direcion )

        self.sender = _sender
        self.receiver =_receiver

        self.return_code_dto = _return_code_dto


        self.ppacket=_ppacket


    def GetPacket(self):
        return self.ppacket
        pass
    def GetSender(self):
        return self.sender

    def GetReceiver(self):
        return self.receiver


    def GetReturnCode(self):
        if self.return_code_dto != None:
            return self.return_code_dto.GetCode()

        return None



    def GetQD(self):
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION

        if self.GetMessageDirection() == E_PROTOCOL_MESSAGE_DIRECTION.REQUEST:
            return self.receiver

        return None

    def GetPS(self):
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION

        if self.GetMessageDirection() == E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
            return self.sender

        return None


    # def __getQPKey(self , qd , ps ):
    #
    #     retu cQdPsHash(qd,ps)

    def GetQPHash(self):
        qd =""
        ps =""

        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        from App.Protocols.InrProtocolMatcher.cProtocolPairContainer import E_PROTOCOL_DIRECTION_SYMBOL
        if self.GetMessageDirection() == E_PROTOCOL_MESSAGE_DIRECTION.REQUEST:
            qd=self.receiver
            ps=self.sender
            sy=E_PROTOCOL_DIRECTION_SYMBOL.QD
        else:
            ps = self.receiver
            qd = self.sender
            sy = E_PROTOCOL_DIRECTION_SYMBOL.PS


        from App.Protocols.InrProtocolMatcher.cQdPsHash import cQdPsHash
        return cQdPsHash( qd , ps , sy  )

        # return self.__getQPKey(qd,ps)


    def GetGD_PS(self):
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        if self.GetMessageDirection() == E_PROTOCOL_MESSAGE_DIRECTION.REQUEST:
            return self.receiver

        return self.sender


def main():
    _protocol_id="aa_PD_-900"
    _protocol_id="pd_-200"
    _protocol_id="pd_-200"

    from App.Protocols.cProtocolMeta import cProtocolMeta


    _protocol_id=cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REP
    _protocol_id=cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REQ

    gid= cProtocolDTO.FactorProtocolGroupID(_protocol_id)
    print(f"gid:{gid}")



    pass

if __name__ == '__main__':
    main()
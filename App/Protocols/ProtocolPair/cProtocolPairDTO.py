from App.Common.cDto import IDTO


class cProtocolPairDTO(IDTO):

    def __init__(self,_protocol_id , _communication_type , _message_direcion):
        IDTO.__init__(self)

        self.protocol_id=_protocol_id
        self.communication_type=_communication_type
        self.message_direction=int(_message_direcion)

        self.protocol_group_id = cProtocolPairDTO.FactorProtocolGroupID( _protocol_id )

    def GetCommunicationType(self):
        return self.communication_type
    def GetProtocolID(self):
        return self.protocol_id

    def GetMessageDirection(self):
        return self.message_direction

    def GetProtocolGroupID(self):
        return self.protocol_group_id

    @staticmethod
    def FactorProtocolGroupID(_protocol_id ):
        s=_protocol_id.split("_")

        ln=len(s)

        calc_protocol_id = s[ln-1]

        iid = int(calc_protocol_id)
        gid= str(abs(int(iid / 100)))

        from LibUtils.StringBuilder import StringBuilder
        sb = StringBuilder()

        for i in range( ln-1 ):
            sb.Append(s[i]).Append("_")

        sb.Append(gid)


        return sb.ToString()

def main():
    from App.Protocols.cProtocolMeta import cProtocolMeta

    dto=cProtocolPairDTO( cProtocolMeta.E_PROTOCOL_ID.INR_STOP_REP , 1 , 1 )


    a=int(cProtocolMeta.E_PROTOCOL_ID.INR_STOP_REP)
    # cProtocolMeta.cProtocolMeta.INR_STOP_REP

    print( str( int(a / 100)) )

    pass

if __name__ == '__main__':
    main()
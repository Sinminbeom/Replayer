from JSon.Gson import Gson
from LibUtils.StringBuilder import StringBuilder
from TimeUtils.cTimeStringFit import cTimeStringFit, E_TIMEFORMAT

from App.cDefine import E_COMMUNICATION_TYPE, IENUM


class cProtocolRapper:
    DELIM_CHAR = "|:|"

    class E_PROTOCOL_MESSAGE_ELE(IENUM):
        COMMUNICATION_TYPE = 0
        MESSAGE_ID = 1
        PROTOCOL_ID = 2
        MESSAGE_DIRECTION = 3
        SENDER = 4
        RECEIVER = 5
        PROTOCOL_MESSAGE = 6

    DecodeHandler = {}
    SequenceID = {}

    ##E_COMMUNICATION_TYPE.IMDG
    def __init__(self, _message_id, _protocol_message):
        try:
            self.communication_type = _protocol_message.communication_type
        except Exception as e:
            self.communication_type = E_COMMUNICATION_TYPE.NORMAL

        self.protocol_id = _protocol_message.protocol_id
        self.message_direction = _protocol_message.message_direction
        self.sender = _protocol_message.sender
        self.receiver = _protocol_message.receiver
        self.protocol_message = _protocol_message
        self.message_id = _message_id

    def GetMessageDirection(self):
        return self.message_direction

    @staticmethod
    def ResetDecodeHandler():
        cProtocolRapper.DecodeHandler = {}

    @staticmethod
    def AppendDecodeHandler(_protocol_id, _lambda_func):
        cProtocolRapper.DecodeHandler[_protocol_id] = _lambda_func

        pass

    @staticmethod
    def GetDecodeHandlerAction(_protocol_id):
        return cProtocolRapper.DecodeHandler[_protocol_id]

    @staticmethod
    def RegisterTest():

        print(len(cProtocolRapper.DecodeHandler))

        pass

    def ToString(self):
        sb = StringBuilder()
        sb.Append("communication_type :").Append(E_COMMUNICATION_TYPE.getSymbol(self.communication_type)) \
            .Append("protocol_id : ").Append(self.protocol_id) \
            .Append("message_direction : ").Append(self.message_direction) \
            .Append("sender : ").Append(self.sender) \
            .Append("receiver : ").Append(self.receiver) \
            .Append("protocol_message : ").Append(self.protocol_message) \
            .Append("message_id : ").Append(self.message_id)
        return sb.ToString()


    ##TODO 101 여기에 추가한다. 프로트콜 정보를
    def getProtocolPacketMessage(self):
        sb = StringBuilder()
        sb.Append(E_COMMUNICATION_TYPE.getSymbol(self.communication_type)).Append(self.DELIM_CHAR) \
            .Append(self.message_id).Append(self.DELIM_CHAR) \
            .Append(self.protocol_id).Append(self.DELIM_CHAR) \
            .Append(self.message_direction).Append(self.DELIM_CHAR) \
            .Append(self.sender).Append(self.DELIM_CHAR) \
            .Append(self.receiver).Append(self.DELIM_CHAR) \
            .Append(Gson.toJson(self.protocol_message))
        return sb.ToString()

    @staticmethod
    def GetSequenceIDNow():
        field_key = cTimeStringFit().Get(E_TIMEFORMAT.YYYYMMDDHH24MI)

        if field_key in cProtocolRapper.SequenceID:
            cProtocolRapper.SequenceID[field_key] += 1
        else:
            cProtocolRapper.SequenceID[field_key] = 0

        seq = int(cProtocolRapper.SequenceID[field_key])
        return field_key + "_" + f"{seq:08}"

    @staticmethod
    def GetProtocolRapper(_protocol_message_object):
        message_id = cProtocolRapper.GetSequenceIDNow()
        # message_id = cRedisUtils.getSequenceIDNow(_redis, E_RUN_MODE.DEBUG)
        return cProtocolRapper(message_id, _protocol_message_object)

    @staticmethod
    def DecodeProtocolPairDTO(_protocol_message_string):
        s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)

        protocol_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]
        communication_type = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.COMMUNICATION_TYPE]
        message_direction = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.MESSAGE_DIRECTION]

        from App.Protocols.ProtocolPair.cProtocolPairDTO import cProtocolPairDTO
        dto = cProtocolPairDTO( protocol_id , communication_type ,message_direction )

        return dto

    @staticmethod
    def DecodeProtocolEventDTO(_protocol_message_string):
        s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)

        protocol_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]
        communication_type = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.COMMUNICATION_TYPE]
        message_direction = int(s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.MESSAGE_DIRECTION])

        sender = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.SENDER]
        receiver = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.RECEIVER]
        protocol_mes=s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_MESSAGE]

        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Protocols.cResponseCode import cResponseCode
        return_code_dto=None

        pPacket = cProtocolMeta.GetJsonDecoder(protocol_id)(protocol_mes)
        if message_direction == E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
            # pPacket = cProtocolMeta.GetJsonDecoder(protocol_id)(protocol_mes)
            return_code_dto=cResponseCode(pPacket.GetReturnCode(), pPacket.GetReturnCodeReason())

        from App.Protocols.InrProtocolMatcher.cProtocolDTO import cProtocolDTO
        dto = cProtocolDTO(protocol_id, communication_type, message_direction, sender, receiver , pPacket , return_code_dto)

        return dto

    @staticmethod
    def DecodeProtocolRapper(_protocol_message_string):
        s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)

        protocol_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]
        message_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.MESSAGE_ID]
        protocol_message_json_string = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_MESSAGE]

        protocol_message_object = cProtocolRapper.GetDecodeHandlerAction(protocol_id)(protocol_message_json_string)
        protocol_rapper = cProtocolRapper(message_id, protocol_message_object)

        return protocol_rapper

    @staticmethod
    def GetProtocolIDWithProtocolMessage(_protocol_message_string):

        s = cProtocolRapper.GetSplitProtocolMessage(_protocol_message_string)
        # s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)
        return s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]

    @staticmethod
    def GetCommunicationTypeWithSplitsProtocolMessage(_splits_protocol_message):
        return _splits_protocol_message[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.COMMUNICATION_TYPE]

    @staticmethod
    def GetProtocolIDWithSplitsProtocolMessage(_splits_protocol_message):

        # s=cProtocolRapper.GetProtocolSplitList(_protocol_message_string)
        # s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)
        return _splits_protocol_message[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]

    @staticmethod
    def GetProtocolReceiverWithSplitsProtocolMessage(_splits_protocol_message):

        # s=cProtocolRapper.GetProtocolSplitList(_protocol_message_string)
        # s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)
        return _splits_protocol_message[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.RECEIVER]

    @staticmethod
    def GetSplitProtocolMessage(_protocol_message_string):
        return _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)

    @staticmethod
    def DecodeProtocolRapperWithMessageProtocol(_protocol_message_string):
        s = _protocol_message_string.split(cProtocolRapper.DELIM_CHAR)

        protocol_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_ID]
        message_id = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.MESSAGE_ID]
        protocol_message_json_string = s[cProtocolRapper.E_PROTOCOL_MESSAGE_ELE.PROTOCOL_MESSAGE]

        protocol_message_object = cProtocolRapper.GetDecodeHandlerAction(protocol_id)(protocol_message_json_string)
        protocol_rapper = cProtocolRapper(message_id, protocol_message_object)

        return protocol_rapper, protocol_message_object


def main():
    # while True:
    #     print( cProtocolRapper.GetSequenceIDNow() )
    #     # time.sleep(0.02)

    # cProtocolRapper.RegisterDecodeHandler()

    from App.Protocols.cMessage import simImdgMessage
    protocolmessage = simImdgMessage("_sender", "_receiver", "play")

    mes = cProtocolRapper.GetProtocolRapper(protocolmessage).getProtocolPacketMessage()

    # protocol_mes= cProtocolRapper.GetProtocolRapper(protocolmessage)
    # mes=protocol_mes.getProtocolPacketMessage()

    print(mes)

    cc = cProtocolRapper.DecodeProtocolRapper(mes)

    o = 10
    o = 100

    pass


if __name__ == '__main__':
    main()

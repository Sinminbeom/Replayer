import json
from types import SimpleNamespace

from JSon.Gson import Gson

# from App.Protocols.cCodeDTO import cCodeDTO
# from App.Protocols.eProtocolId import E_PROTOCOL_ID
from App.cDefine import E_COMMUNICATION_TYPE, IENUM


class E_PROTOCOL_MESSAGE_DIRECTION(IENUM):
    REQUEST=0
    RESPONSE=1
    NOTI=2


class IMessage():


    def toJson(self):

        pass

    pass


class abProtocolMessageDirection(IMessage):
    def __init__(self,_message_direction):
        IMessage.__init__(self)

        self.message_direction=_message_direction

class abRequestMessage(abProtocolMessageDirection):
    def __init__(self):
        abProtocolMessageDirection.__init__(self,E_PROTOCOL_MESSAGE_DIRECTION.REQUEST)


class abReponseMessage(abProtocolMessageDirection):
    def __init__(self,_return_code_dto_factory):
        abProtocolMessageDirection.__init__(self,E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE)

        self.return_code=_return_code_dto_factory.GetCode()

        self.return_code_nm=_return_code_dto_factory.GetCodeNM()
        self.return_code_reason=_return_code_dto_factory.GetReason()


    def GetReturnCode(self):
        return self.return_code

    def GetReturnCodeNM(self):
        return self.return_code_nm

    def GetReturnCodeReason(self):
        return self.return_code_reason


class abNotiMessage(abProtocolMessageDirection):
    def __init__(self):
        abProtocolMessageDirection.__init__(self,E_PROTOCOL_MESSAGE_DIRECTION.NOTI)



class abProtocolMessage(IMessage):

    # def __init__(self,_e_communication_type,_mid,_sender,_receiver):
    def __init__(self,_e_communication_type,_protocol_id,_sender,_receiver):
        IMessage.__init__(self)
        self.communication_type=_e_communication_type
        self.protocol_id=_protocol_id
        self.sender=_sender
        self.receiver=_receiver

    def GetCommunication_type(self):
        return self.communication_type

    def GetProtocolId(self):
        return self.protocol_id

    def GetSender(self):
        return self.sender

    def GetReceiver(self):
        return self.receiver

    def SetCommunication_type(self, _communication_type):
        self.communication_type = _communication_type

    def SetProtocolId(self, _protocol_id):
        self.protocol_id = _protocol_id

    def SetSender(self, _sender):
        self.sender = _sender

    def SetReceiver(self, _receiver):
        self.receiver = _receiver

    def toJson(self):

        return Gson.toJson(self)

        # return json.dumps(self.__dict__)



class abImdgMessage(abProtocolMessage):

    def __init__(self,_protocol_id,_sender,_receiver):
        abProtocolMessage.__init__(self ,E_COMMUNICATION_TYPE.IMDG , _protocol_id,_sender,_receiver )

class abProcessMessage(abProtocolMessage):
    def __init__(self,_protocol_id,_sender,_receiver):
        abProtocolMessage.__init__(self ,E_COMMUNICATION_TYPE.PROCESS , _protocol_id,_sender,_receiver)

class simT2(abReponseMessage ):

    def __init__(self):
        abReponseMessage.__init__(self, "ret_mes")
        # abImdgMessage.__init__(self,E_PROTOCOL_ID.PLAY_TEST,"ss","re")


    @staticmethod
    def from_json(json_string):
        obj=Gson.fromJsonWithCls( simT2,json_str=json_string)
        return obj



class simT3(abReponseMessage ,abImdgMessage ):

    def __init__(self):
        from App.Protocols.cResponseCode import cResponseCode
        from App.Protocols.cProtocolCodeMeta import cProtocolCodeMeta
        abReponseMessage.__init__(self, cResponseCode.Factory(cProtocolCodeMeta.E_CODE.OK))
        abImdgMessage.__init__(self,"ID","ss","re")


    @staticmethod
    def from_json(json_string):
        obj=Gson.fromJsonWithCls( simT2,json_str=json_string)
        return obj

class simImdgMessage(abReponseMessage,abImdgMessage):
    def __init__(self,_sender,_receiver , _command):
        from App.Protocols.cResponseCode import cResponseCode
        from App.Protocols.cProtocolCodeMeta import cProtocolCodeMeta

        abReponseMessage.__init__(self, cResponseCode.Factory(cProtocolCodeMeta.E_CODE.OK))
        abImdgMessage.__init__(self, "DD" ,_sender,_receiver)
        self.command=_command

        pass

    @staticmethod
    def from_json(json_string):
        obj=Gson.fromJsonWithCls( simImdgMessage,json_str=json_string)
        return obj

def main2():
    # s=simT2("ASd")
    # s=simT2()
    #
    # print(s)

    s = simT3()


    # jsonMessage=s.toJson()

    jsonMessage =  Gson.toJson(s)

    jsonMessage = s.toJson()

    print(jsonMessage)

    ob=simT3.from_json(jsonMessage )

    o=100




    pass

def main():
    m=simImdgMessage("sender" , "receiver"  ,"play" )

    json_str=m.toJson()
    print(json_str)

    #
    #
    # o=simImdgMessage.from_json( json_str )
    #
    # print( o.command)
    #
    # a=10
    # a=100

    ss=simT3()

    j=ss.toJson()
    print(j)



if __name__ == '__main__':
    main2()

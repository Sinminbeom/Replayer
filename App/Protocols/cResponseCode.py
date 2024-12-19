from App.Common.cDto import IDTO


class cResponseCode(IDTO):

    def __init__(self,_code,_reason=None):
        IDTO.__init__(self)
        self.code=_code
        from App.Protocols.cProtocolCodeMeta import cProtocolCodeMeta
        self.code_nm=cProtocolCodeMeta.GetCodeNM(_code)
        self.reason=""
        if _reason != None:
            self.reason = _reason

    def SetReason(self,_reason):
        self.reason=_reason
        return self

    def GetCode(self):
        return self.code
    def GetCodeNM(self):
        return self.code_nm

    def GetReason(self):
        return self.reason
    @staticmethod
    def Factory(_code,_reason=None):
        return cResponseCode(_code, _reason)


    @staticmethod
    def FactoryOK():
        from App.Protocols.cProtocolCodeMeta import cProtocolCodeMeta
        return cResponseCode(cProtocolCodeMeta.E_CODE.OK, None)




    @staticmethod
    def FactoryWithResponseProtocolMessageObject( _response_protocol_message_object ):
        return cResponseCode(_response_protocol_message_object.GetReturnCode(), _response_protocol_message_object.GetReturnCodeReason())




from dataclasses import dataclass

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket


@dataclass
class pdResponsePacket(pdDataPacket):
    code: str
    code_nm: str
    reason: str

    def GetCode(self):
        return self.code
    def GetCodeNM(self):
        return self.code_nm

    def GetReason(self):
        return self.reason

    def SetCodeDto(self,_codeDto):
        self.code = _codeDto.GetCode()
        self.code_nm = _codeDto.GetCodeNM()
        self.reason = _codeDto.GetReason()

from dataclasses import dataclass, asdict

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket
from App.Protocols.Messages.dataClass.pdPacketResponse import pdResponsePacket

@dataclass
class pdCrawlingReq(pdDataPacket):
    uri: str
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdCrawlingReq(**dicts)



@dataclass
class pdCrawlingRep(pdResponsePacket):
    s_code: str
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdCrawlingRep(**dicts)


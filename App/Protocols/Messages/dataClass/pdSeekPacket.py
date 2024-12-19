import json
from dataclasses import dataclass

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket
from App.Protocols.Messages.dataClass.pdPacketResponse import pdResponsePacket


@dataclass
class pdSeekReq(pdDataPacket):
    startTime: str
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdSeekReq(**dicts)

@dataclass
class pdSeekRep(pdResponsePacket):
    @staticmethod
    def from_json(_json_string):
        dicts=json.loads(_json_string)
        return pdSeekRep(**dicts)

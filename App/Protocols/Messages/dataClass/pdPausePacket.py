import json
from dataclasses import dataclass

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket
from App.Protocols.Messages.dataClass.pdPacketResponse import pdResponsePacket


@dataclass
class pdPauseReq(pdDataPacket):
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdPauseReq(**dicts)

@dataclass
class pdPauseRep(pdResponsePacket):
    @staticmethod
    def from_json(_json_string):
        dicts=json.loads(_json_string)
        return pdPauseRep(**dicts)


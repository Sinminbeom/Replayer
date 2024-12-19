from dataclasses import dataclass, asdict

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket
from App.Protocols.Messages.dataClass.pdPacketResponse import pdResponsePacket

@dataclass
class pdPlayReq(pdDataPacket):
    sectionId : int
    vehicleId: str
    sensorIdList: []
    startTime: str
    endTime: str
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdPlayReq(**dicts)



@dataclass
class pdPlayRep(pdResponsePacket):
    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdPlayRep(**dicts)


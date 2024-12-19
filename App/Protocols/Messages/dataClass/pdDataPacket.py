import json
from dataclasses import dataclass, asdict

from App.Protocols.Messages.dataClass.pdPacket import pdPacket


@dataclass
class pdDataPacket(pdPacket):
    protocol_id: str
    message_direction: int
    sender: str
    receiver: str

    def SetMessageDirection(self , _message_direction ):
        self.message_direction =_message_direction

    def SetSender(self , _sender ):
        self.sender=_sender

    def SetReceiver(self, _receiver):
        self.receiver = _receiver



    @staticmethod
    def from_json(_json_string):
        dicts = json.loads(_json_string)
        return pdDataPacket(**dicts)

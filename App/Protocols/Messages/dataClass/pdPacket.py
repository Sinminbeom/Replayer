from dataclasses import dataclass, asdict


@dataclass
class pdPacket:


    def to_dict(self):
        return asdict(self)


    def to_json(self):
        import json
        return json.dumps(self.to_dict())
from dataclasses import dataclass, asdict


@dataclass
class pdSectionElement:
    sectionId: int
    startTime: str
    endTime: str

    def to_dict(self):
        return asdict(self)
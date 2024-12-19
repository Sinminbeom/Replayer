import json
from dataclasses import dataclass, asdict

from App.Protocols.Messages.dataClass.pdDataPacket import pdDataPacket
from App.Protocols.Messages.dataClass.pdPacketResponse import pdResponsePacket
from App.Protocols.Messages.dataClass.pdSectionElement import pdSectionElement


@dataclass
class pdPlayAbleListRep(pdResponsePacket):
    sensorIdList: [str]
    sectionList : [pdSectionElement]


    @staticmethod
    def from_json(_json_string):
        dicts=json.loads(_json_string)
        dicts['sectionList'] = [pdSectionElement(**section) for section in dicts['sectionList']]
        return pdPlayAbleListRep(**dicts)

    def to_dict(self):
        dict_obj = asdict(self)
        dict_obj['sectionList'] = [section.to_dict() for section in self.sectionList]
        return dict_obj

@dataclass
class pdPlayAbleListReq(pdDataPacket):
    vehicleId: str
    sensorIdList: []
    startTime: str
    endTime: str

    @staticmethod
    def from_json(_json_string):
        import json
        dicts=json.loads(_json_string)
        return pdPlayAbleListReq(**dicts)


def mainRep():

    str="""{"protocol_id": "100", "sender": "MESSAGE_BRIDGE/MESSAGE_BRIDGE", "receiver": "DOWNLOADER/DOWNLOAD_MANAGER", "vehicleId": "e-100", "sensorIdList": ["LIDAR"], "startTime": "20230602000000", "endTime": "20230602000115"}"""

    c= pdPlayAbleListReq.from_json(str)


def main():

    # """[{ "sectionId" : 0, "startTime":"20230101000000" , "endTime":"20230101000000"} , { "sectionId" : 1, "startTime":"20230101000000" , "endTime":"20230101000000"},{ "sectionId" : 2, "startTime":"20230101000000" , "endTime":"20230101000000"} ]"""
    # json_str="""{"protocol_id": "100", "sender": "MESSAGE_BRIDGE/MESSAGE_BRIDGE", "receiver": "DOWNLOADER/DOWNLOAD_MANAGER", "vehicleId": "e-100", "sensorIdList": ["LIDAR"], sectionList : [{ "sectionId" : 0, "startTime":"20230101000000" , "endTime":"20230101000000"} , { "sectionId" : 1, "startTime":"20230101000000" , "endTime":"20230101000000"},{ "sectionId" : 2, "startTime":"20230101000000" , "endTime":"20230101000000"} ] }"""
    # json_str = """{"protocol_id": "100", "sender": "MESSAGE_BRIDGE/MESSAGE_BRIDGE", "receiver": "DOWNLOADER/DOWNLOAD_MANAGER", "vehicleId": "e-100", "sensorIdList": ["LIDAR"], "sectionList" : [{ "sectionId" : 0, "startTime":"20230101000000" , "endTime":"20230101000000"}, { "sectionId" : 1, "startTime":"20230101000000" , "endTime":"20230101000000"}, { "sectionId" : 2, "startTime":"20230101000000" , "endTime":"20230101000000"} ] }"""
    # json_str = """{"protocol_id": "100", "sender": "MESSAGE_BRIDGE/MESSAGE_BRIDGE", "receiver": "DOWNLOADER/DOWNLOAD_MANAGER", "vehicleId": "e-100", "sensorIdList": ["LIDAR"], "sectionList" : [{"sectionId": 0, "startTime": "20230101000000", "endTime": "20230101000000"}, {"sectionId": 1, "startTime": "20230101000000", "endTime": "20230101000000"}, {"sectionId": 2, "startTime": "20230101000000", "endTime": "20230101000000"}]}"""
    json_str = """{"protocol_id": "100", "sender": "MESSAGE_BRIDGE/MESSAGE_BRIDGE", "receiver": "DOWNLOADER/DOWNLOAD_MANAGER", "code":"OK", "code_nm" :"ok" , "reason":"r", "sensorIdList": ["LIDAR"], "sectionList" : [{"sectionId": 0, "startTime": "20230101000000", "endTime": "20230101000000"}, {"sectionId": 1, "startTime": "20230101000000", "endTime": "20230101000000"}, {"sectionId": 2, "startTime": "20230101000000", "endTime": "20230101000000"}]}"""

    c= pdPlayAbleListRep.from_json(json_str)
    print(c)

    js1=c.to_json()
    print(js1)

    # js= json.dumps(c)
    # print(js)


    o=10
    o=100


    pass

if __name__ == '__main__':
    main()
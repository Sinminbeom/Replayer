from LibUtils.SingletonInstane import SingletonInstane

from App.Common.cDto import IDTO
from App.cDefine import IENUM


class E_SENSOR_TYPE(IENUM):
    ALL = "ALL"

    GNSS = "GNSS"
    LIDAR = "LIDAR"
    CAMERA = "CAMERA"
    TIMER = "TIMER"


class E_TIMER(IENUM):
    TIMER = "TIMER"


class E_GNSS(IENUM):
    GNSS = "GNSS"


class E_LIDAR(IENUM):
    AT128_ROOF_FRONT = "AT128_ROOF_FRONT"
    AT128_ROOF_RIGHT = "AT128_ROOF_RIGHT"
    AT128_ROOF_REAR = "AT128_ROOF_REAR"
    AT128_ROOF_LEFT = "AT128_ROOF_LEFT"
    RSBP_BUMP_FRONT = "RSBP_BUMP_FRONT"
    RSBP_BUMP_RIGHT = "RSBP_BUMP_RIGHT"
    RSBP_BUMP_REAR = "RSBP_BUMP_REAR"
    RSBP_BUMP_LEFT = "RSBP_BUMP_LEFT"


class E_CAMERA(IENUM):
    AM20_FRONT_CENTER_RIGHT_DOWN = "AM20_FRONT_CENTER_RIGHT_DOWN"
    AM20_FRONT_RIGHT_REAR = "AM20_FRONT_RIGHT_REAR"
    AM20_REAR_CENTER_RIGHT = "AM20_REAR_CENTER_RIGHT"
    AM20_FRONT_LEFT_REAR = "AM20_FRONT_LEFT_REAR"
    AM20_REAR_RIGHT_EDGE = "AM20_REAR_RIGHT_EDGE"
    AM20_LEFT_REAR_EDGE = "AM20_LEFT_REAR_EDGE"
    AM20_FRONT_CENTER_LEFT_UP = "AM20_FRONT_CENTER_LEFT_UP"
    AM20_FRONT_CENTER_RIGHT_UP = "AM20_FRONT_CENTER_RIGHT_UP"
    AM20_FRONT_RIGHT_FRONT = "AM20_FRONT_RIGHT_FRONT"
    AM20_FRONT_LEFT_FRONT = "AM20_FRONT_LEFT_FRONT"


class EC_SENSOR(SingletonInstane):

    ## { [] }
    # lists={}

    def __init__(self):
        self.lists = {}
        pass

    # @staticmethod
    def Init(self):
        self.lists = {}

    # @staticmethod
    def Register(self):
        self.Init()

        self.Append(E_SENSOR_TYPE.GNSS, E_GNSS.GNSS)

        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_FRONT)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_RIGHT)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_REAR)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_LEFT)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.RSBP_BUMP_FRONT)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.RSBP_BUMP_RIGHT)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.RSBP_BUMP_REAR)
        self.Append(E_SENSOR_TYPE.LIDAR, E_LIDAR.RSBP_BUMP_LEFT)

        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_CENTER_RIGHT_DOWN)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_RIGHT_REAR)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_REAR_CENTER_RIGHT)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_LEFT_REAR)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_REAR_RIGHT_EDGE)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_LEFT_REAR_EDGE)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_CENTER_LEFT_UP)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_CENTER_RIGHT_UP)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_RIGHT_FRONT)
        self.Append(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_FRONT_LEFT_FRONT)

        self.Append(E_SENSOR_TYPE.TIMER, E_TIMER.TIMER)

        pass

    # @staticmethod
    def Append(self, _sensor_type, _sendor):
        from App.Common.CollectionUtils import CollectionUtils

        if CollectionUtils.DictIsContainKey(self.lists, _sensor_type) == True:
            elements = self.lists.get(_sensor_type)
            if _sendor not in elements:
                elements.append(_sendor)
        else:
            self.lists[_sensor_type] = []
            elements = self.lists.get(_sensor_type)
            if _sendor not in elements:
                elements.append(_sendor)

    # @staticmethod
    def GetSensor(self, _sensor_type, _sensor=None) -> IDTO:
        from App.Category.cSensorDTO import cSensorDTO
        dto = cSensorDTO()

        if _sensor_type == E_SENSOR_TYPE.ALL:
            for s_type, s_lists in self.lists.items():
                for sensor in s_lists:
                    dto.Append(s_type, sensor)

                # dto.AppendSensorType(s_type)
            dto.AppendSensorType(E_SENSOR_TYPE.ALL)
            return dto

        else:

            if _sensor == None:
                for sensor in self.lists.get(_sensor_type):
                    dto.Append(_sensor_type, sensor)

                dto.AppendSensorType(_sensor_type)
                return dto
            else:
                for sensor in self.lists.get(_sensor_type):
                    if _sensor == sensor:
                        dto.Append(_sensor_type, sensor)

                return dto

    # @staticmethod
    def GetSensorArgs(self, _absensor):

        from App.Category.cSensorDTO import cSensorDTO
        from App.Category.cSensorArgs import cSensorArgs
        if cSensorDTO.DELIM in _absensor:
            s = _absensor.split(cSensorDTO.DELIM)
            return cSensorArgs(s[0], s[1])

        else:

            for s_type, s_lists in self.lists.items():

                if _absensor == s_type:
                    return cSensorArgs(_absensor, None)

                for sensor in s_lists:
                    if _absensor == sensor:
                        return cSensorArgs(s_type, sensor)

    ## _sensor_info_lists : [cSensorArgs,cSensorArgs,cSensorArgs,cSensorArgs]
    # @staticmethod
    def SetSensorDtos(self, _absensor_info_lists) -> IDTO:
        from App.Category.cSensorDTO import cSensorDTO
        dtos = cSensorDTO()

        for absensor_info in _absensor_info_lists:
            censorArgs = self.GetSensorArgs(absensor_info)

            # censorArgs= cSensorArgs.Factory(absensor_info)

            self.SetSensorDto(dtos, censorArgs.getSensorType(), censorArgs.getSensor())

        return dtos

    # @staticmethod
    def SetSensorDto(self, _dto, _sensor_type, _sensor=None) -> IDTO:
        dto = _dto

        if _sensor_type == E_SENSOR_TYPE.ALL:
            for s_type, s_lists in self.lists.items():
                for sensor in s_lists:
                    dto.Append(s_type, sensor)

                # dto.AppendSensorType(s_type)
            dto.AppendSensorType(E_SENSOR_TYPE.ALL)
            return dto

        else:

            if _sensor == None:
                for sensor in self.lists.get(_sensor_type):
                    dto.Append(_sensor_type, sensor)

                dto.AppendSensorType(_sensor_type)
                return dto
            else:
                for sensor in self.lists.get(_sensor_type):
                    if _sensor == sensor:
                        dto.Append(_sensor_type, sensor)

                return dto

    # HACK
    def GetLists(self):
        return self.lists


def main():
    EC_SENSOR.instance().Register()

    dto1 = EC_SENSOR.instance().GetSensor(E_SENSOR_TYPE.ALL)
    dto2 = EC_SENSOR.instance().GetSensor(E_SENSOR_TYPE.LIDAR)
    dto3 = EC_SENSOR.instance().GetSensor(E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_REAR)

    dto4 = EC_SENSOR.instance().GetSensor(E_SENSOR_TYPE.CAMERA)
    dto5 = EC_SENSOR.instance().GetSensor(E_SENSOR_TYPE.CAMERA, E_CAMERA.AM20_REAR_RIGHT_EDGE)

    dto1.Println()
    dto2.Println()
    dto3.Println()
    dto4.Println()
    dto5.Println()

    print("===================================================")

    from App.Category.cSensorDTO import cSensorDTO
    dtos = cSensorDTO()

    EC_SENSOR.instance().SetSensorDto(dtos, E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_REAR)
    EC_SENSOR.instance().SetSensorDto(dtos, E_SENSOR_TYPE.LIDAR, E_LIDAR.AT128_ROOF_REAR)
    EC_SENSOR.instance().SetSensorDto(dtos, E_SENSOR_TYPE.CAMERA)
    # E_SENSOR.SetSensorDto(dtos ,E_SENSOR_TYPE.LIDAR)
    # E_SENSOR.SetSensorDto(dtos ,E_SENSOR_TYPE.ALL)

    dtos.Println()

    ar = EC_SENSOR.instance().GetSensorArgs("CAMERA/AM20_REAR_RIGHT_EDGE")
    ar2 = EC_SENSOR.instance().GetSensorArgs(E_LIDAR.AT128_ROOF_REAR)

    # dtos2 = cSensorDTO()

    print("==========================================================")

    dtos2 = EC_SENSOR.instance().SetSensorDtos(
        [E_LIDAR.AT128_ROOF_REAR, E_SENSOR_TYPE.CAMERA, "CAMERA/AM20_REAR_RIGHT_EDGE"])
    dtos2.Println()

    dtos3 = EC_SENSOR.instance().SetSensorDtos(["LIDAR", "CAMERA/AM20_REAR_RIGHT_EDGE"])
    dtos3.Println()
    dtos3.PrintLists()
    print(dtos3.GetSensorsList())

    o = 10
    o = 100

    pass


if __name__ == '__main__':
    main()

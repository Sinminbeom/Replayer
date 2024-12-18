from App.Common.cDto import IDTO


class cSensorArgs(IDTO):
    def __init__(self , _sensor_type , _sensor ):
        IDTO.__init__(self)

        self.sensor_type=_sensor_type
        self.sensor = _sensor

    def getSensorType(self):
        return self.sensor_type

    def getSensor(self):
        return self.sensor
    #
    # @staticmethod
    # def Factory(_absensor) :
    #     from App.Category.eSensor import E_SENSOR
    #     # return E_SENSOR.GetSensorArgs(_absensor)
    #
    #     from App.Category.cSensorDTO import cSensorDTO
    #     if cSensorDTO.DELIM in _absensor:
    #         s = _absensor.split(cSensorDTO.DELIM)
    #         return cSensorArgs(s[0], s[1])
    #
    #     else:
    #
    #         from App.Category.eSensor import E_SENSOR
    #         for s_type, s_lists in E_SENSOR.lists.items():
    #             for sensor in s_lists:
    #                 if _absensor == sensor:
    #                     return cSensorArgs(s_type, sensor)





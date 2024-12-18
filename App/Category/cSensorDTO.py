from App.Common.cDto import IDTO


class cSensorDTO(IDTO):

    DELIM="/"

    def __init__(self):
        IDTO.__init__(self)
        ##{ [] }
        self.lists={}

        self.sensor_type_list=[]

        pass

    def AppendSensorType(self , _sensor_type ):

        if _sensor_type not in self.sensor_type_list:
            self.sensor_type_list.append(_sensor_type)
        pass

    def Append(self , _sensor_type , _sensor):

        if _sensor_type not in self.lists :
            self.lists[_sensor_type]=[]

        li = self.lists.get(_sensor_type)
        if _sensor not in li:
            li.append(_sensor)


    def GetSensorProtocolLists(self):

        protocolSensorLists=[]

        from App.Category.eSensor import E_SENSOR_TYPE
        if E_SENSOR_TYPE.ALL in self.sensor_type_list:
            protocolSensorLists.append(E_SENSOR_TYPE.ALL)

            return protocolSensorLists

        for sensor_type in self.sensor_type_list:
            protocolSensorLists.append(sensor_type)

        for _s_type , _s_lists in self.lists.items():
            if _s_type in protocolSensorLists :
                continue

            for _sensor in _s_lists:
                protocolSensorLists.append( _s_type + cSensorDTO.DELIM +_sensor )

        return protocolSensorLists

    def GetSensorsList(self):
        sensorList = []
        for value in self.lists.values():
            sensorList.extend(value)

        return sensorList


    def Println(self):

        print(self.GetSensorProtocolLists())

    def PrintLists(self):
        print(self.lists)

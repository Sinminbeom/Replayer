from LibUtils.SingletonInstane import SingletonInstane

from App.Category.eCateGory import E_CATE, E_CATE_META_ELE
from App.Common.CollectionUtils import CollectionUtils
from App.Common.cDto import IDTO


class cCateDTO(IDTO):

    def __init__(self):
        IDTO.__init__(self)

        pass

class cProcessCate(SingletonInstane):
    def __init__(self):
        super().__init__()
        self.cateQueue = {}
        # self.cateQueue = {{}}

        self.cateRegActQueue={}
        self.__registCateInfo()

    def Init(self):

        pass
    def GetCateCallback(self , _e_cate1):
        return self.cateRegActQueue.get(_e_cate1)

    def __registCateInfo(self):
        self.cateRegActQueue[E_CATE.MESSAGE_BRIDGE]=lambda: cProcessCate.instance().RegisterMessageBridge()
        self.cateRegActQueue[E_CATE.DOWNLOADER] = lambda: cProcessCate.instance().RegisterDownloader()

    def RegisterMessageBridge(self):
        self.setCate3(E_CATE.MESSAGE_BRIDGE, E_CATE.E_MESSAGE_BRIDGE.COMMON,
                      E_CATE.E_MESSAGE_BRIDGE.E_COMMON.E_MESSAGE_BRIDGE[E_CATE_META_ELE.NAME],
                      E_CATE.E_MESSAGE_BRIDGE.E_COMMON.E_MESSAGE_BRIDGE[E_CATE_META_ELE.LAMBDA])

    def RegisterDownloader(self):
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.COMMON,
                      E_CATE.E_DOWNLOADER.E_COMMON.E_DOWNLOAD_MANAGER[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_COMMON.E_DOWNLOAD_MANAGER[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_RIGHT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_RIGHT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_REAR[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_REAR[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_LEFT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_LEFT[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_FRONT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_FRONT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_RIGHT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_RIGHT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_REAR[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_REAR[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_LEFT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_RSBP_BUMP_LEFT[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.GNSS,
                      E_CATE.E_DOWNLOADER.E_GNSS.E_GNSS[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_GNSS.E_GNSS[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_DOWN[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_DOWN[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_REAR[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_REAR[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_REAR_CENTER_RIGHT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_REAR_CENTER_RIGHT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_LEFT_REAR[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_LEFT_REAR[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_REAR_RIGHT_EDGE[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_REAR_RIGHT_EDGE[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_LEFT_REAR_EDGE[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_LEFT_REAR_EDGE[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_LEFT_UP[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_LEFT_UP[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_UP[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_UP[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_FRONT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_FRONT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_LEFT_FRONT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_LEFT_FRONT[E_CATE_META_ELE.LAMBDA])

    def _extendCate1(self, _cate1):
        return CollectionUtils.DictExtends(self.cateQueue, _cate1, lambda: {})

    def _extendCate2(self, _cate1, _cate2):
        queue = self._extendCate1(_cate1)
        return CollectionUtils.DictExtends(queue, _cate2, lambda: {})

    def getCate1(self, _cate1):
        return CollectionUtils.DictGetValue(self.cateQueue, _cate1)

    def getCate2(self, _cate1, _cate2):
        queue = self.getCate1(_cate1)

        if queue != None:
            return CollectionUtils.DictGetValue(queue, _cate2)

        return None

    def getCate3(self, _cate1, _cate2, _cate3):
        queue = self.getCate2(_cate1, _cate2)

        if queue != None:
            return CollectionUtils.DictGetValue(queue, _cate3)

        return None

    def setCate3(self, _cate1, _cate2, _cate3, _value):
        queue = self._extendCate2(_cate1, _cate2)
        queue[_cate3] = _value

    def GetProcessListsCate(self, *_cate):
        if len(_cate) == 1:
            return self.GetProcessListsCate1(*_cate)

        if len(_cate) == 2:
            return self.GetProcessListsCate2(*_cate)

        if len(_cate) == 3:
            return self.GetProcessListsCate3(*_cate)

        raise Exception

    def GetProcessListsCate1(self, _cate1):
        retLists = []
        cateLists = self.getCate1(_cate1)

        for cate2_nm in cateLists:
            lis = self.GetProcessListsCate2(_cate1, cate2_nm)
            retLists.extend(lis)

        return retLists

    def GetProcessListsCate2(self, _cate1, _cate2):
        cateLists = self.getCate2(_cate1, _cate2)
        retLists = []

        for key, value in cateLists.items():
            retLists.append((key, value))

        return retLists

    def GetProcessListsCate3(self, _cate1, _cate2, _cate3):
        retLists = []

        cate3 = self.getCate3(_cate1, _cate2, _cate3)

        if cate3 != None:
            retLists.append((_cate3, cate3))

        return retLists

    def GetProcessNameListsCate1(self, _cate1):
        retLists = []
        cateLists = self.getCate1(_cate1)

        for cate2_nm in cateLists:
            lis = self.GetProcessNameListsCate2(_cate1, cate2_nm)
            retLists.extend(lis)

        return retLists

    def GetProcessNameListsCate2(self, _cate1, _cate2):
        cateLists = self.getCate2(_cate1, _cate2)
        retLists = []

        for key, value in cateLists.items():
            retLists.append(key)

        return retLists

    def GetProcessNameListsCate3(self, _cate1, _cate2, _cate3):
        retLists = []

        cate3 = self.getCate3(_cate1, _cate2, _cate3)

        if cate3 != None:
            retLists.append(_cate3)

        return retLists

    def GetProcessNameList(self, *_cate):
    # def GetProcessNameList(self, _cate):
    #     splitCate = _cate.split(".")

        if len(_cate) == 3:
            return self.GetProcessNameListsCate3(*_cate)


        if len(_cate) == 2:
            return self.GetProcessNameListsCate2(*_cate)


        if len(_cate) == 1:
            # return self.GetProcessNameListsCate1(splitCate[0])
            return self.GetProcessNameListsCate1(*_cate)

        raise Exception

    def Test1(self):

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST,
                      E_CATE.E_DOWNLOADER.E_TEST.E_PP1[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_TEST.E_PP1[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST,
                      E_CATE.E_DOWNLOADER.E_TEST.E_PP2[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_TEST.E_PP2[E_CATE_META_ELE.LAMBDA])

        cate1Test = self.getCate1(E_CATE.DOWNLOADER)
        for key, value in cate1Test.items():
            print(key, value)

        # li1 = self.GetProcessListsCate1(E_CATE.DOWNLOADER)
        li1 = self.GetProcessNameListsCate2(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST)
        print("asdf")
        print(li1)
        print("asdf")

        li2 = self.GetProcessListsCate2(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST)

        li3 = self.GetProcessListsCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST, E_CATE.E_DOWNLOADER.E_TEST.PP1)

        # self.GetProcessListsCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST, E_CATE.getProcessNameByCate3(E_CATE.E_DOWNLOADER.E_TEST.PP1) )

        E_CATE.getProcessNameByCate3(E_CATE.E_DOWNLOADER.E_TEST.PP1)

        cate2Test = self.getCate2(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.TEST)

        for key, value in cate2Test.items():
            print(key, value)
            # value()
            # mp.append(value(d,f))

        o = 10
        o = 100

    def Test2(self):

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.SENSOR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_RIGHT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_RIGHT[E_CATE_META_ELE.LAMBDA])
        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.SENSOR,
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_DOWN[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_CENTER_RIGHT_DOWN[E_CATE_META_ELE.LAMBDA])

        self.setCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_REAR[E_CATE_META_ELE.NAME],
                      E_CATE.E_DOWNLOADER.E_CAMERA.E_AM20_FRONT_RIGHT_REAR[E_CATE_META_ELE.LAMBDA])

        cate2Camera = self.getCate2(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA)
        cate2Sensor = self.getCate2(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.SENSOR)

        cate3Am20FrontLeftFront = self.getCate3(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.CAMERA,
                                                E_CATE.E_DOWNLOADER.E_CAMERA.AM20_FRONT_CENTER_RIGHT_DOWN[
                                                    E_CATE_META_ELE.NAME])

        cate1Test = self.getCate1(E_CATE.DOWNLOADER)

        o = 10
        o = 100


def TTT2():
    cProcessCate.instance().Init()
    cProcessCate.instance().RegisterDownloader()

    # test = cProcessCate.instance().GetProcessNameList(E_CATE.DOWNLOADER)  ## ALL
    cateList = cProcessCate.instance().GetProcessListsCate(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.LIDAR)
    for _process_factory in cateList:
        _process_factory[E_CATE_META_ELE.LAMBDA]("test", _process_factory[E_CATE_META_ELE.NAME])
            # _process_factory[E_CATE_META_ELE.LAMBDA](self.GetAppNAme(), _process_factory[E_CATE_META_ELE.NAME])

    # cProcessCate.instance().GetProcessNameList(E_CATE.E_DOWNLOADER.SENSOR, E_CATE.E_DOWNLOADER.CAMERA,
    #                                            E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)

    pass


def TTT():
    cProcessCate.instance().Init()
    cProcessCate.instance().RegisterDownloader()
    print(cProcessCate.instance().GetProcessNameList("DOWNLOADER.SENSOR"))
    print(cProcessCate.instance().GetProcessNameList("DOWNLOADER.SENSOR.AT128_ROOF_FRONT"))

    cProcessCate.instance().GetProcessNameList(E_CATE.DOWNLOADER)  ## ALL

    class argsClass:

        def __init__(self, _sensor_type, _sensor=None, _protocol_mes=None):
            pass

        def __init__(self, _absensor):
            ## /

            pass

    argsClass(E_CATE.E_DOWNLOADER.SENSOR)
    argsClass(E_CATE.E_DOWNLOADER.SENSOR.AT_128)

    argsClass(_sensor_type=None, _sensor=None, _protocol_mes="dasdasdasd/asdasdasdas")

    cProcessCate.instance().GetProcessNameList(E_CATE.E_DOWNLOADER.SENSOR, E_CATE.E_DOWNLOADER.CAMERA,
                                               E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)

    ## [SENSOR]

    ## ["SENSOR" , CAMERA , SENSOR/AT128_ROOF_FRONT]

    ## SENSOR/AT128_ROOF_FRONT

    # "DOWNLOADER.SENSOR"
    # "DOWNLOADER.SENSOR.AT128_ROOF_FRONT"

    cProcessCate.instance().GetProcessNameList(E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)


def main():
    cProcessCate.instance().Init()
    # cProcessCate.instance().Test2()
    # cProcessCate.instance().Test1()

    # cProcessCate.instance().Test123()

    o = 10
    o = 100

    nm = E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT
    print(nm)

    cate3Name = E_CATE.getProcessNameByCate3(E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT)

    print(E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)

    print(cate3Name)


    print("===========================================================================")

    cate3Name = E_CATE.getProcessNameByCate3(E_CATE.E_DOWNLOADER.E_LIDAR.E_AT128_ROOF_FRONT)



    pass


def t3():
    cProcessCate.instance().Test2()

    pass


def t2(*args):
    print(args)

    lb = lambda a, b, c: print(f" {c} == {a + b} ")

    for arg in args:
        print(arg)

    lb(*args)

    pass

def t5():
    cProcessCate.instance().Init()

    cProcessCate.instance().RegisterWebT()

    # cate1 = cProcessCate.instance().GetProcessListsCate(E_CATE.DOWNLOADER)
    #
    # o=10
    #
    # cate2 = cProcessCate.instance().GetProcessListsCate(E_CATE.DOWNLOADER , E_CATE.E_DOWNLOADER.LIDAR)

    # for processElement in cate2:
    #     print( processElement[0] )

    name_list = cProcessCate.instance().GetProcessNameList(E_CATE.WEB_T, E_CATE.E_WEB_T.CRAWLER)

    for processElement in name_list:
        print( processElement )

    o = 100

    # GetProcessListsCate2
    pass

if __name__ == '__main__':
    # t3()
    # TTT()
    # t2(1,2,'korea')
    # main()
    # t5()
    TTT2()

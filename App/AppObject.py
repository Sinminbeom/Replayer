from abc import abstractmethod

from MultiProcess.cMultiProcesser import cMultiProcesser
from App.Category.cCateGory import cProcessCate, E_CATE, E_CATE_META_ELE

class IApp:
    def __init__(self):
        # self.Init()
        pass

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def OnRun(self):
        pass

    def Run(self):
        try:
            while True:
                self.OnRun()
                pass
        except Exception as e:
            print(f"============================== EEEE {e}")
            pass

class cABApp( IApp ):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def OnRun(self):
        pass

class cMpApp(cABApp):

    def __init__(self , _app_name,  _process_cnt=0 ):
        cABApp.__init__(self)
        self.app_name=_app_name
        self.mp=cMultiProcesser(_process_cnt)

    def AddProcess(self,_process):
        self.mp.Append(_process)

    def AssineShardQueueEx(self,_process):
        self.mp.AssineShardQueueEx(_process)

    def getMP(self):
        return self.mp
    def GetAppNAme(self):
        return self.app_name

    @abstractmethod
    def Init(self):
        print("init")

    @abstractmethod
    def OnRun(self):
        pass

class cMpAppFromCate(cMpApp):

    def __init__(self, _app_name , *_cate ):
        cateList = cProcessCate.instance().GetProcessListsCate(*_cate)
        cMpApp.__init__(self,_app_name , len(cateList))
        self._appendProcessCate(cateList)

    def _appendProcessCate(self, cateList):
        for _process_factory in cateList:
            self.AddProcess(
                _process_factory[E_CATE_META_ELE.LAMBDA](self.GetAppNAme(), _process_factory[E_CATE_META_ELE.NAME])
            )

    @abstractmethod
    def Init(self):
        print("init")
        pass

    @abstractmethod
    def OnRun(self):
        # print("onrun")
        pass

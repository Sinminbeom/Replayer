import time
from abc import abstractmethod

from MultiProcess.abProcess import abProcess

from App.Common.State.cStateComponents import cStateComponents


class abStepProcess( abProcess ):

    def __init__(self , _app_name, _process_nm ,_queue_ex_name=None ):
        abProcess.__init__(self,  _process_nm , False ,  _queue_ex_name)
        self.StateComponents=None
        self.AppName=_app_name

    def setStateComponent(self,_state_info_lists ,  _init_state ):
        self.StateComponents=cStateComponents(self , _state_info_lists ,  _init_state)

    def GetAppName(self):
        return self.AppName

    def _shardQueuePopWithLockSelf(self):
        return self._shardQueuePopWithLock(self.name)

    def _shardQueuePopSelf(self):
        return self._shardQueuePop(self.name)

    # def Running(self, process):
    #     self.OnInit()
    #     self.OnProcOnce()
    #     pass

    def Action(self, process):

        self._setStart()
        self.OnInit()
        self.OnProcOnce()

        try:
            while self.GetRunning():
                self.OnProcEveryFrame()

                if self.StateComponents != None:
                    self.StateComponents.OnProcEveryFrame()
                    self.StateComponents.OnChangeState()

                time.sleep(0.001)
        except Exception as e:
            print("e:",e)
            self._setStop()
            raise

    @abstractmethod
    def OnInit(self):

        pass

    @abstractmethod
    def OnProcOnce(self):

        pass

    @abstractmethod
    def OnProcEveryFrame(self):
        # if self.StateComponents != None:
        #     self.StateComponents.OnProcEveryFrame()


        pass


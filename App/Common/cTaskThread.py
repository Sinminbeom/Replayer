import threading
import time
from abc import abstractmethod

from ThreadUtils.abThreading import abThreading



class cTaskThread(abThreading):
    def __init__(self ):
        abThreading.__init__(self)
        # self.lamda =_lamda

        self.IsOnStart=False
        self._lock = threading.Lock()
        self.actQueue=[]


        self.clearQueueReserve=False

    # @abstractmethod
    # def run(self):
    #     self.lamda()

    def Start(self):

        from ThreadUtils.abThread import abThread
        if self.IsOnStart==False:
            self.start()
            self.IsOnStart=True

            self.setThreadStatus(abThread.E_THREAD_STATUS.RUNNING)

        # from ThreadUtils.abThread import abThread
        # self._stop.clear()
        # self.setThreadStatus(abThread.E_THREAD_STATUS.RUNNING)
        pass

    def RunTask(self,_lambda):

        with self._lock:
            self._setLambda(_lambda)
            self.Start()

    def run(self):
        while not self.IsStop():
            # print("a1")
            self.Action()
            # print("a2")
            time.sleep(0.01)
            # print("a3")
    def _setLambda(self,_lambda):
        self.actQueue.append(_lambda)
        # print("aaaaaaaaaaaaaaaa")

    def ClearActQueue(self):
        self.__reserveClearQueue()

    def __reserveClearQueue(self):
        self.clearQueueReserve = True
        pass
    def __clearQueue(self):

        if self.clearQueueReserve==True:
            self.actQueue=[]
            self.clearQueueReserve=False

    def Action(self):

        with self._lock:
            # print(f" ----------------------  len:  {len(self.actQueue)}")
            while len(self.actQueue) > 0:
                # print("popopop")
                self.actQueue.pop(0)()
                self.__clearQueue()



def print_test(mes):

    print(f"st>>>>>>>>>>>>>>>>>>>>>>>>>>{mes}")
    time.sleep(1)
    print(f"ed>>>>>>>>>>>>>")

    pass

def main():
    t=cTaskThread()


    t.RunTask( lambda  : print_test("a") )


    # t.Stop()

    # time.sleep(2)

    t.RunTask( lambda  : print_test("b") )

    # time.sleep(2)
    t.RunTask( lambda  : print_test("c") )

    # time.sleep(2)
    t.RunTask( lambda  : print_test("d") )

    # t.ClearActQueue()

    # t.Stop()

    t.RunTask(lambda: print_test("e"))

    # t.Stop()

    time.sleep(0.1)
    t.ClearActQueue()
    t.RunTask(lambda: print_test("e"))

    while True:

        print("1 sec")

        time.sleep(10)


if __name__ == '__main__':
    main()



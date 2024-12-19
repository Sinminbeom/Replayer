from abc import abstractmethod

import redis
from MultiProcess.abProcess import abProcess
from MultiProcess.cMultiProcesser import cMultiProcesser

from App.Common.cQueueControlProcess import cQueueControlProcess
from App.Common.cStepProcess import abStepProcess
from App.Common.eventBus import cEventBus, cImdgBus
from App.Protocols.cResponseCode import cResponseCode
from App.cDefine import Def, E_RUN_MODE


class cBusProcess(cQueueControlProcess):


    def __init__(self , _app_name ,_process_name , _channel_name , _cate_reg_key = None ):
        cQueueControlProcess.__init__(self ,_app_name=_app_name, _process_nm=_process_name, _cateRegKey=_cate_reg_key ,_queue_ex_name=None)
        self._channel_name = _channel_name
        self.imdgBus=None

    @abstractmethod
    def OnInit(self):
        cQueueControlProcess.OnInit(self)

        # cProjectConfig.instance()

        _imdg = redis.StrictRedis(host=Def.DefRedis.IP, port=Def.DefRedis.PORT)
        self.imdgBus = cImdgBus(_imdg, self._channel_name, self)
        self.imdgBus.Start()

        pass
    @abstractmethod
    def OnProcOnce(self):
        # self.receiver.Start()
        pass

    @abstractmethod
    def OnProcEveryFrame(self):
        pass
    @abstractmethod
    def BusBridgeMessage(self,_message):
        # print( "cBusProcess : " , _message)
        pass

    def SendMessageImdg(self,_message):
        self.imdgBus.sendMessqageImdgQueue(_message)

    def SendMessageReqImdg(self,_protocol_id , _receiver_app_process_nm , *_message_args):
        self.imdgBus.sendMessqageReqImdgQueue(_protocol_id , _receiver_app_process_nm , *_message_args)

    def SendMessageRepImdg(self,_protocol_id, _receiver_app_process_nm, *_message_args , _response_code=cResponseCode.FactoryOK()):
        self.imdgBus.sendMessqageRepImdgQueue(_protocol_id , _receiver_app_process_nm , *_message_args , _response_code=_response_code)



class simbus(cBusProcess):

    def __init__(self,_process_name , _channel_name ):
        cBusProcess.__init__(self,_process_name , _channel_name )

    @abstractmethod
    def OnInit(self):
        cBusProcess.OnInit(self)

    @abstractmethod
    def BridgeMessage(self,_message):
        print( "== BridgeMessage : " , _message)
        pass
    @abstractmethod
    def BusBridgeMessage(self,_message):
        print( "RECV BusBridgeMessage : " , _message)
        self.innerQueueBus.SendMessqage("n2",_message)


class simqTest(cQueueControlProcess):
    def __init__(self ,_app_name, _process_nm):
        cQueueControlProcess.__init__(self,_app_name,_process_nm)

    @abstractmethod
    def OnInit(self):
        cQueueControlProcess.OnInit(self)
        pass


    @abstractmethod
    def BridgeMessage(self,_message):
        print( "== simqTest : " , _message)
        pass

def main():
    mp = cMultiProcesser(3)

    chnm= Def.getIMDGChannelNM()

    print(chnm)

    mp.Append(simbus( "n1" , chnm ))
    mp.Append(simqTest( "n2"))


    mp.IsRunning()

    mp.RunAsync()

    while True:


        pass

    pass

if __name__ == '__main__':
    main()








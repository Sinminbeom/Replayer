from App.Common.cBusProcess import cBusProcess

class cSocketIOProcess(cBusProcess):
    def __init__(self,_app_name, _process_name):
        from App.cDefine import Def
        cBusProcess.__init__(self, _app_name ,_process_name, Def.getIMDGChannelNM())
        self.wsServer=None

        self.rest_server_bind_ip=Def.RestServer.getBindIP()
        self.rest_server_bind_port = Def.RestServer.getBindPort()


    def GetSocketIOServer(self):
        return self.wsServer

    def GetSocketIO(self):
        return self.GetSocketIOServer().socketIO

    def OnInit(self):
        cBusProcess.OnInit(self)
        from App.Rest.cWebSocketServer import socketIOServer
        self.wsServer= socketIOServer(self,self.rest_server_bind_ip,self.rest_server_bind_port)
        self.wsServer.Start()


        pass


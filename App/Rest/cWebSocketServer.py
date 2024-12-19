import json
from abc import abstractmethod

from flask_socketio import send


class abWebSocketServer:

    def __init__(self, _parents_process, _bind_ip='0.0.0.0', _port=9999):
        self.parents_process = _parents_process

        from flask import Flask
        self.socketIOApp = Flask(__name__)
        self.socketIOApp.secret_key = "mysecret"

        self.bindIP = _bind_ip
        self.port = _port

        from flask_socketio import SocketIO
        self.socketIO = SocketIO(self.socketIOApp)

        self.Init()

    def Init(self):
        self.OnInit()

        pass

    def Start(self):
        # self.socketIO.run(self.socketIOApp, debug=False, port=9999, allow_unsafe_werkzeug=True)
        self.socketIO.run(self.socketIOApp, debug=False, host=self.bindIP, port=self.port, allow_unsafe_werkzeug=True)

        pass

    def __getApp(self):
        return self.socketIOApp

    @abstractmethod
    def OnInit(self):
        pass

    def GetParentsProcess(self):
        return self.parents_process
        pass


class socketIOServer(abWebSocketServer):

    def __init__(self, _parents_process, _bind_ip, _bind_port):
        abWebSocketServer.__init__(self, _parents_process, _bind_ip, _bind_port)

        # from App.Protocols.cProtocolMeta import cProtocolMeta
        # cProtocolMeta.Init()

    @staticmethod
    def PlayableListRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  PlayableListRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PLAYABLE_LIST_REQ)(
            sender, receiver,
            _protocol_message.vehicleId,
            _protocol_message.sensorIdList,
            _protocol_message.startTime, _protocol_message.endTime
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def PlayableListResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  PlayableListResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        sectionList = []

        from App.Protocols.Messages.dataClass.pdSectionElement import pdSectionElement
        for sectionInfo in _protocol_message.GetSectionList():
            sectionList.append(
                pdSectionElement(sectionInfo.GetSectionId(), sectionInfo.GetStartTime(), sectionInfo.GetEndTime()))

            pass

        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_PLAYABLE_LIST_REP)(
            sender, receiver,
            _protocol_message.GetReturnCode(), _protocol_message.GetReturnCodeNM(),
            _protocol_message.GetReturnCodeReason(),
            _protocol_message.GetSensorIdList(), sectionList
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    # @staticmethod
    # def StreamerReadyResponse(_process, _protocol_rapper, _protocol_message):
    #     print("socketIOServer Call Back  StreamerReadyResponse")
    #
    #     # to ui
    #     from App.Protocols.cProtocolMeta import cProtocolMeta
    #     from App.Category.eCateGory import E_CATE
    #     sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
    #     receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)
    #
    #     from App.Protocols.cCodeDTO import cCodeDTO
    #     packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_STREAMER_READY_REP)(
    #         sender, receiver,
    #         _protocol_message.GetPipeLineState(),
    #         cCodeDTO.FactoryWithResponseProtocolMessageObject(_protocol_message)
    #     )
    #     packetMessage = cProtocolMeta.GetProtocolPacketMessage(packetObject)
    #     _process.SendMessageImdg(packetMessage)
    #
    #     try:
    #         packetObjectJson = packetObject.to_json()
    #         _process.GetSocketIO().emit("message", packetObjectJson)
    #     except Exception as e:
    #         ##TODO
    #         _process.GetSocketIO().emit("message", "error")
    #         print(f" Error ProcessNM : {_process.GetName()} err: {e}")
    #         pass

    @staticmethod
    def PlayRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  PlayableListRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PLAY_REQ)(
            sender, receiver,
            _protocol_message.sectionId,
            _protocol_message.vehicleId,
            _protocol_message.sensorIdList,
            _protocol_message.startTime, _protocol_message.endTime
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def PlayResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  PlayResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        from App.Protocols.cResponseCode import cResponseCode
        # cCodeDTO.FactoryWithResponseProtocolMessageObject(_protocol_message)

        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_PLAY_REP)(
            sender, receiver,
            cResponseCode.FactoryWithResponseProtocolMessageObject(_protocol_message)
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    @staticmethod
    def CloseRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  StopRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.CLOSE_REQ)(
            sender, receiver
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def CloseResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  StopResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_CLOSE_REP)(
            sender, receiver,
            _protocol_message.GetReturnCode(), _protocol_message.GetReturnCodeNM(),
            _protocol_message.GetReturnCodeReason()
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    ###############################################################################################################
    @staticmethod
    def CrawlingRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  CrawlingRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        aa = _protocol_message.uri
        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.CRAWLING_REQ)(
            sender, receiver,
            _protocol_message.uri
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def CrawlingResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  CrawlingResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REP)(
            sender, receiver,
            _protocol_message.GetSCode()
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    ###############################################################################################################

    @staticmethod
    def StopRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  StopRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.STOP_REQ)(
            sender, receiver
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def StopResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  StopResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_STOP_REP)(
            sender, receiver,
            _protocol_message.GetReturnCode(), _protocol_message.GetReturnCodeNM(),
            _protocol_message.GetReturnCodeReason()
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    @staticmethod
    def DownloadingThresholdNotiRecv(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  DownloadingThresholdNotiRecv")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(
            cProtocolMeta.E_PROTOCOL_ID.PD_DOWNLOADING_THRESHOLD_NOTI)(
            sender, receiver,
            _protocol_message.GetThresholdType()
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    @staticmethod
    def PauseRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  PauseRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PAUSE_REQ)(
            sender, receiver
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def PauseResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  PauseResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_PAUSE_REP)(
            sender, receiver,
            _protocol_message.GetReturnCode(), _protocol_message.GetReturnCodeNM(),
            _protocol_message.GetReturnCodeReason()
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    @staticmethod
    def SeekRequest(_process, _protocol_rapper, _protocol_message):
        print("Call Back  SeekRequest")

        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE

        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE)

        message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.SEEK_REQ)(
            sender, receiver, _protocol_message.startTime
        )

        packetMessage = cProtocolMeta.GetProtocolPacketMessage(message)
        _process.SendMessageImdg(packetMessage)

    @staticmethod
    def SeekResponse(_process, _protocol_rapper, _protocol_message):
        print("socketIOServer Call Back  SeekResponse")

        ## to ui
        from App.Protocols.cProtocolMeta import cProtocolMeta
        from App.Category.eCateGory import E_CATE
        sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.REST_SERVER)
        receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.UI)

        ## ERR
        from App.Protocols.cResponseCode import cResponseCode
        packetObject = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.PD_SEEK_REP)(
            sender, receiver,
            cResponseCode.FactoryWithResponseProtocolMessageObject(_protocol_message)
        )

        try:
            packetObjectJson = packetObject.to_json()
            _process.GetSocketIO().emit("message", packetObjectJson)
        except Exception as e:
            ##TODO
            _process.GetSocketIO().emit("message", "error")
            print(f" Error ProcessNM : {_process.GetName()} err: {e}")
            pass

    def OnInit(self):
        from App.Protocols.cProtocolMeta import cProtocolMeta
        cProtocolMeta.Init()
        self.GetParentsProcess().OnRegisterHandler(cProtocolMeta.GetReceiveHandlerContainer())

        @self.socketIOApp.route('/')
        def hello_world():
            return "Hello Gaemigo Project Home Page!!"

        @self.socketIOApp.route('/chat')
        def chatting():
            from flask import render_template
            return render_template('chat2.html')

        @self.socketIO.on("message")
        def request(message):
            print("message : " + message)

            parsed_dict = json.loads(message)

            protocol_id = parsed_dict["protocol_id"]
            receiver_nm = parsed_dict["receiver"]

            # self.socketIO.emit("message_event", "meeeee")
            # send("me1")

            if receiver_nm != self.GetParentsProcess().GetName():
                print("Rest Server Recv Packet MissMatch!!")
                return

            messageObject = cProtocolMeta.GetJsonDecoder(protocol_id)(message)

            from App.Protocols.Protocol import cProtocolRapper
            rapper = cProtocolRapper.GetProtocolRapper(messageObject)
            # packetMessage = rapper.getProtocolPacketMessage()

            recvHandler = cProtocolMeta.GetReceiveHandler(protocol_id, receiver_nm)
            recvHandler(self.GetParentsProcess(), rapper, messageObject)

            ## TODO 패킷 별로 콜백을 등록 해야함...

            # to_client['message'] = message+"1"
            # to_client['type'] = 'normal'
            # send(to_client, broadcast=True)

            # SendMessageImdg()

            # from App.Protocols.Protocol import cProtocolRapper
            # m= cProtocolRapper.GetProtocolRapper(mo).getProtocolPacketMessage()
            # print(m)

            # if message == 'new_connect':
            #     print("11111111111111")
            #     to_client['message'] = "새로운 유저가 난입하였다!!"
            #     to_client['type'] = 'connect'
            # else:
            #     print("222222222222")
            #     to_client['message'] = message+"1"
            #     to_client['type'] = 'normal'
            # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)

            # self.messageBus.SendMessage(f" Recv : {message}")
            # send(to_client, broadcast=True)

        pass


def main():
    # w=cS()
    # w.Start()

    pass


if __name__ == '__main__':
    main()


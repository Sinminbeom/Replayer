from App.cDefine import IENUM




class E_PROTOCOL_META_ELE(IENUM):

    OBJECT_FACTOR=0
    JSON_DECODE=1
    RECEIVE_CALLBACK=2
    INR_GROUP_RECEIVE_CALLBACK=3
    pass


class cProtocolMeta:
    class E_PROTOCOL_ID:
        ## ----> [ PD REQ/REP SECTION ] <---- ##
        PD_PLAYABLE_LIST_REQ = "PD_100"
        PD_PLAYABLE_LIST_REP = "PD_101"


        PD_PLAY_REQ = "PD_200"
        PD_PLAY_REP = "PD_201"

        PD_CLOSE_REQ = "PD_300"
        PD_CLOSE_REP = "PD_301"

        PD_PAUSE_REQ = "PD_400"
        PD_PAUSE_REP = "PD_401"

        PD_SEEK_REQ = "PD_500"
        PD_SEEK_REP = "PD_501"

        PD_STOP_REQ = "PD_600"
        PD_STOP_REP = "PD_601"


        ## ----> [ PD NOTI SECTION ] <---- ##
        PD_DOWNLOADING_THRESHOLD_NOTI = "PD_700"

        PD_CRAWLING_REQ = "PD_800"
        PD_CRAWLING_REP = "PD_801"


        ## ----> [ REQ/REP SECTION ] <---- ##
        PLAYABLE_LIST_REQ = "100"
        PLAYABLE_LIST_REP = "101"

        PLAY_REQ = "200"
        PLAY_REP = "201"

        CLOSE_REQ = "300"
        CLOSE_REP = "301"

        PAUSE_REQ = "400"
        PAUSE_REP = "401"

        SEEK_REQ = "500"
        SEEK_REP = "501"

        STOP_REQ = "600"
        STOP_REP = "601"

        ## ----> [ NOTI SECTION ] <---- ##
        DOWNLOADING_THRESHOLD_NOTI = "700"
        ERROR_NOTI = "710"

        CRAWLING_REQ = "800"
        CRAWLING_REP = "801"


        ## ----> [ INR REQ/REP SECTION ] <---- ##
        INR_PLAYABLE_LIST_REQ = "-100"
        INR_PLAYABLE_LIST_REP = "-101"

        INR_PLAY_REQ = "-200"
        INR_PLAY_REP = "-201"

        INR_CLOSE_REQ = "-300"
        INR_CLOSE_REP = "-301"
        INR_TIME_CLOSE_REQ = "-310"
        INR_TIME_CLOSE_REP = "-311"

        INR_SEEK_REQ = "-500"
        INR_SEEK_REP = "-501"

        INR_STOP_REQ = "-600"
        INR_STOP_REP = "-601"

        ## ----> [ INR NOTI SECTION ] <---- ##


        INR_DOWNLOADING_THRESHOLD_NOTI = "-700"
        INR_DOWNLOADING_REPORT_NOTI = "-800"

        INR_SUB_MODULE_STATE_CHANGE_NOTI = "-900"

        INR_STREAMER_ERROR_NOTI = "-1000"
        INR_STREAMING_THRESHOLD_NOTI = "-1100"
        INR_STREAMING_TARGET_TIME_NOTI = "-1200"
        INR_STREAMING_TIMER_NOTI = "-1210"
        INR_STREAMING_TERMINATE_NOTI = "-1300"



        INR_CRAWLING_REQ = "-1800"
        INR_CRAWLING_REP = "-1801"


    TABLE={}

    @staticmethod
    def Init():

        # Common Import
        from App.MessageBridge.Processes.cMessageBridgeProcess import cMessageBridgeProcess
        from App.Downloader.Manager.cDownloaderManager import cDownloaderManager
        from App.Downloader.ObjectStorage.cDownloaderModule import cDownloaderModule
        from App.Rest.cWebSocketServer import socketIOServer

        # ------------------------------> Playable Req Section


        from App.Category.eCateGory import E_CATE

        ##################################              ##################################
        ##################################     PD       ##################################
        ##################################              ##################################

        from App.Protocols.Messages.dataClass.pdPlayAbleListPacket import pdPlayAbleListReq
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PLAYABLE_LIST_REQ] = (
            lambda _sender, _receiver, _vehicleId, _sensorIdList, _startTime, _endTime: pdPlayAbleListReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_PLAYABLE_LIST_REQ,E_PROTOCOL_MESSAGE_DIRECTION.REQUEST , _sender, _receiver, _vehicleId, _sensorIdList,
                _startTime, _endTime),
            lambda _protocol_message: pdPlayAbleListReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,protocol_message: socketIOServer.PlayableListRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            } ,
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdPlayAbleListPacket import pdPlayAbleListRep
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PLAYABLE_LIST_REP] = (
            lambda _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason , _sensorIdList, _sectionList : pdPlayAbleListRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_PLAYABLE_LIST_REP, E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE, _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason , _sensorIdList, _sectionList),
            lambda _protocol_message: pdPlayAbleListRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda _process, _protocol_rapper,
                                          _protocol_message : socketIOServer.PlayableListResponse(_process,
                                                                                                  _protocol_rapper,
                                                                                                  _protocol_message)
            },
            {

            }
        )


        from App.Protocols.Messages.dataClass.pdPlayPacket import pdPlayReq
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PLAY_REQ] = (
            lambda _sender, _receiver, _sectionId, _vehicleId, _sensorIdList, _startTime, _endTime: pdPlayReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_PLAY_REQ, E_PROTOCOL_MESSAGE_DIRECTION.REQUEST, _sender, _receiver, _sectionId, _vehicleId, _sensorIdList, _startTime, _endTime),
            lambda _protocol_message: pdPlayReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER:lambda process, protocol_rapper, protocol_message: socketIOServer.PlayRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdPlayPacket import pdPlayRep
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PLAY_REP] = (
            lambda _sender, _receiver, _return_code_dto: pdPlayRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_PLAY_REP, E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE, _sender, _receiver, _return_code_dto.GetCode() ,_return_code_dto.GetCodeNM() , _return_code_dto.GetReason()),
            lambda _protocol_message: pdPlayRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER:lambda process, protocol_rapper, protocol_message: socketIOServer.PlayResponse(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )


        from App.Protocols.Messages.dataClass.pdClosePacket import pdCloseReq
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_CLOSE_REQ] = (
            lambda _sender, _receiver: pdCloseReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_CLOSE_REQ, E_PROTOCOL_MESSAGE_DIRECTION.REQUEST, _sender, _receiver),
            lambda _protocol_message: pdCloseReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.CloseRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )


        from App.Protocols.Messages.dataClass.pdClosePacket import pdCloseRep
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_CLOSE_REP] = (
            lambda _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason: pdCloseRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_CLOSE_REP, E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE , _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason),
            lambda _protocol_message: pdCloseRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,protocol_message: socketIOServer.CloseResponse(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )


        from App.Protocols.Messages.dataClass.pdPausePacket import pdPauseReq
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PAUSE_REQ] = (
            lambda _sender, _receiver: pdPauseReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_PAUSE_REQ, E_PROTOCOL_MESSAGE_DIRECTION.REQUEST , _sender, _receiver),
            lambda _protocol_message: pdPauseReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.PauseRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdPausePacket import pdPauseRep
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_PAUSE_REP] = (
            lambda _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason: pdPauseRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_PAUSE_REP,E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE , _sender, _receiver, _return_code , _return_code_nm ,_return_code_reason),
            lambda _protocol_message: pdPauseRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,protocol_message: socketIOServer.PauseResponse(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdSeekPacket import pdSeekReq,pdSeekRep
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_SEEK_REQ] = (
            lambda _sender, _receiver: pdSeekReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_SEEK_REQ,E_PROTOCOL_MESSAGE_DIRECTION.REQUEST, _sender, _receiver),
            lambda _protocol_message: pdSeekReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.SeekRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_SEEK_REP] = (
            lambda _sender, _receiver, _return_code_dto: pdSeekRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_SEEK_REP, E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE ,_sender, _receiver,_return_code_dto.GetCode() ,_return_code_dto.GetCodeNM() , _return_code_dto.GetReason()),
            lambda _protocol_message: pdSeekRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,protocol_message: socketIOServer.SeekResponse(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdStopPacket import pdStopReq , pdStopRep
        ## JOB
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_STOP_REQ] = (
            lambda _sender, _receiver: pdStopReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_STOP_REQ,E_PROTOCOL_MESSAGE_DIRECTION.REQUEST, _sender, _receiver),
            lambda _protocol_message: pdStopReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.StopRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_STOP_REP] = (
            lambda _sender, _receiver, _return_code, _return_code_nm, _reason: pdStopRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_STOP_REP, E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE, _sender, _receiver,
                _return_code, _return_code_nm, _reason),
            lambda _protocol_message: pdStopRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,
                                           protocol_message: socketIOServer.StopResponse(process,
                                                                                          protocol_rapper,
                                                                                          protocol_message)
            },
            {

            }
        )

        from App.Protocols.Messages.dataClass.pdNotiPackets import pdDownloadingThresholdNoti
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_DOWNLOADING_THRESHOLD_NOTI] = (
            lambda _sender, _receiver,_thresholdType: pdDownloadingThresholdNoti(
                cProtocolMeta.E_PROTOCOL_ID.PD_DOWNLOADING_THRESHOLD_NOTI,E_PROTOCOL_MESSAGE_DIRECTION.NOTI, _sender, _receiver,_thresholdType),
            lambda _protocol_message: pdDownloadingThresholdNoti.from_json(_protocol_message),
            {
                # E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.StopRequest(
                #     process,
                #     protocol_rapper,
                #     protocol_message)
            },
            {

            }
        )



        from App.Protocols.Messages.dataClass.pdCrawlingPacket import pdCrawlingReq , pdCrawlingRep
        ## JOB
        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REQ] = (
            lambda _sender, _receiver, _uri: pdCrawlingReq(
                cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REQ,E_PROTOCOL_MESSAGE_DIRECTION.REQUEST, _sender, _receiver , _uri),
            lambda _protocol_message: pdCrawlingReq.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper, protocol_message: socketIOServer.CrawlingRequest(
                    process,
                    protocol_rapper,
                    protocol_message)
            },
            {

            }
        )

        cProtocolMeta.TABLE[cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REP] = (
            lambda _sender, _receiver, _scode , _return_code_dto: pdCrawlingRep(
                cProtocolMeta.E_PROTOCOL_ID.PD_CRAWLING_REP,E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE, _sender, _receiver,_scode ,_return_code_dto.GetCode() ,_return_code_dto.GetCodeNM() , _return_code_dto.GetReason()),
            lambda _protocol_message: pdStopRep.from_json(_protocol_message),
            {
                E_CATE.REST_SERVER: lambda process, protocol_rapper,
                                           protocol_message: socketIOServer.CrawlingResponse(process,
                                                                                          protocol_rapper,
                                                                                          protocol_message)
            },
            {

            }
        )


        cProtocolMeta.__registerJsonDecoder()

    @staticmethod
    def MakeMessage(_protocol_id: E_PROTOCOL_ID, _sender, _receiver, *_message_args):
        messageObject = cProtocolMeta.GetProtocolFactoryHandler(_protocol_id)(_sender, _receiver, _message_args)
        return cProtocolMeta.GetProtocolPacketMessage(messageObject)

    @staticmethod
    def __registerJsonDecoder():

        print("=========== BEGIN __registerJsonDecoder ============")
        from App.Protocols.Protocol import cProtocolRapper
        cProtocolRapper.ResetDecodeHandler()
        for _protocol_id, _call_back_lists in cProtocolMeta.TABLE.items():
            cProtocolRapper.AppendDecodeHandler(_protocol_id,
                                                _call_back_lists[E_PROTOCOL_META_ELE.JSON_DECODE])
        print("=========== __registerJsonDecoder END ============")

    @staticmethod
    def GetReceiveHandlerContainer():
        retDcit={}
        for _protocol_id, _call_back_lists in cProtocolMeta.TABLE.items():
            retDcit[_protocol_id]=_call_back_lists[E_PROTOCOL_META_ELE.RECEIVE_CALLBACK]

        return retDcit


    @staticmethod
    def GetReceiveHandler(_protocol_id , _receiver ):
        callback_dict= cProtocolMeta.TABLE[_protocol_id][E_PROTOCOL_META_ELE.RECEIVE_CALLBACK]
        return callback_dict[_receiver]

    @staticmethod
    def GetInrGroupReceiveHandler(_protocol_id, _receiver):
        callback_dict = cProtocolMeta.TABLE[_protocol_id][E_PROTOCOL_META_ELE.INR_GROUP_RECEIVE_CALLBACK]
        return callback_dict[_receiver]


    @staticmethod
    def GetProtocolFactoryHandler(_protocol_id):
        return cProtocolMeta.TABLE[_protocol_id][E_PROTOCOL_META_ELE.OBJECT_FACTOR]

    @staticmethod
    def GetJsonDecoder(_protocol_id):
        return cProtocolMeta.TABLE[_protocol_id][E_PROTOCOL_META_ELE.JSON_DECODE]

    # @staticmethod
    # def GetReceiveCallBack(_protocol_id):
    #     return cProtocolMeta.TABLE[_protocol_id][E_PROTOCOL_META_ELE.RECEIVE_CALLBACK]

    @staticmethod
    def GetProtocolPacketMessage(_protocol_message_object):
        from App.Protocols.Protocol import cProtocolRapper
        return cProtocolRapper.GetProtocolRapper(_protocol_message_object).getProtocolPacketMessage()


    @staticmethod
    def GetProtocolOwnerName(_app_name, _process_name=None):
        from App.Protocols.cProtocolOwner import cProtocolName
        return cProtocolName.ProtocolNameFactory(_app_name, _process_name).GetProtocolOwnerName()

def main():

    cProtocolMeta.Init()


    from App.Category.eCateGory import E_CATE
    nm= cProtocolMeta.GetProtocolOwnerName(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)


    #
    # m1=cProtocolMeta.GetProtocolPacketMessage(cc)
    # print(m1)
    #
    # from App.Protocols.Protocol import cProtocolRapper
    # mes= cProtocolRapper.GetProtocolRapper(cc).getProtocolPacketMessage()
    # print(mes)
    #
    pass


def TTT():
    cProtocolMeta.Init()
    from App.Category.eCateGory import E_CATE

    sender = cProtocolMeta.GetProtocolOwnerName(E_CATE.MESSAGE_BRIDGE, E_CATE.E_MESSAGE_BRIDGE.E_COMMON.MESSAGE_BRIDGE)
    receiver = cProtocolMeta.GetProtocolOwnerName(E_CATE.DOWNLOADER,
                                                  E_CATE.E_DOWNLOADER.E_COMMON.DOWNLOAD_MANAGER)


    message = cProtocolMeta.GetProtocolFactoryHandler(cProtocolMeta.E_PROTOCOL_ID.SEEK_REQ)(
        sender, receiver, "20230602000045")

    print(cProtocolMeta.GetProtocolPacketMessage(message))


if __name__ == '__main__':
    TTT()
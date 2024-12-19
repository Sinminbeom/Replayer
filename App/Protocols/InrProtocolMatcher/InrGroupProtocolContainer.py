from App.Protocols.InrProtocolMatcher.IEventQueue import IEventQueue



## class 를 하나 파자....
## qd - ps 용도 저장용도......



class cInrGroupProtocolContainer(IEventQueue):
    def __init__(self):
        self.inr_group_protocol_queue={}
    def Append(self , _inr_protocol_dto_rap, _pair_packet_size):


        self.__upsert( _inr_protocol_dto_rap, _pair_packet_size )

        # event_dto = _protocol_event_dto_rap.GetEventDTO()
        # from App.Protocols.InrProtocolMatcher.cProtocolEventDTOMatcher import cProtocolEventDTOMatcher
        # self.group_queue[_protocol_event_dto_rap.GetEventDTO().GetProtocolGroupID()]=cProtocolEventDTOMatcher(event_dto)
        pass

    ## TODO KK upsert 가 될때마다 패킷을 확인 한다....
    ## 이부분에서 이미 있다면
    ## 초기화 부분을 처리해주자.....
    ## 여기서 GD 가 중복이라면 초기화를 시키자.
    ## 개수 정보확인 할것.....



    def __IsContainQD(self , _protocol_group_id, protocol_dto ):

        if _protocol_group_id not in self.inr_group_protocol_queue:
            return False

        # qd = protocol_dto.GetQD()

        return self.inr_group_protocol_queue[_protocol_group_id].IsContainQD( protocol_dto )


    def __upsert(self, _inr_protocol_dto_rap , _pair_packet_size):
        from App.Protocols.InrProtocolMatcher.InrProtocolContainer import cInrProtocolContainer
        protocol_dto = _inr_protocol_dto_rap.GetProtocolDTO()
        protocol_group_id = protocol_dto.GetProtocolGroupID()

        if self.__IsContainQD( protocol_group_id , protocol_dto ) == True:
            self.inr_group_protocol_queue[protocol_group_id] = None
            del self.inr_group_protocol_queue[protocol_group_id]

        if protocol_group_id in self.inr_group_protocol_queue:
            self.inr_group_protocol_queue[protocol_group_id].Append(protocol_dto)
        else:
            self.inr_group_protocol_queue[protocol_group_id]=cInrProtocolContainer(protocol_dto , _pair_packet_size)

    def toString(self):
        ret=""
        for k , v in self.inr_group_protocol_queue.items():
            ret = ret + f""" K : {k} v : {v.GetPairState()}"""
        return ret

    def GetResponseDTOLists(self , _protocol_group_id):
        return self.inr_group_protocol_queue[_protocol_group_id].GetResponseDTOLists()

    def GetPairState(self , _protocol_group_id):
        return self.inr_group_protocol_queue[_protocol_group_id].GetPairState()











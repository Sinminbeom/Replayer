



class cInrProtocolMatcher:

    class E_PROTOCOL_PACKING_TYPE:
        PERSONAL=0
        BROAD_CAST=1

    def __init__(self):
        # self.event_queue={}
        self.__init()

    def __init(self):
        self.inr_group_protocol_container={}

        from App.Protocols.InrProtocolMatcher.InrGroupProtocolContainer import cInrGroupProtocolContainer

        self.inr_group_protocol_container[cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.PERSONAL]=cInrGroupProtocolContainer()
        self.inr_group_protocol_container[cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.BROAD_CAST]=cInrGroupProtocolContainer()

        pass


    def __getGroupProtocolQueue(self , _protocol_packing_type ):
        return self.inr_group_protocol_container[_protocol_packing_type]

    def __append(self , _protocol_event_dto_rap,_pair_packet_size ):

        groupProtocolQueue = self.__getGroupProtocolQueue(_protocol_event_dto_rap.packing_type)

        groupProtocolQueue.Append(_protocol_event_dto_rap,_pair_packet_size)


        pass

    def appendPersonl(self , _protocol_message ):
        from App.Protocols.Protocol import cProtocolRapper
        protocol_dto = cProtocolRapper.DecodeProtocolEventDTO(_protocol_message)

        from App.Protocols.InrProtocolMatcher.cProtocolDTORap import cProtocolDTORap
        self.__append(cProtocolDTORap(cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.PERSONAL, protocol_dto),1)

        return _protocol_message, protocol_dto

    def appendBroad(self , _protocol_message,_pair_packet_size ):
        from App.Protocols.Protocol import cProtocolRapper
        protocol_dto = cProtocolRapper.DecodeProtocolEventDTO(_protocol_message)

        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        if protocol_dto.GetMessageDirection() == E_PROTOCOL_MESSAGE_DIRECTION.NOTI :
            return None , None

        from App.Protocols.InrProtocolMatcher.cProtocolDTORap import cProtocolDTORap
        self.__append(cProtocolDTORap(cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.BROAD_CAST, protocol_dto),_pair_packet_size)

        return _protocol_message , protocol_dto


        # print(self.toString())


    def GetBroadPairState(self , _protocol_group_id ):
        inrGroupProtocolContainer =self.inr_group_protocol_container[cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.BROAD_CAST]
        return inrGroupProtocolContainer.GetPairState(_protocol_group_id)
    def GetResponseDTOLists(self , _protocol_group_id ):
        inrGroupProtocolContainer =self.inr_group_protocol_container[cInrProtocolMatcher.E_PROTOCOL_PACKING_TYPE.BROAD_CAST]
        return inrGroupProtocolContainer.GetResponseDTOLists(_protocol_group_id)


    def toString(self):

        ret="""RRRRR : """
        for k , v in self.inr_group_protocol_container.items():
            ret = ret + " "  + v.toString()

        return ret

def main():
    from App.Protocols.cProtocolMeta import cProtocolMeta


    inr= cInrProtocolMatcher()

    # from App.Protocols.cProtocolMeta import cProtocolMeta
    # from App.Protocols.cProtocolMeta import cProtocolMeta
    # from App.Protocols import cProtocolMeta
    cProtocolMeta.Init()

    inr.appendBroad(
        """IN|:|202311011434_00000000|:|-1800|:|0|:|WEB_T/WEB_T|:|WEB_T/CRAWLER_X|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingReq", "communication_type": 1, "protocol_id": "-1800", "sender": "WEB_T/WEB_T", "receiver": "WEB_T/CRAWLER_X", "message_direction": 0, "uri": "uri"} """
    )

    inr.appendBroad(
        """IN|:|202311011434_00000001|:|-1800|:|0|:|WEB_T/WEB_T|:|WEB_T/CRAWLER_Y|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingReq", "communication_type": 1, "protocol_id": "-1800", "sender": "WEB_T/WEB_T", "receiver": "WEB_T/CRAWLER_Y", "message_direction": 0, "uri": "uri"} """
    )

    inr.appendBroad(
        """IN|:|202311011434_00000002|:|-1800|:|0|:|WEB_T/WEB_T|:|WEB_T/CRAWLER_Z|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingReq", "communication_type": 1, "protocol_id": "-1800", "sender": "WEB_T/WEB_T", "receiver": "WEB_T/CRAWLER_Z", "message_direction": 0, "uri": "uri"}"""
    )

    # print(inr.toString())

    inr.appendBroad(
    """IN|:|202311011434_00000000|:|-1801|:|1|:|WEB_T/CRAWLER_Z|:|WEB_T/WEB_T|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingRep", "communication_type": 1, "protocol_id": "-1801", "sender": "WEB_T/CRAWLER_Z", "receiver": "WEB_T/WEB_T", "message_direction": 1, "return_code": "100", "return_code_nm": "OK", "return_code_reason": "", "s_code": "_scode"} """
    )

    inr.appendBroad(
    """IN|:|202311011434_00000000|:|-1801|:|1|:|WEB_T/CRAWLER_X|:|WEB_T/WEB_T|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingRep", "communication_type": 1, "protocol_id": "-1801", "sender": "WEB_T/CRAWLER_X", "receiver": "WEB_T/WEB_T", "message_direction": 1, "return_code": "100", "return_code_nm": "OK", "return_code_reason": "", "s_code": "_scode"} """
    )

    inr.appendBroad(
    """IN|:|202311011434_00000000|:|-1801|:|1|:|WEB_T/CRAWLER_Y|:|WEB_T/WEB_T|:|{"py/object": "App.Protocols.Messages.Inner.pInrCrawling.pInrCrawlingRep", "communication_type": 1, "protocol_id": "-1801", "sender": "WEB_T/CRAWLER_Y", "receiver": "WEB_T/WEB_T", "message_direction": 1, "return_code": "100", "return_code_nm": "OK", "return_code_reason": "", "s_code": "_scode"} """
    )

    print(inr.toString())

    pass


if __name__ == '__main__':
    main()
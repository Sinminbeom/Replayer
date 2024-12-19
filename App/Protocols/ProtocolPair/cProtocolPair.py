
class cProtocolPairMatcher:
    def __init__(self ):

        self.req_dto=None
        self.rep_dto = None
        self.protocol_group_id=None

        # self.SetDto(_pair_dto)

        pass
    def SetDto(self , _pair_dto ):

        ## req 오면 none 됨
        from App.Protocols.cMessage import E_PROTOCOL_MESSAGE_DIRECTION
        if _pair_dto.message_direction == E_PROTOCOL_MESSAGE_DIRECTION.REQUEST:
            self.req_dto=_pair_dto
            self.rep_dto =None
            self.protocol_group_id = _pair_dto.protocol_group_id

            return cProtocolPair.E_PAIR_STATE.WAIT

        elif _pair_dto.message_direction == E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
            brep=self.rep_dto
            self.rep_dto = _pair_dto

            if brep == None:
                return cProtocolPair.E_PAIR_STATE.COMPLEATE_IMMEDIATELY

            return cProtocolPair.E_PAIR_STATE.COMPLEATED

        # if _pair_dto.message_direction == E_PROTOCOL_MESSAGE_DIRECTION.REQUEST or _pair_dto.message_direction == E_PROTOCOL_MESSAGE_DIRECTION.RESPONSE:
        #     self.protocol_group_id = _pair_dto.protocol_group_id
    # def IsMatching(self):
    #     if self.rep_dto != None and self.rep_dto != None:
    #         return True
    #
    #     return False

class cProtocolPairContainer:
    def __init__(self):
        self.list={}
        pass
    def Pair(self,_pairdto):
        if _pairdto.protocol_group_id in self.list:
            matcher= self.list.get(_pairdto.protocol_group_id)
            return matcher.SetDto(_pairdto)
        else:
            # self.list[_pairdto.protocol_group_id]=cProtocolPairMatcher(_pairdto)
            matcher = cProtocolPairMatcher()
            self.list[_pairdto.protocol_group_id]=matcher
            return matcher.SetDto(_pairdto)

class cProtocolPair:

    class E_PAIR_STATE:
        WAIT=0
        COMPLEATE_IMMEDIATELY=1
        COMPLEATED = 2
    def __init__(self):
        self.container=cProtocolPairContainer()
        pass

    def Pair(self,_protocol_message):
        from App.Protocols.Protocol import cProtocolRapper
        pairdto = cProtocolRapper.DecodeProtocolPairDTO(_protocol_message)
        return self.container.Pair(pairdto)

    def IsIgnorePair(self ,_protocol_message ):
        results = self.Pair(_protocol_message)
        if results == cProtocolPair.E_PAIR_STATE.COMPLEATED:
            return True

        return False

class cAAA:
    def __init__(self):
        pass

def main():

    a=cAAA()

    b=None

    c=b


    b=a




    pass



if __name__ == '__main__':
    main()










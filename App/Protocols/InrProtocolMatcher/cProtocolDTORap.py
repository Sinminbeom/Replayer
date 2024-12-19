from App.Common.cDto import IDTO


class cProtocolDTORap(IDTO):

    def __init__(self , _e_packing_type , _protocol_dto ):
        super().__init__()
        self.packing_type=_e_packing_type
        self.protocol_dto=_protocol_dto
        pass

    def GetProtocolDTO(self):
        return self.protocol_dto

    def GetPackingType(self):
        return self.packing_type




from App.Common.cDto import IDTO
from App.cDefine import IENUM

class cProtocolCodeMeta:


    class E_CODE(IENUM):
        OK="100"
        UNKNOW="-100"
        ERROR="-200"
        INVALID_REQUEST="-300"
        ILLEGAL_ARGUMENT_EXCEPTION="-400"


        class E_ELE(IENUM):
            CODE=0
            NM=1
            pass


        TABLE={
            OK:[OK , "OK"],
            UNKNOW: [UNKNOW, "UNKNOW"],
            ERROR: [ERROR, "ERROR"],
            INVALID_REQUEST: [INVALID_REQUEST, "INVALID_REQUEST"],
            ILLEGAL_ARGUMENT_EXCEPTION: [ILLEGAL_ARGUMENT_EXCEPTION, "ILLEGAL_ARGUMENT_EXCEPTION"]
        }

    @staticmethod
    def GetCodeNM( _code):

        a=cProtocolCodeMeta.E_CODE.TABLE[_code][cProtocolCodeMeta.E_CODE.E_ELE.NM]

        return a

        # return  __TABLE[_code][cProtocolCodeMeta.E_CODE.E_ELE.NM]
        #
        # pass



def main():
    d=cProtocolCodeMeta.GetCodeNM(cProtocolCodeMeta.E_CODE.ERROR)

    o=10
    o=100
    pass

if __name__ == '__main__':
    main()


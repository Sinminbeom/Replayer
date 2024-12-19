from App.Common.Properties.cIMDGConfig import cIMDGConfig
from App.Common.Properties.cRestConfig import cRestConfig


class IENUM:

    pass

class E_RUN_MODE(IENUM):
    DEBUG   = 0
    RELEASE = 1
    TEST    = 2
    class E_COLUMN(IENUM):
        NM = 0
        SYMBOL = 1

    META={
        DEBUG:{E_COLUMN.NM:"DEBUG"     , E_COLUMN.SYMBOL:"D"},
        RELEASE:{E_COLUMN.NM:"RELEASE" , E_COLUMN.SYMBOL:"R"},
        TEST:{E_COLUMN.NM:"TEST" , E_COLUMN.SYMBOL:"T"}
    }

    @staticmethod
    def getSymbol(_e_run_mode):
        return E_RUN_MODE.META[_e_run_mode][E_RUN_MODE.E_COLUMN.SYMBOL]

    @staticmethod
    def getNM(_e_run_mode):
        return E_RUN_MODE.META[_e_run_mode][E_RUN_MODE.E_COLUMN.NM]


class Def:

    PROJECT_NM = "PROJECT_P1"
    REDIS_CHANNEL_PRIVATE_MAIN="PRIVATE_MAIN"
    # REDIS_CHANNEL_PUBLIC_REST = "PUBLIC_REST"

    THREAD_NAME_EVENT_BUS="EVENT_BUS"
    CHANNEL_NM_IMDG="CHANNEL_IMDG"

    RUN_MODE=E_RUN_MODE.DEBUG
    @staticmethod
    def getIMDGChannelNM():
        return Def.DefRedis.getRedisKeyNM(Def.CHANNEL_NM_IMDG , Def.GetRunMode() )

    @staticmethod
    def GetRunMode():
        return Def.RUN_MODE

    @staticmethod
    def SetRunMode(_run_mode):
        Def.RUN_MODE=_run_mode


    class DefRedis:
        config = cIMDGConfig()

        IP = config.GetConfig("SERVER_IP")
        PORT = int(config.GetConfig("SERVER_PORT"))
        POOL_SIZE = int(config.GetConfig("POOL_SIZE"))
        SCHEMA_NM = config.GetConfig("SCHEMA_NM")

        KEY_SEQUENCE_MINUTE="SEQUENCE_MINUTE"

        @staticmethod
        def getRedisPoolSize():
            return Def.DefRedis.POOL_SIZE
        @staticmethod
        def getRedisKeyNM(_key_nm , _e_run_mode):
            sym=E_RUN_MODE.getSymbol( _e_run_mode )
            return f"{sym}:{Def.DefRedis.SCHEMA_NM}:{Def.PROJECT_NM}:{_key_nm}".upper()

    class RestServer:
        config = cRestConfig()
        BIND_IP = config.GetConfig("BIND_IP")
        BIND_PORT = int(config.GetConfig("BIND_PORT"))

        @staticmethod
        def getBindIP():
            return Def.RestServer.BIND_IP

        @staticmethod
        def getBindPort():
            return Def.RestServer.BIND_PORT





class E_COMMUNICATION_TYPE(IENUM):
    IMDG=0
    PROCESS=1
    NORMAL=2

    class E_COLUMN(IENUM):
        NM = 0
        SYMBOL = 1

    META = {
        IMDG: {E_COLUMN.NM: "IMDG", E_COLUMN.SYMBOL: "DG"},
        PROCESS: {E_COLUMN.NM: "PROCESS", E_COLUMN.SYMBOL: "IN"},
        NORMAL: {E_COLUMN.NM: "NORMAL", E_COLUMN.SYMBOL: "NO"}
    }

    @staticmethod
    def getSymbol(_e_communication_type):
        return E_COMMUNICATION_TYPE.META[_e_communication_type][E_COMMUNICATION_TYPE.E_COLUMN.SYMBOL]

    @staticmethod
    def getNM(_e_communication_type):
        return E_COMMUNICATION_TYPE.META[_e_communication_type][E_COMMUNICATION_TYPE.E_COLUMN.NM]

    @staticmethod
    def getSymbolToE_Type(_symbol_string):

        for communication_type , metadata in E_COMMUNICATION_TYPE.META.items():
            if metadata[E_COMMUNICATION_TYPE.E_COLUMN.SYMBOL] == _symbol_string:
                return communication_type

        return None


class E_COMMAND(IENUM):
    PLAY="PLAY"
    STOP="STOP"
    PAUSE="PAUSE"


#
# def main():
#     print(Def.DefRedis.IP)
#     print(Def.DefRedis.PORT)
#     print(E_RUN_MODE.getSymbol(E_RUN_MODE.RELEASE))
#     print(E_RUN_MODE.getNM(E_RUN_MODE.RELEASE))
#     print(Def.DefRedis.getRedisKeyNM("list1", E_RUN_MODE.RELEASE))
#
#     print( E_COMMUNICATION_TYPE.getSymbol(E_COMMUNICATION_TYPE.IMDG) )
#     print( E_COMMUNICATION_TYPE.getSymbol(E_COMMUNICATION_TYPE.PROCESS) )
#
#
#     print("================")
#     a=E_COMMUNICATION_TYPE.getSymbolToE_Type("IN")
#     print(a)
#     print("================")
#
# if __name__ == '__main__':
#     main()
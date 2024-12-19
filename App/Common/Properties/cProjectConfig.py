from LibUtils.ConfigUtils import ConfigUtils
from LibUtils.SingletonInstane import SingletonInstane

CONFIG_PATH = "config/application.conf"
# CONFIG_PATH = "C:\\D\\project2\\infra-glue-conditions-replayer\\config\\application.conf"




class cProjectConfig(SingletonInstane):
    DELIM_CHAR = "|"

    def __init__(self):
        super().__init__()
        self.config = self.__preTreatment()

    def Init(self):
        pass

    def __preTreatment(self):
        config = ConfigUtils.configParser(configFile=CONFIG_PATH)
        tmpConfig = dict()
        for key, value in config.items():
            tmp = value
            if value[0] == "[": tmp = tmp[1:]
            if value[-1] == "]" : tmp = tmp[0:-1]

            value = list(s.strip() for s in tmp.split(cProjectConfig.DELIM_CHAR))

            if len(value) == 1:
                tmpConfig[key] = value[0]
            else:
                tmpConfig[key] = value

        return tmpConfig


    def GetConfig(self, _title1=None, _title2=None) -> dict:
        if _title1 is None:
            return self.config
        elif _title1 is not None and _title2 is None:
            return self.__getConfigFromTitle(_title1)
        elif _title1 is not None and _title2 is not None:
            return self.GetValue(_title1, _title2)

    def __getConfigFromTitle(self, _title) -> dict:
        newConfig = dict()
        for k, v in self.config.items():
            if k[0] == _title or k[0] == "COMMON":
                newConfig[k[1]] = v


        return newConfig

    def GetValue(self, _title1, _title2):
        return self.GetConfig(_title1)[_title2.lower()]



if __name__ == '__main__':
    config = cProjectConfig().instance()

    print(config.GetConfig())
    print(config.GetConfig("STREAMER"))
    print(config.GetConfig("STREAMER", "AT128_ROOF_RIGHT"))
    print(config.GetConfig("DOWNLOADER"))
    print(config.GetConfig("DOWNLOADER", "BUFFERING_TIME"))
    # print(config.GetValue("STREAMER", "AT128_ROOF_FRONT"))

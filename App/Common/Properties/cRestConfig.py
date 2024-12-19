from App.Common.Properties.cIMDGConfig import cIMDGConfig
from App.Common.Properties.cProjectConfig import cProjectConfig


class cRestConfig:
    ALIAS = "REST"

    def __init__(self):
        self.config = cProjectConfig.instance()

    def GetConfig(self, _title=None):
        if _title is None:
            return self.config.GetConfig(cRestConfig.ALIAS)
        return self.config.GetConfig(cRestConfig.ALIAS, _title.lower())



if __name__ == '__main__':
    con = cIMDGConfig()
    print(con.GetConfig("save_path"))
    print(con.GetConfig("DOWNLOAD_RATIO"))


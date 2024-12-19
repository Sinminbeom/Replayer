
class cProtocolName:
    DELIM="""/"""

    def __int__(self):
        self.AppName=None
        self.ProcessName=None
        pass

    def SetName (self , _app_name , _process_name=None):
        self.AppName=_app_name

        # if _process_name == None:
        #     return

        self.ProcessName=_process_name

    def SetNameByProtocolName(self , _protocol_names_string):
        if cProtocolName.DELIM in _protocol_names_string:
            s=_protocol_names_string.split(cProtocolName.DELIM)
            self.AppName= s[0]
            self.ProcessName= s[1]
        else:
            self.AppName = _protocol_names_string
            self.ProcessName=None

    def GetProtocolOwnerName(self):

        from LibUtils.StringBuilder import StringBuilder
        sb=StringBuilder()

        sb.Append(self.AppName)

        if self.ProcessName != None:
            sb.Append(cProtocolName.DELIM).Append(self.ProcessName)

        return sb.ToString()

    def GetAppName(self):
        return self.AppName

    def GetProcessName(self):
        return self.ProcessName

    def IsOwner(self,_app_name,_process_name):

        if self.ProcessName==None:
            if self.AppName == _app_name:
                return True
        else:
            if self.AppName == _app_name and self.ProcessName == _process_name:
                return True

        return False

    @staticmethod
    def ProtocolNameFactory(_app_name,_process_name=None):
        pn= cProtocolName()
        pn.SetName(_app_name,_process_name)
        return pn


def main():
    from App.Category.eCateGory import E_CATE
    print(E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)

    a=cProtocolName.ProtocolNameFactory(E_CATE.DOWNLOADER, E_CATE.E_DOWNLOADER.E_LIDAR.AT128_ROOF_FRONT)

    print(a.GetProtocolOwnerName())
    # pn= cProtocolName()
    # pn.SetName("App","Process")
    # print(pn.GetProtocolName())
    #
    # pn2 = cProtocolName()
    # pn2.SetNameByProtocolName("App/LL")
    # print(pn2.GetProtocolName())
    #
    # print(pn2.GetAppName())
    # print(pn2.GetProcessName())






    pass


if __name__ == '__main__':
    main()





class cQdPsHash():

    def __init__(self , _qd , _ps , _sy ):

        self.qd=_qd
        self.ps=_ps
        self.sy = _sy

    def GetHashKey(self):
        from LibUtils.StringBuilder import StringBuilder
        sb = StringBuilder()
        sb.Append(self.qd).Append("""|^|""").Append(self.ps)
        return sb.ToString()

    def toString(self):
        from LibUtils.StringBuilder import StringBuilder
        sb = StringBuilder()
        sb.Append(self.qd).Append("""|^|""").Append(self.ps)
        return sb.ToString()



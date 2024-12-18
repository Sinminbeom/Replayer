

class CollectionUtils:

    @staticmethod
    def DictExtends(_dict,_key,_lambda):

        if _key in _dict:
            return _dict[_key]
        else:
            _dict[_key]=_lambda()
            return _dict[_key]

    @staticmethod
    def DictIsContainKey(_dict,_key):

        if _dict==None:
            return False

        if _key in _dict:
            return True

        return False


    @staticmethod
    def DictGetValue(_dict, _key):

        if _dict==None:
            return None

        if _key in _dict:
            return _dict[_key]
        else:
            return None


def main():

    dic={}

    ddic=CollectionUtils.DictExtends(dic,"k1",lambda : {})

    o=10
    o=100

    dddic=CollectionUtils.DictExtends(ddic, "k1k1", lambda: [])

    dddic.append(10)
    dddic.append(20)
    dddic.append(30)
    dddic.append(40)

    o = 10
    o = 100

    dddic2=CollectionUtils.DictExtends(ddic, "k1k2", lambda: [])

    dddic2.append(10)
    dddic2.append(20)
    dddic2.append(30)
    dddic2.append(40)

    o = 10
    o = 100

    ddic =CollectionUtils.DictExtends(dic, "k2", lambda: {})
    dddic=CollectionUtils.DictExtends(ddic, "k2k1", lambda: [])

    dddic.append(10)
    dddic.append(20)
    dddic.append(30)
    dddic.append(40)

    o = 10
    o = 100

    dddic2=CollectionUtils.DictExtends(ddic, "k2k2", lambda: [])

    dddic2.append(10)
    dddic2.append(20)
    dddic2.append(30)
    dddic2.append(40)

    o = 10
    o = 100
    pass


if __name__ == '__main__':
    main()


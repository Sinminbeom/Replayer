from typing import List


class cMessageReceiver:

    def __init__(self, _receiver , *_message):

        self.receiver=_receiver
        self.message=_message

    def GetMessage(self):
        return self.message

    def GetReceiver(self):
        return self.receiver

    def toString(self):

        ret=f""" k : {self.receiver} , v {self.message} """

        return ret
        pass

class cMessageReceiverContainer:

    def __init__(self):

        self.queue=[]

        pass

    def __Append(self , _receiver , *_message ):
        self.queue.append(cMessageReceiver(_receiver , *_message)  )
        return self

    def GetQueue(self):
        return self.queue

    @staticmethod
    def Factory():
        return cMessageReceiverContainer()


    ####### USAGE #######
    # AppendReceiverIds(Recevier LIst = "a" , *_message: Once)
    # AppendReceiverIds(Recevier LIst = "b" )
    # If you enter a message with the receiver, the message is added,
    # and if you enter only the receiver, the message is the same.
    def Append(self , _receiver , *_message ):

        if len(_message) != 0:
            self.__Append(_receiver,*_message)
            return self

        if len(self.queue) < 1:
            self.__Append(_receiver, *_message)
            return self


        self.__ExtentsReceiver( _receiver )
        return self

    ####### USAGE #######
    # AppendReceiverIds(Recevier LIst = [ "a", "b", "c"] , *_message: Once)
    # All elements of the entered list have one message.
    def AppendReceiverIds(self, _receiverIds: List, *_message):
        for i in range(len(_receiverIds)):
            if i == 0:
                self.Append(_receiverIds[i], *_message)
                continue
            self.Append(_receiverIds[i])

        return self

    def __ExtentsReceiver(self, _receiver):

        if len(self.queue) < 1 :
            raise Exception( "cMessageReceiverContainer::ExtentsReceiver Extents Error ! ")

        messageReceiver = self.queue[0]
        message= messageReceiver.GetMessage()

        self.__Append(_receiver, *message)

        return self

    def Clear(self):

        self.queue.clear()
        pass


    def toString(self):


        for mr in self.queue:

            print(mr.toString())

        pass


def main():
    cc=cMessageReceiverContainer()


    cc.Append("a" , "a" , 10).\
        Append("b" , "a" , 10)
    cc.toString()
    cc.Clear()

    cc.Append("a" , "a" , 10)\
        .Append("b")\
        .Append("C")

    cc.toString()





    pass

if __name__ == '__main__':
    main()
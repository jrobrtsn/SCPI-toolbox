# defaults



class SerialSettings():
    def __init__(self):
        # serial configs ho here. should be self explaintry

        self.BaudRate = 9600 # baud rate. obvious
        self.Timeout = 2 #time, in seconds for how long to wait for command to be sent or received before its aborted

serial = SerialSettings()



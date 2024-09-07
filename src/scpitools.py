# SCPI_INTERPERATATION_UTILITY

import serial
import sqlite3


class device(serial.Serial):
    def __init__(self, device_name, device_ID, device_type, device_limitations, TIMEOUT, BAUD):

        self.name = device_name # SET BY USER, typically manufacturer and model number
        self.ID = device_ID # unique ID assigned by program so avoid conflicts
        self.type = device_type # types are: `POWER_SUPPLY` = PSU `OSCILLOSCOPE` = DSO `MULTIMETER` = DMM `SOLDERING_IRON` = C_s `CUSTOM_SELECTION` = C_x ETC.. 
        self.limits = device_limitations # what commands are known to be defective, list
        self.write_timeout = TIMEOUT # time limit for serial data transfer (write)
        self.timeout = TIMEOUT # time limit for serial data transfer (read)
        self.baudrate = BAUD 
    

    def connect(self, PORT):
        self.port = PORT
        try:
            self.open()
        except serial.SerialException:
            #port is busy or non existent
            return 1
            #TODO make redundancy loop where input is asked for again from user with error info
            # "connection failed. port busy or disconnected"

    
    def disconnect(self):
        self.close()
    

    

#================== device-unique functions ==========================

class DMM(device):
    def __init__(self):
         pass 
    
    def SetRange(self, range):
        
        self.command = ("something" + range + "something else\r\n")
        self.write(self.command)
        self. range = (self.readline().decode())[1,1]  ] #TODO: put the right things here for it to work





class DSO(device):
    def __init__(self):
        pass
    

    def SetTimebase(self, timebase):
        self.command = ("something" + timebase + "something else\r\n")
        self.write(self.command)
        




class PSU(device):
    def __init__(self):
        pass
    

    def SetVoltage(self, voltage):
        self.command = ("something" + voltage + "something else\r\n")
        self.write(self.command)









# SCPI_INTERPERATATION_UTILITY


import serial
import sqlite3




class WrongModeError(Exception):
    def __init__(self, message):
        self.message = message

class SettingError(Exception):
    def __init__(self):
        self.message = "could not set mode, function, or setting on device. device has returnrd an error. see error log database [not implemented yet]"

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
    
    def SendCommand(self):
        self.write(self.command)
        self.flush()


    

#================== device-unique functions ==========================

class DMM(device):
    def __init__(self):
         pass 
    
    def SetVoltageRange(self, aRange):
        
        if self.mode != "VOLTAGE_READ":
            raise WrongModeError()
        self.command = ("something" + aRange[0] + "something else\r\n")
        self.write(self.command)
        self.SendCommand() #TODO: put the right things here for it to work

    
    def SetResistanceRange(self, aRange):
        
        self.command = ("something" + aRange[0] + "something else\r\n")
        self.write(self.command)
        self.SendCommand() #TODO: put the right things here for it to work

    def SetCurrentRange(self, aRange):
        
        self.command = ("something" + aRange[0] + "something else\r\n")
        self.write(self.command)
        self.SendCommand() #TODO: put the right things here for it to work

    def SetACVoltageRange(self, aRange):
        
        self.command = ("something" + aRange[0] + "something else\r\n")
        self.write(self.command)
        self.SendCommand() #TODO: put the right things here for it to work
    
    def SetACCurrentRange(self, aRange):
        
        self.command = ("something" + aRange[0] + "something else\r\n")
        self.write(self.command)
        self.SendCommand() #TODO: put the right things here for it to work



    def AutoRange(self):
        self.command = ("something")
        self.SendCommand()


    





class DSO(device):
    def __init__(self):
        pass
    

    def SetTimebase(self, timebase):
        self.command = ("something" + timebase + "something else\r\n")
        self.SendCommand()
        




class PSU(device):
    def __init__(self):
        self.current = 0
        self.voltage = 0
        self.LiveCurrent = 0
        self.LiveVoltage = 0

    
    # i think this is basically all the commands needed for power supplies. 


    def SetVoltage(self, voltage):
        self.command = ("something" + voltage + "something else\r\n")
        self.SendCommand()

    def SetCurrentLim(self, current):
        self.command = ("something" + current + "something else\r\n")
        self.SendCommand()
        
    def SetMaxVoltage(self, voltage):
        self.command = ("something" + voltage + "something else\r\n")
        self.SendCommand()
    
    def SetMaxCurrentLim(self, current):
        self.command = ("something" + current + "something else\r\n")
        self.SendCommand()

    def ReadLiveCurrent(self):
        self.command = ("command for reading current")
        self.SendCommand()
        self.current = self.read()
    
        









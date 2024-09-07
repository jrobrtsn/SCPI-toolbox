# SCPI_INTERPERATATION_UTILITY

import serial
import sqlite3



class device(serial.Serial):
    def __init__(self, device_name, device_ID, device_type, device_limitations, TIMEOUT, BAUD):

        self.name = device_name # SET BY USER, typically manufacturer and model number
        self.ID = device_ID # unique ID assigned by program so avoid conflicts
        self.type = device_type # types are: `POWER_SUPPLY` = PSU `OSCILLOSCOPE` = DSO `MULTIMETER` = DMM `SOLDERING_IRON` = C_s `CUSTOM_SELECTION` = C_x ETC.. 
        self.limits = device_limitations # what commands are known to be defective, list
        self.write_timeout = TIMEOUT # dwell time for serial data transfer (write)
        self.timeout = TIMEOUT # dwell time for serial data transfer (read)
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
    

    def Functions(self):
        # generic functions for all scpi deviced go here. 

    

#================== device-unique functions ==========================

#TODO
# add all scpi commands as onject methods 
# i.e. some set voltage would be object.Functions.Setvoltage(volts)
#   amd would send relevant scpi command via serial 
        if self.type == "DSO":
            # oscilloscope-specific functions
            print("testing")



        if self.type == "DMM":
            # multimeter-specific functions
            print("testing")



        if self.type == "PSU":
            # power supply-specific functions
            print("testing")



        if self.type == "C_":
            # custom defined device. needs more work 
            raise TypeError("custom devices not supported")
        











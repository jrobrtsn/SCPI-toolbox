# SCPI_INTERPERATATION_UTILITY

import serial
import sqlite3



class device(serial.Serial):
    def __init__(self, device_name, device_ID, device_type, device_limitations, TIMEOUT, BAUD):

        self.name = device_name # SET BY USER, typically manufacturer and model number
        self.ID = device_ID # unique ID assigned by program so avoid conflicts
        self.type = device_type # types are: `POWER_SUPPLY` `OSCILLOSCOPE` `MULTIMETER` `SOLDERING_IRON` `CUSTOM_SELECTION` ETC.. 
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
        









class SCPI_commandmaker():


    def set_voltage(volts):
        pass()

    def set_ovr_volt(volts):
        pass()

    def set_current(amps):


        pass()

    def ser_ovr_current(amps):
        pass()



def connect_device():
    # takes a serial port and a known device name. 



def commandReader():







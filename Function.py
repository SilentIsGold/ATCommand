import time
import sys
import glob
from datetime import datetime
from Serial import Serialport
from Command import Command 
from Serial import Serialport


count =0

class Function():
    def __init__(self):
        """
        """
        self.commandserial = Serialport()
        self.GPSserial = Serialport()
        self.modem = Command()
        

    
    def SetLogConfig(self):
        """
        """
        return 
    
    def GetLogConfig(self):
        """
        """

    def SetAutoSendConfig(self):
        """Return available modem command
        """
        with open(self.ModemConfList[self.ChooseModem]) as f:
            CommandList = f.read().splitlines()
        return CommandList
        
    def GetAutoSendConfig(self):
        pass
        
    def SetSerialPort(self,port):
        self.commandserial.SetSerialPort(port)
        pass
        
    def GetSerialPort(self):
        return self.commandserial.GetSerialPortList()
        pass
        
    def SetGPSConfig(self):
        pass
        
    def GetGPSConfig(self):
        pass
        
    def SetUploadConfig(self):
        pass
        
    def GetUploadConfig(self):
        pass
       
       
       

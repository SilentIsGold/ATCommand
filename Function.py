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
        """Write info into LogConfig
        """
        return 
    
    def GetLogConfig(self):
        """Read info from LogConfig
        """

    def SetAutoSendConfig(self):
        """Write info into AutoSendConfig
        """
        with open(self.ModemConfList[self.ChooseModem]) as f:
            CommandList = f.read().splitlines()
        return CommandList
        
    def GetAutoSendConfig(self):
        """Read info from AutoSendConfig
        """
        pass
        
    def SetSerialPort(self,port):
        """Set CommandSerial
        """
        self.commandserial.SetSerialPort(port)
        pass
        
    def GetSerialPort(self):
        """Get Command serial list
        """
        return self.commandserial.GetSerialPortList()
        pass
        
    def SetGPSConfig(self):
        """Write info into GPSConfig
        """
        pass
        
    def GetGPSConfig(self):
        """Read info from GPSConfig
        """
        pass
        
    def SetUploadConfig(self):
        """Write info into UploadConfig
        """
        pass
        
    def GetUploadConfig(self):
        """Read info from UploadConfig
        """
        pass
       
       
       

import time
import sys
import glob
import thread
from datetime import datetime
from Serial import Serialport
from Modem import ModemCommand 
from Serial import Serialport
from GPS import GPSCommand
from  Tkinter import *

count =0

class Function():
    def __init__(self):
        """
        """
        self.commandserial = Serialport()
        self.GPSserial = Serialport()
        self.modem = ModemCommand()
        self.gps = GPSCommand()
        self.AutoSendStop=False
        self.AutoSendTimeInterval=1 #second

    def SetScrollText(self,frame):
        self.txt=frame


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
        pass
        
    def GetAutoSendConfig(self):
        """Read info from AutoSendConfig
        """
        #self.modem.GetModemCommandList
        CommandList=[1,2,3,4,5,6,7]
        print "function ",self.AutoSendTimeInterval
        return self.AutoSendTimeInterval*1000, CommandList
        pass
        
    def SetModemSerialPort(self,port):
        """Set ModemSerial
        """
        self.commandserial.SetSerialPort(port)
        pass
    
    def SetModemConfig(self):
        pass
    def GetModemConfig(self):
        
        pass
    
    def GetModemSerialPort(self):
        """Get Modem serial list
        """
        return self.commandserial.GetSerialPortList()
        pass
    
    def GetSerialPort(self):
        """Get  serial list
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
       
    def SetUserInPut(self,mess):
        """Send the input to the serial port
        """
        output = self.commandserial.SendSerialCommand(mess)
        
        self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
        self.txt.yview(END)
        #return "UserInput:"+mess+"\nOutput:"+output+"\r\n"

    def AutoSendThread(self):
        while not self.AutoSendStop:
            output = self.commandserial.SendSerialCommand(mess)
        
            self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
            self.txt.yview(END)
            time.sleep(self.AutoSendTimeInterval)   
            pass

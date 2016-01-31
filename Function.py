import time
import sys
import glob
import thread
from datetime import datetime
from Serial import Serialport
from Modem import ModemCommand 
from Serial import Serialport
from GPS import GPSCommand
from datetime import datetime
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
        
        self.GPSLogState = False
        self.GPSLogFile = None
        
        self.ModemLogState=False
        self.ModemLogFile=None
        
        self.AutoSendStop=False
        self.AutoSendTimeInterval=1 #second
        self.ModemCommandList=[]

    def SetModemLog(self,state):
        """log the modem and the gps same time
        """
        if state ==1 :
            self.ModemLogState = True
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            modem = self.modem.GetModemName()
            self.ModemLogFile = open(".//Log//"+myUTCtime+"-"+modem,"w")
            if self.GPSLogState:
                self.GPSLogFile = open(".//Log//"+myUTCtime+"-GPS","w")
        else:
            self.ModemLogState = False
            if self.ModemLogFile != None :
                self.ModemLogFile.close()
                self.ModemLogFile = None
                print "Close Modem Log file"
        print self.ModemLogState
    def SetScrollText(self,frame):
        self.txt=frame

    def SetGPSLog(self,state):
        """only set the GPS state and close the file
        """
        if state ==1 :
            self.GPSLogState = True
        else:
            self.GPSLogState = False
            if self.GPSLogFile != None :
                self.GPSLogFile.close()
                self.GPSLogFile = None
                print "Close GPS Log file"
        print self.GPSLogState

    def SetLogConfig(self):
        #TODO
        """Write info into LogConfig
        """
        return 
    
    def GetLogConfig(self):
        #TODO
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
        return self.AutoSendTimeInterval*1000, self.ModemCommandList
        pass
        
    def SetModemSerialPort(self,port):
        """Set ModemSerial
        """
        self.commandserial.SetSerialPort(port)
        pass
    
    def SetGPSSerialPort(self,port):
        """Set the GPS serial port
        """
        self.GPSserial.SetSerialPort(port)
    
    def SetModemConfig(self):
        pass
    def GetModemConfig(self):
        
        pass
    
    def GetModemList(self):
        """return the supporeted modem list
        """
        return self.modem.GetModemList()
        
    def SetModem(self,modem):
        """Set which modem will be use
        """
        self.ModemCommandList[:]=[]
        self.ModemCommandList=self.modem.SetChooseModem(modem)
        
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
        
        if self.ModemLogFile != None:
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            self.ModemLogFile,write(myUTCtime+":"+output+"\r\n")
        
        #return "UserInput:"+mess+"\nOutput:"+output+"\r\n"

    def AutoSendThread(self):
        while not self.AutoSendStop:
            output = self.commandserial.SendSerialCommand(mess)
                    
            self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
            self.txt.yview(END)
            if self.ModemLogFile != None:
                myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
                self.ModemLogFile,write(myUTCtime+":"+output+"\r\n")
            time.sleep(self.AutoSendTimeInterval)   
            pass

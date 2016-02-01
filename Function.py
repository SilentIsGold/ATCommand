import time
import sys
import glob
import threading
import ftplib,os
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
        self.GPSThread=None
        
        self.ModemLogState=False
        self.ModemLogFile=None
        self.ModemThread=None
        
        self.AutoSendState=None
        self.AutoCommandList={}

        self.AutoSendTimeInterval=1 #second
        self.ModemCommandList=[]
        
        self.UploadConfigList={}
        self.UploadFileList={}
        
        

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
                print "start gps thread"
                self.GPSThread=threading.Thread(target=self.GPSLogThread)
                self.GPSThread.start()
        else:
            self.ModemLogState = False
            if self.ModemLogFile != None :

                self.ModemLogFile.close()
                self.ModemLogFile = None

                print "Close Modem Log file"
        print self.ModemLogState
    def SetScrollText(self,frame):
        self.txt=frame

    def SetAutoSendState(self, state):
        """Set AutoSendState
        """
        if state == 1:
            self.AutoSendState =True
            if len(self.AutoCommandList.keys() )==0:
                raise EnvironmentError('No command choosen')
            print self.AutoCommandList.keys()
            self.AutoThread=threading.Thread(target=self.AutoSendThread)
            self.AutoThread.start()
            
        else:
            self.AutoSendState =False
            self.AutoCommandList.clear()
        
        
        
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
        print "function ",self.ModemCommandList
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
        print "SetModem"
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
        self.UploadConfigList.clear()
        file = open('.//Setting//Upload.conf','r')
        
        for line in file.read().splitlines():
            content = line.split(':')
            self.UploadConfigList[content[0]] = content[1]
            #print line
        return self.UploadConfigList
        
        pass
    
    def GetUploadFileList(self):
        """Get the available upload file list
        """
        filelist = []
        for file in os.listdir('.//Log'):
            if not ( file.endswith('GPS') or file.endswith('-Uploaded') ):
                filelist.append(file)
                #print file
        return filelist
        pass
    
    def UploadFile(self):
        """upload the file to the server
        """
        UploadConfig = self.GetUploadConfig()
        
        #session = ftplib.FTP(UploadConfig['Server IP'],UploadConfig['Server ID'],UploadConfig['Server PW'])
        ftp = ftplip.FTP()
        ftp.connect(UploadConfig['Server IP'], port)
        print ftp.getwelcome()
        try:
            print "Logging in..."
            ftp.login("login", "password")
        except:
            "failed to login"
        for filename in self.UploadFileList.keys():
            
            file = open('.//Log//'+filename,'rb')                  # file to send
            session.storbinary(filename, file)     # send the file
            file.close()                                    # close file and FTP
            session.quit()
    
    def SetUploadFile(self,command,state):
        """set which file will be uploaded
        """
        if command in self.UploadFileList:
            if state == 0:
                del self.UploadFileList[command]
        else:
            if state ==1:
                self.UploadFileList[command]=state
        print self.UploadFileList
    
    def SetAutoSendCommand(self,command,state):
        """Set which command will be auto 
        """
        if command in self.AutoCommandList:
            if state == 0:
                del self.AutoCommandList[command]
        else:
            if state ==1:
                self.AutoCommandList[command]=state
        print self.AutoCommandList
        
   
    def SetUserInPut(self,mess):
        """Send the input to the serial port
        """
        output = self.commandserial.SendSerialCommand(mess)
        
        self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
        self.txt.yview(END)
        
        if self.ModemLogFile != None:
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            self.ModemLogFile.write(myUTCtime+":"+output+"\r\n")
        
        #return "UserInput:"+mess+"\nOutput:"+output+"\r\n"

    def GPSLogThread(self):
        """log the gps data from serial by threading
        """
        
        while  self.GPSLogState and self.ModemLogState :
            #print "in thread"
            output = self.GPSserial.GetSerialReadline()
            #print output
            self.GPSLogFile.write(output)
        
    def AutoSendThread(self):
        while self.AutoSendState:
            for mess in self.AutoCommandList.keys():
                output = self.commandserial.SendSerialCommand(mess)
                        
                self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
                self.txt.yview(END)
                if self.ModemLogFile != None:
                    myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
                    self.ModemLogFile.write(myUTCtime+":"+output+"\r\n")
            time.sleep(self.AutoSendTimeInterval)   
            pass

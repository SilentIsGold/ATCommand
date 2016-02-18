import time
import sys
import glob
from datetime import datetime
import threading
from Serial import Serialport
from  Tkinter import *

class Logger():
    def __init__(self):
        """This is for encry the data and decry
        """
        self.UploadKey = 9600
        self.TempKey=123
        
        #self.AutoSendState=0
        self.AutoCommandList={}
        self.ModemLogFile=None
        self.GPSLogState = False
        self.ModemLogState=False
        self.GPSLogFile=None
        
        
    def Encry(self,file,mode):
        """encry the file with key
        mode :1 -->upload encry
        mode :2 -->temp encry
        """
        pass
        
        
    def Decry(self,file):
        """decrt the temp file
        """
        pass
    
    def SetGPSLogState(self,state):
        self.GPSLogState=state
    
    def SetModemLogState(self,state):
        self.ModemLogState=state
    
    def SetAutoSendState(self,state):
        """function.py will set this variable
        """
        self.AutoSendState=state
    
    def SetAutoCommandList(self,list):
        self.AutoCommandList.clear()
        self.AutoCommandList=list.copy()
        
    def SetScrollText(self,frame):
        """get the GUI fram
        """
        self.txt=frame
    
    def SetModemLogFile(self,file,mode):
        """open or close the file
        mode1: open
        mode2: close

        """
        if mode==1:
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            self.ModemLogFile = open(".//Log//"+myUTCtime+"-"+file,"w")
        else:
            if self.ModemLogFile != None :

                self.ModemLogFile.close()
                self.ModemLogFile = None
    
    def SetGPSLogFile(self,mode):
        """open or close the log
        mode1: open
        mode2: close

        """
        if mode==1:
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            self.GPSLogFile = open(".//Log//"+myUTCtime+"-GPS","w")
        else:
            if self.GPSLogFile != None :

                self.GPSLogFile.close()
                self.GPSLogFile = None
    
    def StartAutoThread(self):
        self.AutoThread=threading.Thread(target=self.AutoSendThread)
        self.AutoThread.start()
    
    def StartGPSThread(self):
        self.GPSThread=threading.Thread(target=self.GPSLogThread)
        self.GPSThread.start()
    
    def Setcommandserial(self,serial):
        """get serial controll fomr function.py
        """
        self.commandserial=serial
    
    def SetGPSserial(self,serial):
        self.GPSserial=serial
    
    def SetAutoSendTimeInterval(self,interval):
        self.AutoSendTimeInterval=interval
    
    def ReadUserInPut(self,input):
        """get user input from function
        """
        output = self.commandserial.SendSerialCommand(mess)
        self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
        self.txt.yview(END)
        
        if self.ModemLogFile != None:
            myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
            self.ModemLogFile.write(myUTCtime+":"+output+"\r\n")
    
    
    def AutoSendThread(self):
        while self.AutoSendState:
            for mess in self.AutoCommandList.keys():
                output = self.commandserial.SendSerialCommand(mess)
                        
                self.txt.insert(END,"UserInput:"+mess+"\nOutput:"+output+"\r\n")
                self.txt.yview(END)
                if self.ModemLogFile != None:
                    dt = datetime.now()
                    sec_since_epoch = time.mktime(dt.timetuple()) + dt.microsecond/1000000.0

                    myUTCtime = sec_since_epoch * 1000
                    #myUTCtime = datetime.strftime(datetime.utcnow(),'%Y-%m-%d %H-%M-%S')
                    self.ModemLogFile.write(str(int(myUTCtime))+":"+output+"\r\n")
            time.sleep(self.AutoSendTimeInterval)   
            pass
            
    def GPSLogThread(self):
        """log the gps data from serial by threading
        TODO make sure the serial can readline
        """
        
        while  self.GPSLogState and self.ModemLogState :
            #print "in thread"
            output = self.GPSserial.GetSerialReadline()
            if len(output) >10:
            #print output
                
                dt = datetime.now()
                sec_since_epoch = time.mktime(dt.timetuple()) + dt.microsecond/1000000.0
                myUTCtime = sec_since_epoch * 1000
                self.GPSLogFile.write(str(dt)+","+output)
                #self.GPSLogFile.write(str(int(myUTCtime))+","+output)
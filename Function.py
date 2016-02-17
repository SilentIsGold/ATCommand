import time
import sys
import glob
import threading,json
import ftplib
import os
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
        self.GPSControll = GPSCommand()
        
        self.GPSLogState = False
        self.GPSLogFile = None
        self.GPSThread=None
        
        self.ModemLogState=False
        self.ModemLogFile=None
        self.ModemThread=None
        
        self.AutoSendState=None
        self.AutoCommandList={}

        self.AutoSendTimeInterval=1 #second
        self.ModemCommandList={}
        
        self.UploadConfigList={}
        self.UploadFileList={}
        
        self.Version=1.0;

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
        return self.AutoSendTimeInterval*1000, self.ModemCommandList.keys()
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
        self.ModemCommandList.clear()
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
    
    def ParseFileToJson(self):
        """cahnge the upload file into json format(both of the signal and gps)
        determine gps need to add in json or not
        """
        SignalFileList = self.UploadFileList.keys()
        
        for file in SignalFileList:
            print 'ParseFileToJson with file:',file
            GPSFIle = self.CheckGPS(file)
            self.ToJson(file,GPSFIle)
            
    
    def ToJson(self,signal,gps):
        """parse the signal and gps into one json file
        assume the gps log and signal are both as same timestamp formate 
        """
        GPSFile=None
        GPSLines=None
        if gps!=None:
            GPSFile=open(".//Upload//"+gps,"r")
            #GPSLines=GPSFile.readlines()
            gpsstate=1
        #SignalFile = open('.//Log//'+signal,'r')
        #SignalLines=SignalFile.readlines()
        
        WriteFile = open('.//Upload//'+signal,'w')
        
        
        
        timestamp=None
        jsonArray=[]
        jsonElement={}
        
        with open('.//Log//'+signal) as SignalFile:
            
            CommandResultList = self.modem.GetCommandResultList()#TODO need to dynamic change the modem 
            print 'open ',signal,CommandResultList
            for SignalLine in SignalFile:
                #print SignalLine
                if len(SignalLine) >15:#remove empty line
                    SignalLine = SignalLine.strip() 
                    SignalLine=SignalLine.replace(':',',')
                    line=SignalLine.split(',')#first is timestamp,second is command, other is result
                    if line[1] not in CommandResultList or len(line)<3:
                        #if is not a command result, pass to next one
                        continue
                    if timestamp == None:
                        #initial the time stamp
                        jsonElement.clear()
                        jsonElement=self.JsonReset()
                        #print jsonElement
                        timestamp= long(float(line[0])) #get minisceond
                        if GPSFile!=None:
                            #if GPS is available, check the time is correct or not
                            GPSLine=GPSFile.readline()
                            GPSLine=GPSLine.split(',')
                            GPStime = long(float(GPSLine[0]))/1000#use second to divide the data,not minisceond
                            #print 'GPS time=',GPStime
                            while timestamp/1000 > GPStime:
                                # if the GPS time is less than signal. then search the right one
                                GPSLine=GPSFile.readline()
                                if not GPSLine:#end of file, no data
                                    GPSFile.close()
                                    GPSFile=None
                                    GPSLine=None
                                    break
                                GPSLine=GPSLine.split(',')
                                GPStime = long(float(GPSLine[0]))/1000
                    
                    if long(float(line[0]))/1000 != timestamp/1000:#next timestamp
                        timestamp=long(line[0])
                        jsonArray.append(jsonElement.copy())
                        jsonElement.clear()
                        jsonElement=self.JsonReset()
                    
                    
                    command = CommandResultList[line[1]] #todo need to dynamic detect the right command list, now only get the choose one
                    
                    jsonElement['Time']=timestamp
                    for index, response in enumerate(command):
                        #index start with 0
                        if line[index+2]=='D':
                            #don't care
                            continue
                        if response in jsonElement['CellularInfo'][0]:
                            jsonElement['CellularInfo'][0][response]=line[index+2]
                        else:
                            jsonElement['other'][0][response]=line[index+2]
                    
                    if GPSFile != None:
                        #if GPS is available, check the time is correct or not
                        #print timestamp/1000,GPStime
                        while timestamp/1000 > GPStime:
                            # if the GPS time is less than signal. then search the right one
                            GPSLine=GPSFile.readline()
                            if not GPSLine:#end of file, no data
                                GPSFile.close()
                                GPSFile=None
                                GPStime=None
                                break
                            GPSLine=GPSLine.split(',')
                            GPStime = long(float(GPSLine[0]))/1000
                        
                        if timestamp/1000 == GPStime:#check if is in the same sceond.  don't care minisceond
                            jsonElement['Lat']=GPSLine[1]
                            jsonElement['Lng']=GPSLine[3]
                            
                        
                    #print line
                    
        jsonArray.append(jsonElement.copy())     #last data       
        json.dump(jsonArray, WriteFile)        
        
        #SignalFile.close()
        WriteFile.close()

        if GPSFile != None:

            GPSFile.close()
        #os.rename('.//Log//'+signal,'.//Log//'+signal+'-Uploaded')
    
    def JsonReset(self):
        jsonElement={}
        jsonElement.clear()
        seq = ("AppicationType", "ApplicationVersion", "Account","IMEI","Lat", "Lng","CellularInfo","other")
        jsonElement=dict.fromkeys(seq)
        jsonElement["AppicationType"]=self.commandserial.GetPlatformOS()
        jsonElement["ApplicationVersion"]=self.Version
        jsonElement["Account"]='this is pc'
        jsonElement["CellularInfo"]=[]
        cellseq=( "Time","CellID","CellMCC","CellMNC","CellPCI","CellTAC","RSSI","SINR","RSRQ","RSRP")
        cell=dict.fromkeys(cellseq)
        jsonElement["CellularInfo"].append(cell)
        jsonElement["other"]=[]
        jsonElement["other"].append({})
        return jsonElement
    
    def CheckGPS(self,file):
        """check the upload file need gps or not
        """
        
        lasttag=file.rfind('-')
        GPSfile=file[:lasttag]+'-GPS'
        print 'CheckGPS with ',GPSfile
        for gpslist in os.listdir('.//Log'):
            if gpslist==GPSfile:
                self.GPSControll.ValidGPSFile(gpslist)
                return GPSfile
        return None
        
    def UploadFile(self):
        """upload the file to the server
        """
  
        UploadConfig = self.GetUploadConfig()
        self.ParseFileToJson()
        #session = ftplib.FTP(UploadConfig['Server IP'],UploadConfig['Server ID'],UploadConfig['Server PW'])
        ftp = ftplib.FTP()
        ftp.connect(UploadConfig['Server IP'], 21)
        ftp.login(UploadConfig['Server ID'],UploadConfig['Server PW'])
        print "Logging in"
        

        for filename in self.UploadFileList.keys():
            print 'upload file:',filename
            try:
                uploadfile=open('.//Upload//'+filename,'rb')
                ftp.storbinary("STOR " + filename, uploadfile)     # send the file
            #file.close()                                    # close file and FTP
            
                print 'uploaded ',filename
            except IOError:
                print "failed to upload"
        print 'close ftp'
        ftp.close()
        self.UploadFileList.clear()
        
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

import serial
import time
import sys
import glob
from datetime import datetime

class Serialport():
    def __init__(self):
        self.SerialPortList= []
        self.SerialPortUsed = ""
        self.SerialPort=None
        self.SendInterval =  "1000"
        
        self.LogFileName = ""
        self.LogPath = "./"
        
        self.DetectPlatformOS()
     
    def SetLogNameAndPath(self,name="original",path="./"):
        pass
        
    def CheckLogName(self,name):
        pass
    
    def GetPlatformOS(self):
        return self.Platform
    
    def DetectPlatformOS(self):
        """Find out PlatformOS
        """
        if sys.platform.startswith('win'):
            self.Platform = "win"
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            self.Platform = "linux"
        elif sys.platform.startswith('darwin'):
            self.Platform = "darwin"
        else:
            self.Platform = "NaN"
            raise EnvironmentError('Unsupported platform')    
            
    def SetSendInterval(self,interval):
        """Set interval of request sending with ms
        divide to 1000 (time.sleep use second)
        """
        self.SendInterval = interval/1000.0 #time.sleep use second


            
    def SetSerialPort(self, port,baudrate=9600):
        """Set serial port to use modem
        """
        self.SerialPortUsed = port
        self.SerialPort = serial.Serial(port,baudrate,timeout=0)
        self.SerialPort.close()
        self.SerialPort.open()
    
    def GetSerialPortList(self):
        """return available Serial port
        """
        self.FindSerialPort()
        return self.SerialPortList
        
    def SendSerialCommand(self,command):
        """Send Serial command to serial port
        """
        if self.SerialPortUsed != "":
            self.SerialPort.write(command)
            time.sleep(self.SendInterval)   
            return self.SerialPort.read(size=100)
        else:
            raise EnvironmentError('Serial not choosen')


            
    def FindSerialPort(self):
        """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        """
        if self.Platform == "win":
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif self.Platform == "linux":
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif self.Platform == "darwin":
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.SerialPortList.append(port)
            except (OSError, serial.SerialException):
                pass
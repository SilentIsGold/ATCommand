import time
import sys
import glob
from datetime import datetime




count =0

class GPSCommand():
    def __init__(self):
        """In case the GPS has different update rate or baud rate
        updaterate use ms
        """
        self.BaudRate = 9600
        self.UpdateRate = 1000
        

    
    def GeBaudRate(self):
        """Return baud rate
        """
        return self.BaudRate
    
    def SetBaudRate(self,rate):
        """set baud rate
        """
        self.BaudRate = rate

    def GetUpdateRate(self):
        """Return update rate
        """
        return self.UpdateRate
        
    def SetUpdateRate(self,rate):
        """set update rate
        """
        self.UpdateRate = rate
       
    
   
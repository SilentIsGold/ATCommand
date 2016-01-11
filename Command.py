import time
import sys
import glob
from datetime import datetime
from Serial import Serialport



count =0

class Command():
    def __init__(self):
        """ModemVailList is support model list
        ModemConfList is the conf file for support command list
        ChooseModem is choosen modem to use
        """
        self.ModemVailList = ["Huawei E3372"]
        self.ModemConfList = {"Huawei E3372":"HuaweiE3372.conf"}
        self.ChooseModem = self.ModemVailList[0]

    
    def GetModemList(self):
        """Return support modem
        """
        return self.ModemVailList
    
    def SetChooseModem(self,modem):
        """Get choosen modem to use
        """
        self.ChooseModem = modem

    def GetModemCommandList(self):
        """Return available modem command
        """
        with open(self.ModemConfList[self.ChooseModem]) as f:
            CommandList = f.read().splitlines()
        return CommandList
        
        
       

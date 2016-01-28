import time
import sys,os
import glob
from datetime import datetime




count =0

class ModemCommand():
    def __init__(self):
        """ModemVailList is support model list
        ModemConfList is the conf file for support command list
        ChooseModem is choosen modem to use
        """
        self.ModemVailList = []
        self.ModemConfList = {}
        self.ChooseModem = None
        
        self.GetModemList()
    
    def GetModemList(self):
        """Return support modem
        """
        for company in os.listdir('.//Modem'):
            print company
            for modem in os.listdir('.//Modem//'+company):
                print modem
                modemName = modem.split('.')
                self.ModemVailList.append(company+modemName[0])
                self.ModemConfList[company+modemName[0]] = company+modem
                print self.ModemVailList, self.ModemConfList
        
        
        return self.ModemVailList
    
    def SetChooseModem(self,modem):
        """set  modem to use
        """
        self.ChooseModem = modem

    def GetModemCommandList(self):
        """Return available modem command
        """
        with open(self.ModemConfList[self.ChooseModem]) as f:
            CommandList = f.read().splitlines()
        return CommandList
        
    def SpecialCommand(self,path,command):
        """For those modem that need to special command to enter debug mode
        """
        pass    
       
    
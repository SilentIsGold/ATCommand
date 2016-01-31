import time
import sys,os,re
import glob
from datetime import datetime




count =0

class ModemCommand():
    def __init__(self):
        """ModemVailList is support model list
        ModemConfList is the conf file for support command list
        ChooseModem is choosen modem to use
        """
        #self.ModemVailList = []
        self.ModemConfList = {}
        self.ChooseModem = None
        
        #self.GetModemList()
        self.TAGList=[]
        self.CommandList={}
    
    def GetModemList(self):
        """Return support modem
        """
        for company in os.listdir('.//Modem'):
            print company
            for modem in os.listdir('.//Modem//'+company):
                print modem
                modemName = modem.split('.')
                #self.ModemVailList.append(company+" "+modemName[0])
                self.ModemConfList[company+" "+modemName[0]] = ".//Modem//"+company+"//"+modem
                print self.ModemConfList.keys()
        
        
        return self.ModemConfList.keys()
    def GetModemName(self):
        """return choosen modem name
        """
        return self.ChooseModem
    
    def SetChooseModem(self,modem):
        """set  modem to use
        """
        self.ChooseModem = modem
        self.TAGList[:]=[]
        self.CommandList.clear()
        self.GetModemCommandList(self.ModemConfList[self.ChooseModem])
        return self.CommandList.keys()

    # def GetModemCommandList(self):
        # """Return available modem command
        # """
        # with open(self.ModemConfList[self.ChooseModem]) as f:
            # CommandList = f.read().splitlines()
        # return CommandList
        
    def SpecialCommand(self,path,command):
        """For those modem that need to special command to enter debug mode
        """
        pass    
       
    def GetModemCommandList(self,FilePath):
        with open(FilePath) as file:
            for line in file.readlines():
                line = line.split(' ') 
                print line
                if len(line) == 1 or line[0].startswith("#"):
                    #is comment
                    continue
                command = line[0]
                response = line[1]#.split(",")
                response = re.split(r'[,\n]',response)
                response = filter(None, response)#remove empty string
                if command == "TAG":
                    #list = response.split(',')
                    for value in response:
                        self.TAGList.append(value)
                else:
                    self.CommandList[command]=response
            print self.CommandList        
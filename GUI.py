from  Tkinter import *

from Function import Function
   
class GUIDemo():
    def __init__(self, master=None):
        #self.commandserial = Serialport()
        #self.GPSserial = Serialport()
        #self.modem = Command()
        self.function = Function()
        self.SerialList=["Choose"]
        #master.minsize(width=666, height=666)
        
        self.myParent = master

        self.main_container = Frame(master, bg="green",width=800, height=666)
        self.main_container.grid()

        self.top_frame = Frame(self.main_container, bg="red",width=666, height=666)
        self.top_frame.grid()
        
        self.bottom_frame = Frame(self.main_container, bd=2, bg="yellow",width=666, height=666)
        self.bottom_frame.grid(row=2, column=0)

        self.top_left = Frame(self.top_frame, bd=2)
        self.top_left.grid(row=0, column=0)

        self.top_right = Frame(self.top_frame, bd=2)
        self.top_right.grid(row=0, column=2)
        
        self.popwindows=[]
        # for page in range(4):
            # self.popwindows.append(Toplevel(master))
        
        self.createTopWidgets()
        self.createButtomWidgets()
        #self.Serialrefreshevent()
    
        
        
    def createTopWidgets(self):
        self.createUserInputButton()
        self.createLogButton()
        self.createAutoSendButton()
        self.createSerialButton()
        self.createGPSButton()
        self.createUploadButton()
        self.createSystemLabel()    
        
    
    def createUserInputButton(self):
        self.inputText = Label(self.top_frame)
        self.inputText["text"] = "Input Command:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self.top_frame)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=5)
        self.inputField.bind('<Return>',  self.EntryEnterEvent )
        
        self.enter = Button(self.top_frame,command = self.Enterevent) 
        self.enter["text"] = "Enter"
        self.enter.grid(row=0,column=6,sticky=E)   
        
    def createSystemLabel(self):
        self.systiminfoText = Label(self.top_frame, text = "System Info: ")
        self.systiminfoText.grid(row=4, column=0)
        
        self.displayText = Label(self.top_frame)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=4, column=1)
    
    def createLogButton(self):
        myrow=0
        self.logstate = IntVar()
        self.logbutton = Checkbutton(self.top_frame, text="Log Data", variable=self.logstate)
        self.logbutton.grid(row=2, column=0)
        
        self.logconfig = Button(self.top_frame, text="Log Config", command = self.Logconfigevent)
        self.logconfig.grid(row=3, column=0)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        
        
        
    def createAutoSendButton(self):
        self.autosendstate = IntVar()
        self.autosend = Checkbutton(self.top_frame, text="AutoSend", variable=self.autosendstate)
        self.autosend.grid(row=2, column=1)
        
        self.autosendconfig = Button(self.top_frame, text="AutoSend Config", command = self.Autosendconfigevent)
        self.autosendconfig.grid(row=3, column=1)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        
        
    def createSerialButton(self):
        self.serialchoose = StringVar(self.top_frame)
        self.serialchoose.set(self.SerialList[0]) # default value
        self.serialportmenu =  OptionMenu(self.top_frame, self.serialchoose, self.SerialList, command = self.Serialchooseevent )
        self.serialportmenu.grid(row=2, column=2)
        
        self.serialrefresh = Button(self.top_frame, text = "Serial refresh", command=self.Serialrefreshevent )
        self.serialrefresh.grid(row=3, column=2)
        
    def createGPSButton(self):
        self.gps = Button(self.top_frame, text = "GPS Config", command = self.GPSevent)
        self.gps.grid(row=2, column=4)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        
        
    def createUploadButton(self):
        myrow=0
        self.upload = Button(self.top_frame, text = "Upload", command = self.Uploadevent)
        self.upload.grid(row=2, column=5 )
        
        self.uploadconfig = Button(self.top_frame,text="Upload Config", command = self.Uploadconfigevent)
        self.uploadconfig.grid(row=3, column=5)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        
    
    def createButtomWidgets(self):
        
        
        self.txt = Text(self.bottom_frame, height=20)
        
        self.txt.grid(row=0, column=0, columnspan=7)
        # self.txt.insert(END,"456")
        # for i in range(100):
            # self.txt.insert(END,"789\n\n")
        self.scroll = Scrollbar(self.bottom_frame,command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=7, sticky='Ens')
    
    def Logevent(self):
        pass
    
    def Logconfigevent(self):
        myrow=0
        #self.popwindows.append(Toplevel())
        self.Logpopwindows = Toplevel()
        self.Logpopwindows.title("Log Config")
        msg = Label(self.Logpopwindows, text="Log configure window")
        msg.grid(row=myrow, column=0)
        myrow+=1
        
        self.logTimeStampstate = IntVar()
        logFileText = Checkbutton(self.Logpopwindows,text="Use Time Stamp", variable=self.logTimeStampstate)
        logFileText.grid(row=myrow,column=0)
        myrow+=1
        
        
        Cancel = Button(self.Logpopwindows, text="Cancel", command=self.Logpopwindows.destroy)
        Cancel.grid(row=myrow, column=1)
        
        Save = Button(self.Logpopwindows, text="Save", command=self.LogconfigSaveevent)
        Save.grid(row=myrow, column=0)

        
        self.displayText["text"] = "Logconfigevent" + str(self.logstate.get())
        pass
    
    def Autosendevent(self):
        pass
    
    def Autosendconfigevent(self):
        myrow=0
        self.Autosendpopwindows=Toplevel()
        self.Autosendpopwindows.title("Log Config")
        msg = Label(self.Autosendpopwindows, text="AutoSend configure window")
        msg.grid(row=0, column=0)
        
        button = Button(self.Autosendpopwindows, text="Cancel", command=self.Autosendpopwindows.destroy)
        button.grid(row=1, column=1)
        
        Save = Button(self.Autosendpopwindows, text="Save", command=self.AutosendconfigSaveevent)
        Save.grid(row=1, column=0)
        

        self.displayText["text"] = "Autosendconfigevent" + str(self.autosendstate.get())
        pass
        
    def Serialevent(self):
        pass
    
    def Serialrefreshevent(self):
        """Get the abailable serial list from Serial.py
        """
        self.SerialList[:]=[] #refres list
        self.SerialList = self.function.GetModemSerialPort()
        
        #update the optionbutton
        self.serialportmenu['menu'].delete(0, 'end')
        for choice in self.SerialList:
            self.serialchoose.set(choice)
            #self.serialportmenu['menu'].add_command(label=choice, command=lambda v=choice: self.serialchoose.set(v) )
            self.serialportmenu['menu'].add_command(label=choice, command=self.Serialchooseevent )
        #self.serialportmenu['command']=self.Serialchooseevent
        
        self.displayText["text"] = "Serialrefreshevent" + str(self.SerialList) + str(self.serialchoose.get())
        
    def Serialchooseevent(self,value=0):
        """User choose a serial port
        """
        print value,self.serialchoose.get()
        self.function.SetModemSerialPort(self.serialchoose.get())
        
        self.displayText["text"] = "Serialchooseevent" + str(self.SerialList) + str(self.serialchoose.get())
        pass
    
    def GPSevent(self):
        myrow=0
        self.GPSpopwindows=Toplevel()
        self.GPSpopwindows.title("Log Config")
        msg = Label(self.GPSpopwindows, text="GPS configure window")
        msg.grid(row=0, column=0)
        
        button = Button(self.GPSpopwindows, text="Cancel", command=self.GPSpopwindows.destroy)
        button.grid(row=1, column=1)
        
        Save = Button(self.GPSpopwindows, text="Save", command=self.GPSSaveevent)
        Save.grid(row=1, column=0)

        self.displayText["text"] = "GPSevent" 
        pass
        
    def Uploadevent(self):
        
        
        self.displayText["text"] = "Uploadevent" 
        pass
       
    def Uploadconfigevent(self):
        myrow=0
        self.Uploadpopwindows=Toplevel()
        self.Uploadpopwindows.title("Log Config")
        msg = Label(self.Uploadpopwindows, text="Upload configure window")
        msg.grid(row=myrow, column=0)
        myrow+=1
        
        uploadUserText = Label(self.Uploadpopwindows,text="UserName")
        uploadUserText.grid(row=myrow,column=0)
        
        self.uploadUserField = Entry(self.Uploadpopwindows,width=15)
        self.uploadUserField.grid(row=myrow,column=1)
        myrow+=1
        
        uploadEmailText = Label(self.Uploadpopwindows, text="User Email")
        uploadEmailText.grid(row=myrow,column=0)
        
        uploadEmailField = Entry(self.Uploadpopwindows,width=30)
        uploadEmailField.grid(row=myrow,column=1)
        myrow+=1
        
        button = Button(self.Uploadpopwindows, text="Cancel", command=self.Uploadpopwindows.destroy)
        button.grid(row=myrow, column=1)
        
        Save = Button(self.Uploadpopwindows, text="Save", command=self.UploadconfigSaveevent)
        Save.grid(row=myrow, column=0)
        

        self.displayText["text"] = "Uploadconfigevent" 
        pass
    
    def Enterevent(self):
        self.displayText["text"] = "This is Enter."
        mess = self.inputField.get() + "\r"
        output = self.function.SetUserInPut(mess)
        self.txt.insert(END,output)
        
    def EntryEnterEvent(self,event):
        print "click"
        self.displayText["text"] = "entry enter"
        mess = self.inputField.get() + "\r\n"
        self.txt.insert(END,mess)
        
    def LogconfigSaveevent(self):
    
        
        self.Logpopwindows.destroy()
        self.displayText["text"] = "LogconfigSaveevent" 
        pass
        
    def AutosendconfigSaveevent(self):
        self.Autosendpopwindows.destroy()
        self.displayText["text"] = "AutosendconfigSaveevent" 
        pass
        
    def GPSSaveevent(self):
        self.GPSpopwindows.withdraw()
        self.displayText["text"] = "GPSSaveevent" 
        pass
        
    def UploadconfigSaveevent(self):
        self.Uploadpopwindows.withdraw()
        self.displayText["text"] = "UploadconfigSaveevent" 
        pass
    
class MyApp:
    def __init__(self, parent):
        self.myParent = parent

        self.main_container = Frame(parent, bg="green")
        self.main_container.grid()

        self.top_frame = Frame(self.main_container)
        self.top_frame.grid()

        self.top_left = Frame(self.top_frame, bd=2)
        self.top_left.grid(row=0, column=0)

        self.top_right = Frame(self.top_frame, bd=2)
        self.top_right.grid(row=0, column=2)

        self.top_left_label = Label(self.top_left, bd=2, bg="red", text="Top Left", width=22, anchor=W)
        self.top_left_label.grid(row=0, column=0)

        self.top_right_label = Label(self.top_right, bd=2, bg="blue", text="Top Right", width=22, anchor=E)
        self.top_right_label.grid(row=0, column=0)

        self.bottom_frame = Frame(self.main_container, bd=2)
        self.bottom_frame.grid(row=2, column=0)

        self.text_box = Text(self.bottom_frame, width=40, height=5)
        self.text_box.grid(row=0, column=0)        
 
if __name__ == '__main__':
    root = Tk()
    #root.geometry("800x600")
    root.title("AT-Command")
    app = GUIDemo(master=root)
    root.mainloop()
    # root.title("Test UI")
    # myapp = MyApp(root)
    # root.mainloop()
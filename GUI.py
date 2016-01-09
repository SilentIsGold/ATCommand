from  Tkinter import *
from Command import Command 
from Serial import Serialport
   
class GUIDemo():
    def __init__(self, master=None):
        self.commandserial = Serialport()
        self.GPSserial = Serialport()
        self.modem = Command()
        self.SerialList=["Refresh"]
        
        
        self.myParent = master

        self.main_container = Frame(master, bg="green")
        self.main_container.grid()

        self.top_frame = Frame(self.main_container, bg="red")
        self.top_frame.grid()
        
        self.bottom_frame = Frame(self.main_container, bd=2, bg="yellow")
        self.bottom_frame.grid(row=2, column=0)

        self.top_left = Frame(self.top_frame, bd=2)
        self.top_left.grid(row=0, column=0)

        self.top_right = Frame(self.top_frame, bd=2)
        self.top_right.grid(row=0, column=2)
        
        self.popwindows=[]
        for page in range(4):
            self.popwindows.append(Toplevel(master))
        
        self.createTopWidgets()
        self.createButtomWidgets()
    
        
        
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
        self.logstate = IntVar()
        self.logbutton = Checkbutton(self.top_frame, text="Log Data", variable=self.logstate)
        self.logbutton.grid(row=2, column=0)
        
        self.logconfig = Button(self.top_frame, text="Log Config", command = self.Logconfigevent)
        self.logconfig.grid(row=3, column=0)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        self.popwindows[0].title("Log Config")
        msg = Label(self.popwindows[0], text="Log configure window")
        msg.grid(row=0, column=0)
        
        Cancel = Button(self.popwindows[0], text="Cancel", command=self.popwindows[0].destroy)
        Cancel.grid(row=1, column=1)
        
        Save = Button(self.popwindows[0], text="Save", command=self.popwindows[0].destroy)
        Save.grid(row=1, column=0)
        
        self.popwindows[0].withdraw()
        
        
    def createAutoSendButton(self):
        self.autosendstate = IntVar()
        self.autosend = Checkbutton(self.top_frame, text="AutoSend", variable=self.autosendstate)
        self.autosend.grid(row=2, column=1)
        
        self.autosendconfig = Button(self.top_frame, text="AutoSend Config", command = self.Autosendconfigevent)
        self.autosendconfig.grid(row=3, column=1)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        self.popwindows[1].title("Log Config")
        msg = Label(self.popwindows[1], text="AutoSend configure window")
        msg.grid(row=0, column=0)
        
        button = Button(self.popwindows[1], text="Cancel", command=self.popwindows[1].destroy)
        button.grid(row=1, column=1)
        
        Save = Button(self.popwindows[1], text="Save", command=self.popwindows[1].destroy)
        Save.grid(row=1, column=0)
        
        self.popwindows[1].withdraw()
        
    def createSerialButton(self):
        self.serialchoose = StringVar(self.top_frame)
        self.serialchoose.set(self.SerialList[0]) # default value
        self.serialportmenu =  OptionMenu(self.top_frame, self.serialchoose, self.SerialList)
        self.serialportmenu.grid(row=2, column=2)
        
        self.serialrefresh = Button(self.top_frame, text = "Serial refresh", command=self.Serialrefreshevent )
        self.serialrefresh.grid(row=3, column=2)
        
    def createGPSButton(self):
        self.gps = Button(self.top_frame, text = "GPS Config", command = self.GPSevent)
        self.gps.grid(row=2, column=4)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        self.popwindows[2].title("Log Config")
        msg = Label(self.popwindows[2], text="GPS configure window")
        msg.grid(row=0, column=0)
        
        button = Button(self.popwindows[2], text="Cancel", command=self.popwindows[2].destroy)
        button.grid(row=1, column=1)
        
        Save = Button(self.popwindows[2], text="Save", command=self.popwindows[2].destroy)
        Save.grid(row=1, column=0)
        
        self.popwindows[2].withdraw()
        
    def createUploadButton(self):
        self.upload = Button(self.top_frame, text = "Upload", command = self.Uploadevent)
        self.upload.grid(row=2, column=5 )
        
        self.uploadconfig = Button(self.top_frame,text="Upload Config", command = self.Uploadconfigevent)
        self.uploadconfig.grid(row=3, column=5)
        
        #self.top.append(Toplevel())
        #self.top[0].geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
        self.popwindows[3].title("Log Config")
        msg = Label(self.popwindows[3], text="Upload configure window")
        msg.grid(row=0, column=0)
        
        button = Button(self.popwindows[3], text="Cancel", command=self.popwindows[3].destroy)
        button.grid(row=1, column=1)
        
        Save = Button(self.popwindows[3], text="Save", command=self.popwindows[3].destroy)
        Save.grid(row=1, column=0)
        
        self.popwindows[3].withdraw()
    
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
        self.popwindows[0].deiconify()
        self.displayText["text"] = "Logconfigevent" + str(self.logstate.get())
        pass
    
    def AutoSendevent(self):
        pass
    
    def Autosendconfigevent(self):
        self.popwindows[1].deiconify()
        self.displayText["text"] = "Autosendconfigevent" + str(self.autosendstate.get())
        pass
        
    def Serialevent(self):
        pass
    
    def Serialrefreshevent(self):
        """Get the abailable serial list from Serial.py
        """
        self.SerialList[:]=[] #refres list
        self.SerialList = self.commandserial.GetSerialPortList()
        
        #update the optionbutton
        self.serialportmenu['menu'].delete(0, 'end')
        for choice in self.SerialList:
            self.serialportmenu['menu'].add_command(label=choice, command=lambda v=choice: self.serialchoose.set(v) )

        
        self.displayText["text"] = "Serialrefreshevent" + str(self.SerialList) + str(self.serialchoose.get())
       
    
    def GPSevent(self):
        self.popwindows[2].deiconify()
        self.displayText["text"] = "GPSevent" 
        pass
        
    def Uploadevent(self):
        
        
        self.displayText["text"] = "Uploadevent" 
        pass
       
    def Uploadconfigevent(self):
        
        self.popwindows[3].deiconify()
        self.displayText["text"] = "Uploadconfigevent" 
        pass
    
    def Enterevent(self):
        self.displayText["text"] = "This is Enter."
        mess = self.inputField.get() + "\r\n"
        self.txt.insert(END,mess)
        
    def EntryEnterEvent(self,event):
        print "click"
        self.displayText["text"] = "entry enter"
        mess = self.inputField.get() + "\r\n"
        self.txt.insert(END,mess)
        
    
    
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
    root.title("AT-Command")
    app = GUIDemo(master=root)
    root.mainloop()
    # root.title("Test UI")
    # myapp = MyApp(root)
    # root.mainloop()
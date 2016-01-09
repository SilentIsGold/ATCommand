from  Tkinter import *
   
class GUIDemo():
    def __init__(self, master=None):
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
        
        self.createTopWidgets()
        self.createBottomWidgets()
    
        
    def createTopWidgets(self):
 
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
        
        
        
        self.new = Button(self.top_frame)
        self.new["text"] = "New"
        self.new.grid(row=2, column=0)
        self.load = Button(self.top_frame)
        self.load["text"] = "Load"
        self.load.grid(row=2, column=1)
        self.save = Button(self.top_frame)
        self.save["text"] = "Save"
        self.save.grid(row=2, column=2)
        self.encode = Button(self.top_frame)
        self.encode["text"] = "Encode"
        self.encode.grid(row=2, column=3)
        self.decode = Button(self.top_frame)
        self.decode["text"] = "Decode"
        self.decode.grid(row=2, column=4)
        self.clear = Button(self.top_frame)
        self.clear["text"] = "Clear"
        self.clear.grid(row=2, column=5)
        self.copy = Button(self.top_frame)
        self.copy["text"] = "Copy"
        self.copy.grid(row=2, column=6)
        
        
 
        self.displayText = Label(self.top_frame)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=3, column=0, columnspan=7)
        
        
    def createBottomWidgets(self):
        
        
        self.txt = Text(self.bottom_frame, height=20)
        
        self.txt.grid(row=0, column=0, columnspan=7)
        # self.txt.insert(END,"456")
        # for i in range(100):
            # self.txt.insert(END,"789\n\n")
        self.scroll = Scrollbar(self.bottom_frame,command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=7, sticky='Ens')
    
   
    
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
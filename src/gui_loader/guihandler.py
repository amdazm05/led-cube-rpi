import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.attributes( '-zoomed', True)
        self.title("NFT - CUBE")
        self.geometry('480x480')
        self.configure(bg='yellow')
        self.img = PhotoImage(file="background.png")
        label = Label(
            self,
            image=self.img
        )
        label.place(x=0, y=0)
        
        hello_button = tk.Button(self, text="Load Image", command=self.LoadImage, font=('Arial Bold', 16))

        hello_button.place(x=320,y=410)
        hello_button.config(bg="navy blue",fg="deeppink")
        hello_button["border"]="0"

        goodbye_button = tk.Button(self, text="Close Cube", command=self.ExitProgram,font=('Arial Bold', 16))
        goodbye_button.place(x=40,y=410)
        goodbye_button.config(bg="navy blue",fg="deeppink")
        goodbye_button["border"]="0"

    def getfilename(self):
        return self.filename
    def LoadImage(self): 
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        self.filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(self.filename +  " $")
        return self.filename

    def ExitProgram(self):
        if msgbox.askyesno("Close Window?", "Would you like to close this window?"):
            message = "Window will now close - goodybye " + self.name_entry.get()
            self.label_text.set(message)
            self.after(100, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open.")
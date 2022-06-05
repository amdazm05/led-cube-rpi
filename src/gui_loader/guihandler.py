import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes( '-zoomed', True)
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("My Name Is: ")
        self.filename="Hello"
        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self, text="Load Image", command=self.LoadImage)

        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self, text="Close Program", command=self.ExitProgram)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def getfilename(self):
        return self.filename
    def LoadImage(self):
        message = "Hello there " + self.name_entry.get()
        msgbox.showinfo("Hello", message)
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
import os
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename ,asksaveasfile
root = Tk()
root.title("Untitled - Notepad")
root.wm_iconbitmap("Progrmming.ico")
root.geometry("644x688")
# Add TextAread
TextArea = Text(root, font="lucida 13")
TextArea.pack(fill=BOTH, expand=True)
file = None
# Adding Menubar
MenuBar = Menu(root)
# Adding Scrollbar
Scroll = Scrollbar(TextArea)
Scroll.pack(fill=Y, side = RIGHT)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

#                   FileMenu Functions
def Newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes = [("All Files","*.*"),("Text Documents")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    
def Save():
    global file
    if file == None:
        file = asksaveasfile(initialfile = 'Untitled.txt', defaultextension = ".txt",filetypes = [("All Files","*.*"),("Text Documents")])
        if file == "":
            file = None
        else:
            #Save as a New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
         #Save the New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
def QuitApp():
    root.destroy()

#                   EditMenu Functions
def Copy():
    TextArea.event_generate(("<<Copy>>"))
def Cut():
    TextArea.event_generate(("<<Cut>>"))
def Paste():
    TextArea.event_generate(("<<Paste>>"))

#                       HelpMenu Functions
def AboutPad():
    message = tmsg.showinfo("About","This is a text editor Made By Adityaraj")


#                  FileMenu Start
# To Open New File and To Open already existing file and To Save a Current File
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=Newfile)
FileMenu.add_command(label="Open", command=OpenFile)
FileMenu.add_command(label="Save", command=Save)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=QuitApp)
MenuBar.add_cascade(label="File", menu=FileMenu)

#                  Edit Menu Starts
# To give a feature of cut,copy and paste
EditMenu = Menu(MenuBar,tearoff=0)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Paste", command=Paste)
MenuBar.add_cascade(label="Edit", menu= EditMenu)

#                  Help Menu Starts
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command="AboutPad")
MenuBar.add_cascade(label="Help", menu= HelpMenu)

root.config(menu=MenuBar)
root.mainloop()
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Untitled - Notepad")
root.wm_iconbitmap("Progrmming.ico")
root.geometry("644x788")
# Add TextAread
TextArea = Text(root, font="lucida 13")
TextArea.pack(fill=BOTH, expand=True)
file = None
# Adding Menubar
MenuBar = Menu(root)
# Adding Scrollbar
ScrollBar = Scrollbar(TextArea)
ScrollBar.pack(fill=BOTH, side = RIGHT)
text = Text(root, yscrollcommand = ScrollBar.set)
text.pack(fill= BOTH)
ScrollBar.config(command=text.yview)

#                   FileMenu Functions
def Newfile():
    pass
def OpenFile():
    pass
def Save():
    pass
def QuitApp():
    pass
def FileMenu():
    pass

#                   EditMenu Functions
def Cut():
    pass
def Copy():
    pass
def Paste():
    pass
def EditMenu():
    pass

#                       HelpMenu Functions
def AboutPad():
    pass


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
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Paste", command=Paste)
MenuBar.add_cascade(label="Edit", menu= EditMenu)

#                  Help Menu Starts
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command="AboutPad")
MenuBar.add_cascade(label="Help", menu= HelpMenu)

root.config(menu=MenuBar)
root.mainloop()
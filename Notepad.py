from tkinter import *
root = Tk()
root.title("Untitled - Notepad")
root.wm_iconbitmap("Programming.ico")
root.geometry("644x788")
# Add TextAread
TextArea = Text(root, font="lucida 13")
file = None

# Adding Menubar
MenuBar = Menu(root)

#                  FileMenu Start
# To Open New File and To Open already existing file and To Save a Current File
FileMenu = Menu(Menubar, tearoff=0)
FileMenu.add_command(label="New", command=newfile)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=Save)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=quitApp)
MenuBar.add_cascade(label="File", menu=FileMenu)

#               Edit Menu Starts
EditMenu = Menu(MenuBar,tearoff=0)
# To give a feature of cut,copy and paste
EditMenu.add_command(label="Cut", command=Cut)
EditMenu.add_command(label="Copy", command=Copy)
EditMenu.add_command(label="Paste", command=Paste)
EditMenu.add_cascade(label="Edit", menu= EditMenu)


root.mainloop()
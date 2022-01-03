from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("ImageNote.ioc")
    root.geometry("644x788")

    # Add TextAread
    TextArea = Text(root, font="lucida 13")
    file = None

    # Adding Menubar
    MenuBar = Menu(root)
    FileMenu = Menu(Menubar, tearoff=0)
    # To Open New File
    FileMenu.add_command(label="New", command=newfile)

    # To Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # To Save a Current File
    FileMenu.add_command(label="Save", command=Save)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)


    root.mainloop()
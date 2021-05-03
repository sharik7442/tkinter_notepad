from tkinter import  *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetype=[("All Files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "- Notebook")
        TextArea.delete(1.0, END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def saveFile():

    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetype=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None

        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notebook")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()






def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by sharik")





if __name__ == '__main__':
    root=Tk()
    root.title("untitled notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")


    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    # lets create a menu bar
    menubar=Menu(root)
    # filemenu start
    filemenu=Menu(menubar,tearoff=0)
    # to open a new file
    filemenu.add_command(label="New",command=newFile)

    filemenu.add_command(label="open", command=openFile)

    filemenu.add_command(label="save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=filemenu)


    # editmenu start
    editmenu = Menu(menubar, tearoff=0)
    # to open a new file
    editmenu.add_command(label="cut", command=cut)

    editmenu.add_command(label="copy", command=copy)

    editmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editmenu)

    # Help menu start
    Helpmenu = Menu(menubar, tearoff=0)
    # to open a new file
    Helpmenu.add_command(label="About notepad", command=about)
    menubar.add_cascade(label="Help", menu=Helpmenu)


    root.config(menu=menubar)

    scrollbar=Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
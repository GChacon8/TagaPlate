from cgitb import text
import code
from distutils.cmd import Command
from tkinter import Tk, Menu
from turtle import bgcolor
from typing import Text
from tkinter import *
from tkinter import filedialog
from tkinter.tix import *
# root window
def saveFile():
    file = open ('TagaPlateCode.txt','w')
    code = textCode.get("1.0","end-1c")
    #print(code)
    file.write(code)
    file.close()

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    return filename

def openFile():
    fileName = browseFiles()
    #print(fileName)
    file = open(fileName, 'r')
    code = file.read()
    #print(code)
    textCode.insert(END, code)
    file.close()


root = Tk()
root.geometry('1400x800')
root.title('TagaPlate IDE')

iconButtonSave = PhotoImage(file='Save_1.png')
iconButtonOpen=PhotoImage(file="open.png")
iconButtonRun=PhotoImage(file="run.png")

scroll=scroll=Scrollbar(root, orient='vertical')
scroll.pack(side=RIGHT, fill='y')

lblCode = Label(root, text="Code")
lblCode.place(x=500,y=5)

textCode = Text(root,height=35, width=130)
scroll.config(command=textCode.yview)
textCode.place(x=5,y=40)

lblErrors = Label(root, text="Errors")
lblErrors.place(x=1220,y=5)

textErrors = Text(root,height=35, width=40)
textErrors.place(x=1065,y=40)

lblTerminal = Label(root, text="Terminal")
lblTerminal.place(x=5, y=607)

saveButton=Button(root, text="save", image=iconButtonSave, width="30", height="30", command=saveFile)
saveButton.place(x=0,y=0)
openFileButton=Button(root,text="open", image=iconButtonOpen,width="30",height="30", command=openFile)
openFileButton.place(x=35,y=0)
runButton=Button(root,text="run",image=iconButtonRun, width="30",height="30" )
runButton.place(x=70,y=0)


textTerminal = Text(root,height=10, width=173)
textTerminal.place(x=5,y=630)

tip = Balloon(root)
#Bind the tooltip with button
tip.bind_widget(openFileButton, balloonmsg="open")
tip.bind_widget(saveButton, balloonmsg="save")
tip.bind_widget(runButton,balloonmsg="run")


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='Open', command = openFile)
file_menu.add_command(label='Save', command = saveFile)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Compile')
help_menu.add_command(label='Run')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Program",
    menu=help_menu,
    underline=0
)


root.mainloop()
from tkinter import *
from tkinter import filedialog
from tkinter.tix import *
# root window
"""
def saveFile():
    file = open ('TagaPlateCode.tgp', 'w')
    code = textCode.get("1.0","end-1c")
    #print(code)
    file.write(code)
    file.close()

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("TagaPlate files",
                                                        "*.tgp*"),
                                                       ))
    return filename

def openFile():
    fileName = browseFiles()
    #print(fileName)
    file = open(fileName, 'r',encoding="UTF-8")
    code = file.read()
    #print(code)
    textCode.insert(END, code)
    file.close()
"""

class Errors:
    def __init__(self,root):
        self.__root = root
        self.__createLabel()
        self.__createErrorsBox()
    def __createLabel(self):
        lblErrors = Label(self.__root, text="Errors",background="#5e5d5b", foreground="#ffffff")
        lblErrors.place(x=1220, y=5)
    def __createErrorsBox(self):
        textErrors = Text(self.__root, height=35, width=40, background="#3d3f42", foreground="#ffffff")
        textErrors.place(x=1065, y=40)
class Terminal:
    def __init__(self,root):
        self.__root = root
        self.__createLabel()
        self.__createTerminalBox()
    def __createLabel(self):
        Label(self.__root, text="Terminal",background="#5e5d5b", foreground="#ffffff").place(x=5, y=607)
    def __createTerminalBox(self):
        Text(self.__root, height=10, width=173, background="#3d3f42", foreground="#ffffff").place(x=5, y=630)

class TextCodeIDE:
    def __init__(self,root):
        self.__root = root
        self.__textCode = None
        self.__linenumbers = None
        self.__scroll=None
        self.__createLabel()
        self.__createCodeBox()
        self.__addLineNumbers()
        self.__addLineNumbers()
        self.__scrollLineNumberAndCodeBox()
    def getTextBox(self):
        return self.__textCode

    def __addLineNumbers(self):
        self.__linenumbers = Text(self.__root, width=2,height=35,background="#3d3f42", foreground="#ffffff")
        self.__linenumbers.place(x=0,y=40)
        self.__linenumbers.tag_configure('line', justify='right')
        self.__number_line()
    def __number_line(self, interval=100):
        self.__linenumbers.config(state=NORMAL)
        self.__linenumbers.delete("1.0","end")
        for i in range(0,int(str(self.__textCode.index('end-1c')).split('.')[0])):
            self.__linenumbers.insert(INSERT,str(i+1)+"\n")
        self.__linenumbers.config(state=DISABLED)
        self.__linenumbers.after(interval, self.__number_line)
    def __createLabel(self):
        lblCode = Label(self.__root, text="Code",background="#5e5d5b", foreground="#ffffff")
        lblCode.place(x=500, y=5)
    def __createCodeBox(self):
        self.__textCode = Text(self.__root, height=35, width=130, background="#3d3f42", foreground="#ffffff",undo=True)
        self.__textCode.place(x=20, y=40)
        self.__textCode.tag_configure("current_line", background="#454647")
        self._highlight_current_line()
    def _highlight_current_line(self, interval=100):
        '''Updates the 'current line' highlighting every "interval" milliseconds'''
        self.__textCode.tag_remove("current_line", 1.0, "end")
        self.__textCode.tag_add("current_line", "insert linestart", "insert lineend+1c")
        self.__textCode.after(interval, self._highlight_current_line)

    def __scrollBoth(self, action, position, type=None):
        self.__textCode.yview_moveto(position)
        self.__linenumbers.yview_moveto(position)

    def __updateScroll(self, first, last, type=None):
        self.__textCode.yview_moveto(first)
        self.__linenumbers.yview_moveto(first)
        self.__scroll.set(first, last)

    def __scrollLineNumberAndCodeBox(self):
        self.__scroll = Scrollbar(self.__root, orient='vertical', background="#5e5d5b")
        self.__scroll.place(x=3 + self.__textCode.winfo_reqwidth(), y=40, height=self.__textCode.winfo_reqheight())
        #self.__textCode.configure(yscrollcommand=self.__scroll.set)
        #self.__scroll.config(command=self.__textCode.yview)
        self.__scroll.config(command=self.__scrollBoth)
        self.__textCode.config(yscrollcommand=self.__updateScroll)
        self.__linenumbers.config(yscrollcommand=self.__updateScroll)




class myMenu:
    def __init__(self,root,textCode,menubar,iconButtonSave,iconButtonOpen,iconButtonRun):
        self.__root = root
        self.__textCode = textCode
        self.__menubar = menubar
        self.__file_menu = Menu(self.__menubar,tearoff=0)
        self.__createMenu(iconButtonSave,iconButtonOpen,iconButtonRun)
        self.__lastOpenedFile="Untitled.tgp"
    def saveFileAs(self):
        file = filedialog.asksaveasfilename(initialdir="/",
                                              title="Choose the Name File",
                                              filetypes=(("TagaPlate files",
                                                          "*.tgp*"),
                                                         ))
        if file.endswith(".tgp"):
            file = open(file, 'w')
        else:
            file = open(file+".tgp", 'w')
        code = self.__textCode.get("1.0", "end-1c")
        file.write(code)
        file.close()
        self.__lastOpenedFile = str(file.name)

    def saveFile(self):
        print(self.__lastOpenedFile)
        file = open(self.__lastOpenedFile, 'w')
        print(file.name)
        code = self.__textCode.get("1.0", "end-1c")
        # print(code)
        file.write(code)
        file.close()
        self.__lastOpenedFile = str(file.name)

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("TagaPlate files",
                                                          "*.tgp*"),
                                                         ))
        return filename

    def openFile(self):
        fileName = self.browseFiles()
        # print(fileName)
        file = open(fileName, 'r', encoding="UTF-8")
        code = file.read()
        # print(code)
        self.__textCode.insert(END, code)
        file.close()
        self.__lastOpenedFile = str(file.name)
    def __createMenu(self,iconButtonSave,iconButtonOpen,iconButtonRun):
        self.__createFileMenu()
        self.__createHelpMenu()
        self.__createIconMenu(iconButtonSave,iconButtonOpen,iconButtonRun)
    def __createFileMenu(self):
        # add menu items to the File menu
        self.__file_menu.add_command(label='Open', command=self.openFile)
        self.__file_menu.add_command(label='Save', command=self.saveFile)
        self.__file_menu.add_command(label='Save As', command=self.saveFileAs)
        # add Exit menu item
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label='Exit',command=self.__root.destroy)

        self.__menubar.add_cascade(label="File",menu=self.__file_menu,underline=0)
        # create the Help menu
        self.help_menu = Menu(self.__menubar,tearoff=0)
    def __createHelpMenu(self):
        self.help_menu.add_command(label='Compile')
        self.help_menu.add_command(label='Run')

        # add the Help menu to the menubar
        self.__menubar.add_cascade(label="Program",menu=self.help_menu,underline=0)
    def __createIconMenu(self,iconButtonSave,iconButtonOpen,iconButtonRun):
        saveButton = Button(self.__root, text="save", image=iconButtonSave, width="30", height="30", command=self.saveFile)
        saveButton.place(x=0, y=0)
        openFileButton = Button(self.__root, text="open", image=iconButtonOpen, width="30", height="30", command=self.openFile)
        openFileButton.place(x=35, y=0)
        runButton = Button(self.__root, text="run", image=iconButtonRun, width="30", height="30")
        runButton.place(x=70, y=0)
        tip = Balloon(self.__root)
        # Bind the tooltip with button
        tip.bind_widget(openFileButton, balloonmsg="open")
        tip.bind_widget(saveButton, balloonmsg="save")
        tip.bind_widget(runButton, balloonmsg="run")

class WindowIDE:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry('1400x800')
        self.__root.title('TagaPlate IDE')
        self.__root.configure(background="#5e5d5b")
        self.__menubar = Menu(self.__root)
        self.__iconButtonSave = PhotoImage(file='IDE/Save_1.png')
        self.__iconButtonOpen = PhotoImage(file="IDE/open.png")
        self.__iconButtonRun = PhotoImage(file="IDE/run.png")
        self.__textCode = None
        self.__setIDE()

    def __setIDE(self):
        self.__setBoxes()
        self.__setMenu()
        self.__root.mainloop()
    def __setMenu(self):
        self.__root.config(menu=self.__menubar)
        myMenu(self.__root,self.__textCode,self.__menubar,self.__iconButtonSave,self.__iconButtonOpen,self.__iconButtonRun)
    def __setBoxes(self):
        textCodeTemp = TextCodeIDE(self.__root)
        self.__textCode = textCodeTemp.getTextBox()
        Terminal(self.__root)
        Errors(self.__root)

    def saveFile(self):
        file = open('TagaPlateCode.tgp', 'w')
        code = self.__textCode.get("1.0", "end-1c")
        # print(code)
        file.write(code)
        file.close()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("TagaPlate files",
                                                          "*.tgp*"),
                                                         ))
        return filename

    def openFile(self):
        fileName = self.browseFiles()
        # print(fileName)
        file = open(fileName, 'r', encoding="UTF-8")
        code = file.read()
        # print(code)
        self.__textCode.insert(END, code)
        file.close()

myIDE = WindowIDE()


"""root = Tk()
root.geometry('1400x800')
root.title('TagaPlate IDE')

iconButtonSave = PhotoImage(file='Save_1.png')
iconButtonOpen=PhotoImage(file="open.png")
iconButtonRun=PhotoImage(file="run.png")

scroll=scroll=Scrollbar(root, orient='vertical')
scroll.pack(side=RIGHT, fill='y')

lblCode = Label(root, text="Code")
lblCode.place(x=500,y=5)

textCode = Text(root,height=35, width=130,background="#3d3f42",foreground="#ffffff")
scroll.config(command=textCode.yview)
textCode.place(x=5,y=40)


lblErrors = Label(root, text="Errors")
lblErrors.place(x=1220,y=5)

textErrors = Text(root,height=35, width=40,background="#3d3f42",foreground="#ffffff")
textErrors.place(x=1065,y=40)

lblTerminal = Label(root, text="Terminal")
lblTerminal.place(x=5, y=607)

saveButton=Button(root, text="save", image=iconButtonSave, width="30", height="30", command=saveFile)
saveButton.place(x=0,y=0)
openFileButton=Button(root,text="open", image=iconButtonOpen,width="30",height="30", command=openFile)
openFileButton.place(x=35,y=0)
runButton=Button(root,text="run",image=iconButtonRun, width="30",height="30" )
runButton.place(x=70,y=0)


textTerminal = Text(root,height=10, width=173,background="#3d3f42",foreground="#ffffff")
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


root.mainloop()"""
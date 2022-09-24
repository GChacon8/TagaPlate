from ast import operator
import codecs
from msilib.schema import Condition
from operator import truediv
from types import NoneType
from expresion import ExpresionConcatenar, Valor
from instrucciones import *
from tabla import *
from process import *
from LexicalAnalyzer import *
ts=Tabla_Of_Simbols()
import SintacticAnalyzer as AST
import os
import subprocess

#f = open("./entrada.txt", "r")
#input = f.read()

contIdent = 1


code  = "import pyfirmata\nfrom time import sleep\n\ndef start():\n\tglobal pin8, pin9, pin10\n\tboard=pyfirmata.Arduino('COM3')\n\titer8 = pyfirmata.util.Iterator(board)\n\titer8.start()\n\tpin8 = board.get_pin('d:8:s')\n\tpin9 = board.get_pin('d:9:s')\n\tpin10 = board.get_pin('d:10:s')\n\tpin8.write(0)\n\tsleep(1)\n\tpin9.write(90)\n\tsleep(1)\n\tpin10.write(90)\n\tsleep(1)\n\ndef MoveLeft():\n\tsleep(1)\n\tfor i in range(0,90):\n\t\tpin8.write(i)\n\ndef MoveLeft():\n\tsleep(1)\n\tfor i in range(0,180):\n\t\tpin8.write(i)\n\ndef MoveRight():\n\tsleep(1)\n\tfor i in range(180,1,-1):\n\t\tpin8.write(i)\n\ndef Hammer(pos):\n\tif pos == \"N\":\n\t\tfor i in range(90,130):\n\t\t\tpin9.write(i)\n\t\tfor i in range(130,90,-1):\n\t\t\tpin9.write(i)\n\t\tsleep(1)\n\telif pos == \"S\":\n\t\tfor i in range(90,50,-1):\n\t\t\tpin9.write(i)\n\t\tfor i in range(50,90):\n\t\t\tpin9.write(i)\n\t\tsleep(1)\n\telif pos == \"E\":\n\t\tfor i in range(90,130):\n\t\t\tpin10.write(i)\n\t\tfor i in range(130,90,-1):\n\t\t\tpin10.write(i)\n\t\tsleep(1)\n\telif pos == \"O\":\n\t\tfor i in range(90,50,-1):\n\t\t\tpin10.write(i)\n\t\tfor i in range(50,90):\n\t\t\tpin10.write(i)\n\t\tsleep(1)\n\telse:\n\t\tprint(\"Error\")\n\n" # STRING THAT CONTAINS ALL THE FUTURE .PY FILE

def validar_Principal(instrucciones):
    for i in instrucciones:
        if type(i)==Main:
            return True
    return False


def procesar_instrucciones(instrucciones, ts):
    for i in instrucciones:
        print("ACTUAL ", i)
        if isinstance(i, Values) : procesar_Values(i, ts)
        elif isinstance(i, Process) : procesar_Proces(i, ts)
        elif isinstance(i, Alter) : procesar_Alter(i, ts)
        elif isinstance(i, AlterB) : procesar_AlterB(i, ts)
        elif isinstance(i, MoveRight) : procesar_MoveRight(i, ts)
        elif isinstance(i, MoveLeft) : procesar_MoveLeft(i, ts)
        elif isinstance(i, Hammer) : procesar_Hammer(i, ts)
        elif isinstance(i, Stop) : procesar_Stop(i, ts)
        elif isinstance(i, IsTrue) : procesar_IsTrue(i, ts)
        elif isinstance(i, Repeat) : procesar_Repeat(i, ts)
        elif isinstance(i, Until) : procesar_Until(i, ts)
        elif isinstance(i, While) : procesar_While(i, ts)
        elif isinstance(i, Case) : procesar_Case(i, ts)
        elif isinstance(i, CaseWhen) : procesar_CaseWhen(i, ts)
        elif isinstance(i, PrintValues) : procesar_PrintValues(i, ts)
        elif isinstance(i, When) : procesar_When(i, ts)
        elif isinstance(i, CaseWhenElse): procesar_CaseWhenElse(i,ts)
        else : procesar_declaracion(i, ts)

         
def procesar_funciones(instrucciones, ts):
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr,Main): procesar_Principal(instr,ts)
        elif isinstance(instr, Process) : procesar_Proces(instr, ts)
        else : print('Error: instrucción no válida')
       
def procesar_Principal(instr,ts):
    global code, contIdent

    code += "def principal():\n"

    for i in instr.instrucciones:
        if isinstance(i, Values) : procesar_Values(i, ts)
        elif isinstance(i, Process) : procesar_Proces(i, ts)
        elif isinstance(i, Alter) : procesar_Alter(i, ts)
        elif isinstance(i, AlterB) : procesar_AlterB(i, ts)
        elif isinstance(i, MoveRight) : procesar_MoveRight(i, ts)
        elif isinstance(i, MoveLeft) : procesar_MoveLeft(i, ts)
        elif isinstance(i, Hammer) : procesar_Hammer(i, ts)
        elif isinstance(i, Stop) : procesar_Stop(i, ts)
        elif isinstance(i, IsTrue) : procesar_IsTrue(i, ts)
        elif isinstance(i, Repeat) : procesar_Repeat(i, ts)
        elif isinstance(i, Until) : procesar_Until(i, ts)
        elif isinstance(i, While) : procesar_While(i, ts)
        elif isinstance(i, Case) :  procesar_Case(i, ts)
        elif isinstance(i, CaseWhen) : procesar_CaseWhen(i, ts)
        elif isinstance(i, PrintValues) : procesar_PrintValues(i, ts)
        elif isinstance(i, When) : procesar_When(i, ts)
        elif isinstance(i, CaseWhenElse): procesar_CaseWhenElse(i,ts)
        else : procesar_declaracion(i, ts)

def procesar_declaracion(instr, ts):
    global code, contIdent
    global contIdent
    #print("Instr ", instr.id, instr.type, instr.valor.valor)
    varName = instr.id[1:] 
    code += contIdent*"\t" + varName + " = " + instr.valor.valor + "\n"
def procesar_Values(instr, ts):
    global code, contIdent

    varName = instr.id[1:]
    if isinstance(instr.valor.valor, int) or isinstance(instr.valor.valor, bool):
        code += contIdent*"\t" + varName + " = " + instr.valor.valor + "\n"
    elif isinstance(instr.valor.valor, Alter):
        procesar_Alter(instr.valor.valor, ts)
    else:
        procesar_AlterB(instr.valor.valor, ts)

def procesar_Alter(instr, ts):
    global code, contIdent 
    varName = instr.id[1:]
    operacion = ""
    if instr.operador == "ADD":
        operacion = "+"
    elif instr.operador == "SUB":
        operacion = "-"
    elif instr.operador == "MUL":
        operacion = "*"
    else:
        operacion = "/"
    code += contIdent*"\t" + varName + " " + operacion + "= " + instr.valor.valor + "\n"

def procesar_AlterB(instr, ts):
    global code, contIdent
    varName = instr.id[1:]
    code += contIdent*"\t"+varName+" = " + "not" + varName + "\n"


def procesar_MoveRight(instr, ts):
    global code, contIdent
    code += contIdent*"\t"+"MoveRight()\n"

def procesar_MoveLeft(instr, ts):
    global code, contIdent
    code += contIdent*"\t"+"MoveLeft()\n"

def procesar_Hammer(instr, ts):
    global code, contIdent
    varPosicion = instr.position
    if varPosicion == 'N' or varPosicion == 'S' or varPosicion == "E" or varPosicion == "O":
        code += contIdent*"\t"+"Hammer(\""+varPosicion+"\")\n"

def procesar_Stop(instr, ts):
    global code, contIdent
    code += contIdent*"\t"+"print(\"Para\") \n"

def procesar_IsTrue(id, ts):
    global code, contIdent
    if id:
        code += "True"
    else:
        code += "False\n" 

def procesar_Repeat(instr, ts):
    global code, contIdent
    code += contIdent*"\t"+"while True:\n"
    contIdent += 1
    procesar_instrucciones(instr.instrucciones, ts)
    contIdent -= 1

def procesar_Until(instr, ts):
    global code, contIdent
    instrucciones = instr.instrucciones
    code += contIdent*"\t"+"while True:\n"
    contIdent += 1
    procesar_instrucciones(instrucciones, ts)

    code += contIdent*"\t"+"if "
    if isinstance(instr.condicion,IsTrue):
        procesar_IsTrue(instr.condicion,ts)
        code += ":\n"
    else:
        code += instr.condicion+":\n" + "break"
    contIdent += 1
    procesar_instrucciones(instrucciones, ts)
    contIdent -= 2
    
def procesar_While(instr, ts):
     global code, contIdent
     code += contIdent*"\t"+"while "
     instrucciones = instr.instrucciones

     if isinstance(instr.condicion,IsTrue):
        procesar_IsTrue(instr.condicion,ts)
        code += ":\n"
     else:
        code += instr.condicion+":\n"
     contIdent += 1
     procesar_instrucciones(instrucciones, ts)
     contIdent -= 1

def procesar_CaseWhen(instr, ts):
    global code, contIdent
    condicion = instr.condicion
    code += contIdent*"\t"+"if "
    if isinstance(instr.condicion,IsTrue):
        procesar_IsTrue(instr.condicion,ts)
        code += ":\n"
    else:
        contIdent +=1
        code += instr.condicion.num1[1:]+instr.condicion.operador+instr.condicion.num2+":\n"
        contIdent -= 1
    contIdent += 1
    procesar_instrucciones(instr.instrucciones1, ts)
    contIdent -= 1

def procesar_CaseWhenElse(instr,ts):
    global code, contIdent
    condicion = instr.condicion
    code += contIdent*"\t"+"if "
    if isinstance(instr.condicion,IsTrue):
        procesar_IsTrue(instr.condicion,ts)
        code += ":\n"
    else:
        code += instr.condicion+":\n"
    contIdent += 1
    procesar_instrucciones(instr.instrucciones1, ts)
    contIdent -= 1
    code += contIdent*"\t"+"else:\n"
    contIdent +=1
    procesar_instrucciones(instr.instrucciones2, ts)
    contIdent +=1
    

def procesar_PrintValues(instr, ts):
    global code, contIdent
    #list=[]
    #print(instr.valor)
    def concatenar(texto,valores):
        print("Valor actual",valores)
        if isinstance(valores,str):
            texto += valores
            return texto
        elif isinstance(valores,NoneType):
            return ""
        
        elif isinstance(valores,ExpresionConcatenar):
            if isinstance(valores.dato1,str):
                texto += valores.dato1+","
                return concatenar(texto,valores.dato2)
            elif isinstance(valores.dato2,ExpresionConcatenar):
                return concatenar(texto,valores.dato2)
            else:
                #print("hola",valores.dato2)
                texto += valores.dato2
                return texto

    impresion = concatenar("",instr.valor)
    code +=contIdent*"\t"+"print("+impresion+")\n"
    

def procesar_Case(instr, ts): # varName, value, instr
    global code, contIdent
    #for i in instr.instrucciones:
    procesar_instrucciones(instr, ts) 

def procesar_WhenOptions(instr, ts):
    global code, contIdent
    varName = instr.id[1:]
    value = instr.value
    instructions = instr.instrucciones
    if isinstance(instr,IsTrue):
        procesar_IsTrue(instr.condicion,ts)

    code += contIdent*"\t"+"if" + varName + "==" + value + ":\n"
    contIdent += 1
    procesar_instrucciones(instr.instrucciones, ts)
    contIdent -=1

def procesar_When(instr, ts):
    global code, contIdent
    variable = instr.variable
    valor = instr.valor
    code += contIdent*"\t"+"if "+variable+"=="+valor+":\n"
    contIdent += 1
    procesar_instrucciones(instr.instrucciones, ts)
    contIdent -= 1

def procesar_Proces(instr, ts):
    global code, contIdent
    functionName = instr.id[1:]
    contIdent = 1

    code += "def " + functionName + "():\n"

    for i in instr.instrucciones:
        if isinstance(i, Values) : procesar_Values(i, ts)
        elif isinstance(i, Process) : procesar_Proces(i, ts)
        elif isinstance(i, Alter) : procesar_Alter(i, ts)
        elif isinstance(i, AlterB) : procesar_AlterB(i, ts)
        elif isinstance(i, MoveRight) : procesar_MoveRight(i, ts)
        elif isinstance(i, MoveLeft) : procesar_MoveLeft(i, ts)
        elif isinstance(i, Hammer) : procesar_Hammer(i, ts)
        elif isinstance(i, Stop) : procesar_Stop(i, ts)
        elif isinstance(i, IsTrue) : procesar_IsTrue(i, ts)
        elif isinstance(i, Repeat) : procesar_Repeat(i, ts)
        elif isinstance(i, Until) : procesar_Until(i, ts)
        elif isinstance(i, While) : procesar_While(i, ts)
        elif isinstance(i, Case) : procesar_Case(i, ts)
        elif isinstance(i, CaseWhen) : procesar_CaseWhen(i, ts)
        elif isinstance(i, PrintValues) : procesar_PrintValues(i, ts)
        elif isinstance(i, When) : procesar_When(i, ts)
        elif isinstance(i, WhenOptions) : procesar_WhenOptions(i, ts)
        elif isinstance(i, CaseWhenElse): procesar_CaseWhenElse(i,ts)
        else : procesar_declaracion(i, ts)


def procesar(Condicion,ts,instruccionesl):
    if Condicion==True:
        procesar_funciones(instruccionesl,ts)
    else:
        print("no existe la funcion principal")



def makeSemantic(myFile):
    file = myFile
    lexTable = returnLexTable(file)

    for i in lexTable:
        ts.agregar(Simbolo(i.type, i.type, i.value))

    print("\n", ts.simbols)
    fp = codecs.open(file)
    cadena = fp.read()
    fp.close()

    instruccionesl=AST.parseM(cadena)

    procesar(validar_Principal(instruccionesl),ts,instruccionesl)

code += "start()\n"

lastOpened = ""
def crearArchivo(file):
    global code 
    code += "principal()"
    #print(code)
    file = open("src/PruebaCode.py","w")
    file.write(code)
    file.close()

def ejecutarArchivo(file=lastOpened):
    os.chdir("src/")
    subprocess.run("PruebaCode.py", shell=True)
    os.chdir("../")

def compilacion(file):
    makeSemantic(file)
    crearArchivo(file.split("/")[-1].split(".")[0])
#print(os.getcwd().split("\\")[-1])
compilacion("src/TestsFiles/Untitled.tgp")
ejecutarArchivo()
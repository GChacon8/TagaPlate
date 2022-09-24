from ast import operator
import codecs
from msilib.schema import Condition
from operator import truediv
from expresion import Valor
from instrucciones import *
from tabla import *
from process import *
from LexicalAnalyzer import *
ts=Tabla_Of_Simbols()
import SintacticAnalyzer as AST
import os

#f = open("./entrada.txt", "r")
#input = f.read()

contIdent = 1

file = 'src/TestsFiles/Untitled.tgp'
lexTable = returnLexTable(file)

for i in lexTable:
    ts.agregar(Simbolo(i.type, i.type, i.value))

print("\n", ts.simbols)
fp = codecs.open(file)
cadena = fp.read()
fp.close()

instruccionesl=AST.parseM(cadena)


code  = "from pyfirmata import Arduino, SERVO, util\nfrom time import sleep\nport=\"COM3\"\nboard = Arduino(port)\n" # STRING THAT CONTAINS ALL THE FUTURE .PY FILE

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
        elif isinstance(i, Case) : procesar_Case(i, ts)
        elif isinstance(i, CaseWhen) : procesar_CaseWhen(i, ts)
        elif isinstance(i, PrintValues) : procesar_PrintValues(i, ts)
        elif isinstance(i, When) : procesar_When(i, ts)
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
        code += contIdent*"\t"+"Hammer("+varPosicion+")\n"

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

def procesar_Case(instr, ts):
    global code, contIdent
    varName = instr.id
    print("Instrucciones ", instr)
    procesar_instrucciones(instr.instrucciones, ts)

def procesar_CaseWhen(instr, ts):
    global code, contIdent
    valor = instr.valor.valor
    if valor:
        procesar_instrucciones(instr.instrucciones1, ts)
    else:
        procesar_instrucciones(instr.instrucciones2, ts)

def procesar_PrintValues(instr, ts):
    global code, contIdent
    impresion = instr.valor
    code += contIdent*"\t"+"print("+impresion+")"

def procesar_When(instr, ts):
    global code, contIdent
    variable = instr.variable
    valor = instr.valor
    code += "if "+variable+"=="+valor+":\n"
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
        else : procesar_declaracion(i, ts)


def procesar(Condicion,ts,instruccionesl):
    if Condicion==True:
        procesar_funciones(instruccionesl,ts)
    else:
        print("no existe la funcion principal")


procesar(validar_Principal(instruccionesl),ts,instruccionesl)

print(code)
file = open("src/PruebaCode.py","w")
file.write(code)
file.close()

#print(instruccionesl)
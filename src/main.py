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

#f = open("./entrada.txt", "r")
#input = f.read()


file = 'src/TestsFiles/Untitled.tgp'
lexTable = returnLexTable(file)

for i in lexTable:
    ts.agregar(Simbolo(i.type, i.type, i.value))

print("\n", ts.simbols)
fp = codecs.open(file)
cadena = fp.read()
fp.close()

instruccionesl=AST.parse(cadena)
print(instruccionesl)

code  = "" # STRING THAT CONTAINS ALL THE FUTURE .PY FILE

def validar_Principal(instrucciones):
    for i in instrucciones:
        if type(i)==Main:
            return True
        else:
            return False




         
def procesar_instrucciones(instruccionesl, ts):
    ## lista de instrucciones recolectadas
    
        
    for instr in instruccionesl :
        if isinstance(instr,Main): procesar_Principal(instr,ts)
        elif isinstance(instr, Values) : procesar_Values(instr, ts)
        elif isinstance(instr, Process) : procesar_Proces(instr, ts)
        elif isinstance(instr, Alter) : procesar_Alter(instr, ts)
        elif isinstance(instr, AlterB) : procesar_AlterB(instr, ts)
        elif isinstance(instr, MoveRight) : procesar_MoveRight(instr, ts)
        elif isinstance(instr, MoveLefth) : procesar_MoveLeft(instr, ts)
        elif isinstance(instr, Hammer) : procesar_Hammer(instr, ts)
        elif isinstance(instr, Stop) : procesar_Stop(instr, ts)
        elif isinstance(instr, IsTrue) : procesar_IsTrue(instr, ts)
        elif isinstance(instr, Repeat) : procesar_Repeat(instr, ts)
        elif isinstance(instr, Until) : procesar_Until(instr, ts)
        elif isinstance(instr, While) : procesar_While(instr, ts)
        elif isinstance(instr, Case) : procesar_Case(instr, ts)
        elif isinstance(instr, CaseWhen) : procesar_CaseWhen(instr, ts)
        elif isinstance(instr, PrintValues) : procesar_PrintValues(instr, ts)
        elif isinstance(instr, When) : procesar_When(instr, ts)
        else : print('Error: instrucción no válida')
       
def procesar_Principal(instr,ts):
    global code

    code += "def principal():\n"

    for i in instr.instrucciones:
        if isinstance(i, Values) : procesar_Values(i, ts)
        elif isinstance(i, Process) : procesar_Proces(i, ts)
        elif isinstance(i, Alter) : procesar_Alter(i, ts)
        elif isinstance(i, AlterB) : procesar_AlterB(i, ts)
        elif isinstance(i, MoveRight) : procesar_MoveRight(i, ts)
        elif isinstance(i, MoveLefth) : procesar_MoveLeft(i, ts)
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
    global code
    #print("Instr ", instr.id, instr.type, instr.valor.valor)
    varName = instr.id[1:] 
    code += "\t" + varName + " = " + instr.valor.valor + "\n"

def procesar_Values(instr, ts):
    global code

    varName = instr.id[1:]
    if isinstance(instr.valor.valor, int) or isinstance(instr.valor.valor, bool):
        code += "\t" + varName + " = " + instr.valor.valor + "\n"
    elif isinstance(instr.valor.valor, Alter):
        procesar_Alter(instr.valor.valor, ts)
    else:
        procesar_AlterB(instr.valor.valor, ts)

def procesar_Alter(instr, ts):
    global code 
    varName = instr.id[1:]
    code += "\t" + varName + instr.operator + "= " + instr.valor.valor + "\n"

def procesar_AlterB(instr, ts):
    global code
    varName = instr.id[1:]
    code += "\t" + varName + "= " + "not " + varName + "\n"

def procesar_MoveRight(instr, ts):
    global code
    code += "\t board.digital[pin].write(grados)\n sleep(3000)\n"

def procesar_MoveLeft(instr, ts):
    global code
    code += "\t board.digital[pin].write(-grados)\n sleep(3000)\n"

def procesar_Hammer(instr, ts):
    global code
    code += "\t board.digital[pin].write(grados)\n sleep(6000)\n"

def procesar_Stop(instr, ts):
    pass 

def procesar_IsTrue(instr, ts):
    global code
    varName = instr.id[1:]
    if instr.valor.valor:
        code += "\t return True \n"
    else:
        code += "\t return False \n" 

def procesar_Repeat(instr, ts):
    global code
    procesar_instrucciones(instr.instrucciones, ts)

def procesar_Until(instr, ts):
    global code
    condicion = instr.condicion[1:]
    instrucciones = instr.instrucciones
    while not condicion:
        procesar_instrucciones(instrucciones, ts)

def procesar_While(instr, ts):
   global code
   valor = instr.valor.valor
   while valor:
    procesar_instrucciones(instr.instrucciones, ts)

def procesar_Case(instr, ts):
    global code
    procesar_instrucciones(instr.instrucciones, ts)

def procesar_CaseWhen(instr, ts):
    global code
    valor = instr.valor.valor
    if valor:
        procesar_instrucciones(instr.instrucciones1, ts)
    else:
        procesar_instrucciones(instr.instrucciones2, ts)

def procesar_PrintValues(instr, ts):
    global code
    impresion = instr.valor.valor
    code += "print("+impresion+")"

def procesar_When(instr, ts):
    global code
    valor = instr.valor.valor
    if valor:
        procesar_instrucciones(instr.instrucciones, ts)


def resolver_expresion_logica(expresion,ts):
    pass
def procesar_Proces(instr, ts):
    print("move proces")


def procesar(Condicion,ts,instruccionesl):
    if Condicion==True:
        procesar_instrucciones(instruccionesl,ts)
    else:
        print("no existe la funcion principal")


procesar(validar_Principal(instruccionesl),ts,instruccionesl)
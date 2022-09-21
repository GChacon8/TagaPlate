import codecs
from operator import truediv
from instrucciones import *
from tabla import *
from process import *
ts=Tabla_Of_Simbols()

#f = open("./entrada.txt", "r")
#input = f.read()


file = 'src/TestsFiles/Untitled.tgp'
fp = codecs.open(file)
cadena = fp.read()
fp.close()
import SintacticAnalyzer as AST
instruccionesl=AST.parse(cadena)
print(instruccionesl)


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
    for i in instr.instrucciones:
        if isinstance(i,MoveRight):
            print("mover dercho")



def procesar_Values(instr, ts):
    pass

def procesar_Alter(instr, ts):
    pass

def procesar_AlterB(instr, ts):
    pass

def procesar_MoveRight(instr, ts):
    print("hola")

def procesar_MoveLeft(instr, ts):
    pass

def procesar_Hammer(instr, ts):
    pass 

def procesar_Stop(instr, ts):
    pass 

def procesar_IsTrue(instr, ts):
    pass 

def procesar_Repeat(instr, ts):
    pass 

def procesar_Until(instr, ts):
    pass 

def procesar_While(instr, ts):
    while resolver_expresion_logica(instr.condicion, ts):
        ts_local = Tabla_Of_Simbols(ts.simbols)
        procesar_instrucciones(instr.intrucciones, ts_local)

def procesar_Case(instr, ts):
    pass 

def procesar_CaseWhen(instr, ts):
    pass

def procesar_PrintValues(instr, ts):
    pass 

def procesar_When(instr, ts):
    pass


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
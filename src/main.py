import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *

def procesar_instrucciones(instrucciones, ts):
    ## lista de instrucciones recolectadas
    for instr in instrucciones :
        if isinstance(instr, Values) : procesar_Values(instr, ts)
        elif isinstance(instr, Alter) : procesar_Alter(instr, ts)
        elif isinstance(instr, AlterB) : procesar_AlterB(instr, ts)
        elif isinstance(instr, MoveRight) : procesar_MoveRight(instr, ts)
        elif isinstance(instr, MoveLeft) : procesar_MoveLeft(instr, ts)
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


def procesar_Values(instr, ts):
    pass

def procesar_Alter(instr, ts):
    pass

def procesar_AlterB(instr, ts):
    pass

def procesar_MoveRight(instr, ts):
    pass

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
    while resolver_expresion_logica(instr.expLogica, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.intrucciones, ts_local)

def procesar_Case(instr, ts):
    pass 

def procesar_CaseWhen(instr, ts):
    pass

def procesar_PrintValues(instr, ts):
    pass 

def procesar_When(instr, ts):
    pass

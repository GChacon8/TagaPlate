# El Parser/analizador sintáctico se encarga de reconocer la estructura de los bloques de código

from unittest import result
import ply.yacc as yacc
import os
import codecs
import re
from sys import stdin
from LexicalAnalyzer import tokens
from process import *
from instrucciones import *
from expresion import *

# PRECEDENCIA: SABER DE QUÉ LADO ANALIZAR A LOS TOKENS SIGUIENTES DE LOS MENCIONADOS AQUÍ

precedence = (
    ('right', 'New'),
    ('left', 'Less','LessEqual', 'Greater', 'GreaterEqual', 'Equals', 'Different'),
    ('right','LPARENTHESIS','RPARENTHESIS')
)


# PENDIENTE 3: modificar el archivo del IDE para que el Lexer ya no sea una clase
# PENDIENTE 4: incluir el token TEXTVALUE (valores de texto, o sea strings) para probarlo en la funcion PrintValues (SIN ESA FUNCION EL PROYECTO VALE CERO)


# RECONOCIMIENTO DE FUNCIONES Y LOS PROC ---------------------------------------------

def p_start(p):
    '''start : main'''
    p[0]=p[1]

"""def p_list_of_instrucciones():"""
def p_main(p):
    '''main :  Proc ID LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM'''
    p[0]=Main(p[4])


def p_Proced(p): # Reconoce los Procedimientos, es decir los: Proc @nombre();
    '''Proced : Proc ID LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM'''
    p[0]=Process(p[2],p[4])
    
    print("Proced ", p[4])



def p_recursivo(p):
    '''recursivo : recursivo instruccion
                 '''
    p[0]=p[1]
def p_recursivo2(p):
    '''recursivo : instruccion'''
    p[0]=p[1]


def p_instruccion(p): # Una instruccion puede ser cualquiera de las sig. funciones
    '''instruccion : varDeclaration 
                     | Values_f
                     | Alter_f
                     | AlterB_f
                     | MoveRight_f
                     | MoveLeft_f
                     | Hammer_f
                     | Stop_f
                     | IsTrue_f
                     | Repeat_f
                     | Until_f
                     | While_f
                     | Case_f
                     | Case2_f
                     | PrintValues_f
                     | call_f
                     | empty'''
    p[0] = p[1]
    print("instruccion ", p[1])    


def p_Values_f(p):
     '''Values_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM'''
     p[0]=Values(p[3],p[5])

def p_valorDato(p):
    '''valorDato : True 
                | False  
                | Number
                | Alert_f
                | Alert_B'''
    p[0] = Valor(p[1])
    print("valorDato ", p[1])


def p_Alter_f(p):       # Altera ligeramente el valor de una variable y retorna dicho valor nuevo
    '''Alter_f : Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM'''

    p[0]=Alter(p[3],p[7])
    print("Alter_f ", p[4])

def p_AlterB_f(p):      # Altera el valor de una variables booleana (Alter_f pero solo con True y False) y retorna dicho valor nuevo
    '''AlterB_f : AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
    p[0]=AlterB(p[3])
    print("ALterB_f ", p)

def p_MoveRight_f(p):
    '''MoveRight_f : MoveRight SEMMICOLOM'''
    p[0]=p[1]
    print("MoveRight_f", p)

def p_MoveLeft_f(p):
    '''MoveLeft_f : MoveLeft SEMMICOLOM'''
    p[0]=p[1]
    print("MoveLeft_f", p)

def p_Hammer_f(p):
    '''Hammer_f : Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM
                 | Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM 
                 | Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM
                 | Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOM'''
    p[0]=Hammer(p[3])
    print("Hammer_f", p[3])

def p_Stop_f(p):
    '''Stop_f : Stop SEMMICOLOM'''
    p[0]=p[0]
    print("Stop_f", p)

def p_Repeat_f(p):
    '''Repeat_f : Repeat LPARENTHESIS recursivo Break RPARENTHESIS SEMMICOLOM'''
    p[0]=Repeat(p[3])
    print("Repeat_f", p)

def p_Until_f(p):
    '''Until_f : Until LPARENTHESIS recursivo RPARENTHESIS condicional SEMMICOLOM'''
    p[0]=Until(p[3])
    print("Until_f", p)

def p_While_f(p):
    '''While_f : While condicional LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM'''
    p[0]=While(p[2],p[4])
    print("While_f", p)

def p_Case_f(p):
    '''Case_f : Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM
              | Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS Else LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM'''
    print("Case_f ", p)

def p_opciones(p): # otra funcion recursiva para permitir varios "When ... Then"
    '''opciones : opciones When valorDato Then LPARENTHESIS recursivo RPARENTHESIS
                | When valorDato Then LPARENTHESIS recursivo RPARENTHESIS'''

def p_Case2_f(p):
    '''Case2_f : Case ID opciones SEMMICOLOM
                | Case ID opciones Else recursivo SEMMICOLOM '''

# something engloba a los ID de variables, valores de texto entre comillas(QUOTES) y numeros. 
# El PrintValues puede imprimir varias cosas a la vez, por eso se incluye la posiblidad de poner coma (,)"

#                  | QUOTES TEXTVALUE QUOTES COMMA something
 #                | QUOTES TEXTVALUE QUOTES                          incluir esas 2 cuando ya sirva el token TEXTVALUE y QUOTES

def p_something(p): 
    '''something : ID COMMA something
                 | expresionNum COMMA something
                 | expresionNum
                 | Number COMMA something
                 | Number
                 | empty'''
    

def p_PrintValues_f(p):
    '''PrintValues_f : PrintValues LPARENTHESIS something RPARENTHESIS SEMMICOLOM'''
    p[0]=PrintValues(p[3])

    print("PrintValues ", p)

def p_empty(p):
    '''empty : '''
    print("Empty! ", p)
    pass

# RECONOCIMIENTO DE CONDICIONALES ------------------------------------------
        # estas son importantes para definir condiciones de finalización en funciones como: Until, While y Case When

def p_condicional_f(p):
    '''condicional : IsTrue_f
                   | Greater_f
                   | GreaterEqual_f
                   | Equals_f
                   | Different_f
                   | LessEqual_f
                   | Less_f'''
    print("condicional ", p)

def p_IsTrue_f(p):
    '''IsTrue_f : IsTrue ID SEMMICOLOM'''
    p[0]=IsTrue(p[2])
    print("IsTrue_f", p)

def p_Greater_f(p):
    '''Greater_f : expresionNum Greater expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.GREATER,p[3])

    print("Greater_f", p)

def p_GreaterEqual_f(p):
    '''GreaterEqual_f : expresionNum GreaterEqual expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.GREATEREQUAL,p[3])
    print("GreaterEqual", p)

def p_Equals_f(p):
    '''Equals_f : expresionNum Equals expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.EQUAL,p[3])
    print("Equals", p)

def p_Different_f(p):
    '''Different_f : expresionNum Different expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.DIFFERENT,p[3])
    print("Different_f:", p)

def p_LessEqual_f(p):
    '''LessEqual_f : expresionNum LessEqual expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.LESSEQUAL,p[3])
    print("LessEquals", p)

def p_Less_f(p):
    '''Less_f : expresionNum Less expresionNum SEMMICOLOM'''
    p[0]=Binar_Expression(p[1],OperationL.LESS,p[3])
    print("Less_f :", p)
    

# RECONOCIMIENTO DE VARIABLES---------------------------------------------------------

def p_varDeclaration(p):
    '''varDeclaration : New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM '''
    #p[0] = var(p[5], p[7], "var")
    p[0]=Assigment(p[2],p[5],p[7])
    print("varDeclaration ", p[2])

def p_expresionNum(p): # una expresion numerica puede ser el valor de una variable o el resultado de la funcion Alter
    '''expresionNum : ID
                     | Alter_f '''
    print("expresionNum ", p[1])

def p_tipoDatos(p):
    '''tipoDatos : Bool
                 | Num'''
    p[0] = p[1]
    print("tipoDato ", p[1])

def p_valorDato(p):
    '''valorDato : True 
                | False  
                | Number'''
    #p[0] = p[1]
    print("valorDato ", p[1])










"""def p_Values_f(p):      # Cambia el valor de una variable
    '''Values_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM
               '
    print("Values_f", p[2])"""
# LLAMAR A UNA FUNCIÓN ---------------------------------------------------------------

def p_call_f(p):
    '''call_f : CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
    p[0]=Call(p[3])
    print("call_f ", p)

# RECONOCIMIENTO DE ERRORES LÉXICOS --------------------------------------------------

def p_error(p):
     print("\nSyntax error in input! ", p)






# PRUEBA DEL PARSER EN UN ARCHIVO ----------------------------------------------------

print("\n")
file = 'src/TestsFiles/Untitled.tgp'
fp = codecs.open(file)
cadena = fp.read()
parser = yacc.yacc()
fp.close()
result=parser.parse(cadena)
#result.imprimir("")
#print result
"""
fileNew=open("semanticTree.vz","w")
fileNew.write(result.transalte())
fileNew.close()"""

print("\nParser.parse(cadena) =  " + str(parser.parse(cadena)) + "\n")

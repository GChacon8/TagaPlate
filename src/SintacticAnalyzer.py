# El Parser/analizador sintáctico se encarga de reconocer la estructura de los bloques de código

from unittest import result
import ply.yacc as yacc
import os
import codecs
import re
from sys import stdin
from LexicalAnalyzer import tokens

# PRECEDENCIA: SABER DE QUÉ LADO ANALIZAR A LOS TOKENS SIGUIENTES DE LOS MENCIONADOS AQUÍ

precedence = (
    ('right', 'New'),
    ('left', 'Less','LessEqual', 'Greater', 'GreaterEqual', 'Equals', 'Different'),
    ('right','LPARENTHESIS','RPARENTHESIS')
)


# PENDIENTE 1: definir Scopes para las funciones y que asi el parser me reconozca N cantidad de instrucciones dentro de las funciones
# PENDIENTE 2: definir qué es una 'expresion' para incluirla en las condicionales booleanas y en las funciones que utilizan esas condicionales
# PENDIENTE 3: modificar el archivo del IDE para que el Lexer ya no sea una clase
# PENDIENTE 4: incluir el token TEXTVALUE (valores de texto, o sea strings) para probarlo en la funcion PrintValues (SIN ESA FUNCION EL PROYECTO VALE CERO)

# RECONOCIMIENTO DE FUNCIONES Y LOS PROC ---------------------------------------------

def p_Proced(p):        # Reconoce los Procedimientos, es decir los: Proc @nombre();
    '''Proced : Proc PRINCIPAL LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM
              '''
    print("Proced ", p[4])
    # p[0]=Proced(p[1],"Proced")
def p_recursivo(p):
    '''recursivo : recursivo instruccion
                    | instruccion'''
    pass




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
                     | PrintValues_f
                     | empty'''
    p[0] = p[1]
    print("instruccion ", p[1])    

def p_Values_f(p):      # Cambia el valor de una variable
    '''Values_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM
                | LPARENTHESIS ID COMMA Alter_f RPARENTHESIS SEMMICOLOM'''
    print("Values_f", p[2])

def p_Alter_f(p):       # Altera ligeramente el valor de una variable
    '''Alter_f : Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM'''
    print("Alter_f ", p[4])

def p_AlterB_f(p):      # Altera el valor de una variables booleana (Alter_f pero solo con True y False)
    '''AlterB_f : AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
    print("ALterB_f ", p)

def p_MoveRight_f(p):
    '''MoveRight_f : MoveRight '''
    print("MoveRight_f", p)

def p_MoveLeft_f(p):
    '''MoveLeft_f : MoveLeft '''
    print("MoveLeft_f", p)

def p_Hammer_f(p):
     '''Hammer_f : Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM
                 | Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM 
                 | Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM
                 | Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOM'''
     print("Hammer_f", p[3])

def p_Stop_f(p):
    '''Stop_f : Stop SEMMICOLOM'''
    print("Stop_f", p)

def p_IsTrue_f(p):
    '''IsTrue_f : IsTrue ID SEMMICOLOM'''
    print("IsTrue_f", p)

def p_Repeat_f(p):
    '''Repeat_f : Repeat LPARENTHESIS instruccion Break SEMMICOLOM RPARENTHESIS SEMMICOLOM'''
    print("Repeat_f", p)

def p_Until_f(p):
    '''Until_f : Until LPARENTHESIS instruccion RPARENTHESIS SEMMICOLOM'''
    print("Until_f", p)

def p_While_f(p):
    '''While_f : While LPARENTHESIS instruccion RPARENTHESIS SEMMICOLOM'''
    print("While_f", p)

def p_Case_f(p):
    '''Case_f : Case When LPARENTHESIS RPARENTHESIS Then LPARENTHESIS instruccion RPARENTHESIS SEMMICOLOM
              | Case When LPARENTHESIS RPARENTHESIS Then LPARENTHESIS instruccion RPARENTHESIS Else LPARENTHESIS instruccion RPARENTHESIS SEMMICOLOM'''
    print("Case_f ", p)

def p_PrintValues_f(p):
    '''PrintValues_f : PrintValues LPARENTHESIS RPARENTHESIS SEMMICOLOM'''
    print("PrintValues ", p)

def p_empty(p):
    '''empty : '''
    print("Empty! ", p)
    pass



# RECONOCIMIENTO DE VARIABLES---------------------------------------------------------

def p_varDeclaration(p):
    '''varDeclaration : New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM '''
    #p[0] = var(p[5], p[7], "var")
    print("varDeclaration ", p[2])

def p_tipoDatos(p):
    '''tipoDatos : Bool
                 | Num'''
    #p[0] = p[1]
    print("tipoDato ", p[1])

def p_valorDato(p):
    '''valorDato : True 
                | False  
                | Number'''
    #p[0] = p[1]
    print("valorDato ", p[1])

# definir qué es una expresion 
""""def p_expresion(p):
    '''expresion : '''
"""

# LLAMAR A UNA FUNCIÓN ---------------------------------------------------------------

def p_call_f(p):
    '''call : CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
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
result=parser.parser(cadena)
#result.imprimir("")
#print result
"""
fileNew=open("semanticTree.vz","w")
fileNew.write(result.transalte())
fileNew.close()"""

print("\nParser.parse(cadena) =  " + str(parser.parse(cadena)) + "\n")
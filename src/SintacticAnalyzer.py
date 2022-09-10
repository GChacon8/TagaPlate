# El Parser/analizador sintáctico se encarga de reconocer la estructura de los bloques de código

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

# RECONOCIMIENTO DE FUNCIONES Y LOS PROC ---------------------------------------------

def p_Proced(p):        # Reconoce los Procedimientos, es decir los: Proc @nombre();
    '''Proced : Proc ID LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM
              | Proc PRINCIPAL LPARENTHESIS RPARENTHESIS SEMMICOLOM'''
    print("Proced ", p)

def p_instrucciones(p): # Una instruccion puede ser cualquiera de las sig. funciones
    '''instrucciones : varDeclaration
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
                     
    print("instruccion ", p)    

def p_Values_f(p):      # Cambia el valor de una variable
    '''Values_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM
                | LPARENTHESIS ID COMMA Alter_f RPARENTHESIS SEMMICOLOM'''

def p_Alter_f(p):       # Altera ligeramente el valor de una variable
    '''Alter_f : LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM
               | LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM
               | LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM
               | LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM'''
    print("Alter_f ", p)

def p_AlterB_f(p):      # Altera el valor de una variables booleana (Alter_f pero solo con True y False)
    '''AlterB_f : LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
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
     print("Hammer_f", p)

def p_Stop_f(p):
    '''Stop_f : Stop SEMMICOLOM'''
    print("Stop_f", p)

def p_IsTrue_f(p):
    '''IsTrue_f : IsTrue ID SEMMICOLOM'''
    print("IsTrue_f", p)

def p_Repeat_f(p):
    '''Repeat_f : Repeat LPARENTHESIS instrucciones Break SEMMICOLOM RPARENTHESIS SEMMICOLOM'''
    print("Repeat_f", p)

def p_Until_f(p):
    '''Until_f : Until LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    print("Until_f", p)

def p_While_f(p):
    '''While_f : While LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    print("While_f", p)

def p_Case_f(p):
    '''Case_f : Case When LPARENTHESIS RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM
              | Case When LPARENTHESIS RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS Else LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    print("Case_f ", p)

def p_PrintValues_f(p):
    '''PrintValues_f : PrintValues LPARENTHESIS RPARENTHESIS SEMMICOLOM'''
    print("PrintValues ", p)

def p_empty(p):
    '''empty : '''
    print("Empty! ", p)

# RECONOCIMIENTO DE CONDICIONALES NUMÉRICAS ------------------------------------------

# RECONOCIMIENTO DE CONDICIONALES BOOLEANAS ------------------------------------------

            # estas son importantes para definir condiciones de finalización en funciones como: Until, While y Case When

# RECONOCIMIENTO DE VARIABLES---------------------------------------------------------

def p_varDeclaration(p):
    '''varDeclaration : New ID LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM '''
    #p[0] = var(p[5], p[7], "var")
    print("varDeclaration ", p)

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


# RECONOCIMIENTO DE ERRORES LÉXICOS --------------------------------------------------

def p_error(p):
     print("\nSyntax error in input! ", p)


# PRUEBA DEL PARSER EN UN ARCHIVO ----------------------------------------------------

file = 'src/TestsFiles/Untitled.tgp'
fp = codecs.open(file)
cadena = fp.read()
parser = yacc.yacc()
fp.close()


print("\n", parser.parse(cadena))
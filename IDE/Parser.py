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

def p_Proced(p): # Reconoce los Procedimientos, es decir los: Proc @nombre();
    '''Proced : Proc ID LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM
              | Proc PRINCIPAL LPARENTHESIS RPARENTHESIS SEMMICOLOM'''
    print("Proced ", p)

def p_instrucciones(p): # Una instruccion puede ser cualquiera de las sig. funciones
    '''instrucciones : varDeclaration
                     | Values_f
                     | Alter_f '''
                     
    print("instruccion ", p)    

def p_Values_f(p):
    '''Values_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM
                | LPARENTHESIS ID COMMA Alter_f RPARENTHESIS SEMMICOLOM'''

def p_Alter_f(p):
    '''Alter_f : LPARENTHESIS ID COMMA RPARENTHESIS'''
    print("Alter_f", p)



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

file = './Lex/Untitled.tgp'
fp = codecs.open(file)
cadena = fp.read()
parser = yacc.yacc()
fp.close()


print("\n", parser.parse(cadena))
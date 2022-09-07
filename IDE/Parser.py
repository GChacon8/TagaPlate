from this import d
import ply.yacc as yacc
import os
import codecs
import re
from sys import stdin
from LexicalAnalyzer import tokens


precedence = (
    ('right', 'New'),
    ('left', 'Less','LessEqual', 'Greater', 'GreaterEqual', 'Equals', 'Different'),
    ('right','LPARENTHESIS','RPARENTHESIS')
)


def p_Principal(p):
    '''Principal : Proc PRINCIPAL LPARENTHESIS instrucciones RPARENTHESIS'''
    print("Principal")

def p_instrucciones(p):
    '''instrucciones : var
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
    print("Instrucciones", p)
    


def p_Values_f(p):
    '''Values_f : Values LPARENTHESIS ID COMMA ValorDato RPARENTHESIS SEMMICOLOM
              | LPARENTHESIS ID COMMA Alter_f  RPARENTHESIS SEMMICOLOM'''

def p_var(p):
    '''var : New ID COMMA LPARENTHESIS tipoDatos COMMA ValorDato RPARENTHESIS SEMMICOLOM '''

    #p[0] = var(p[5], p[7], "var")
    print("var")

 
def p_tipoDatos1(p):
    '''tipoDatos : Bool
                | Num'''
    #p[0] = p[1]
    print("TipoDatos1 ", p[1])


def p_ValorDato(p):
    '''ValorDato : True 
            | False  
            | Number'''
    #p[0] = p[1]
    print("Dato ", p[1])


def p_error(p):
     print("Syntax error in input!", p)


file = './Lex/Untitled.tgp'
fp = codecs.open(file)
cadena = fp.read()
parser = yacc.yacc()
fp.close()


print(parser.parse(cadena))
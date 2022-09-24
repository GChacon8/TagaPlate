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

errorMsg = ""
lastLineErr = ""
currentLineErr = ""
backUp = [{}]

precedence = (
    ('right', 'New'),
    ('left', 'Less','LessEqual', 'Greater', 'GreaterEqual', 'Equals', 'Different'),
    ('right','LPARENTHESIS','RPARENTHESIS')
)





# RECONOCIMIENTO DE FUNCIONES Y LOS PROC ---------------------------------------------
def p_start(p):
    '''start : instrucciones
            '''
    p[0]=p[1]

"""def p_list_of_instrucciones():"""
def p_main(p):
    '''main :  Proc PRINCIPAL LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    p[0]=Main(p[4])
    print("MAIN",p[4])

   # print("Tipo de main", type(p[0]))


def p_Proced(p): # Reconoce los Procedimientos, es decir los: Proc @nombre();
    '''Proced : Proc ID LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    p[0]=Process(p[2],p[4])

    print("Proced ", p[4])



def p_list_instrucciones(p):
    '''instrucciones : instrucciones instruccion
                '''
    p[1].append(p[2])
    p[0]=p[1]
def p_one_instruccion(p):
    '''instrucciones : instruccion'''
    p[0]=[p[1]]


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
                     | main
                     | Proced
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
                | Alter_f
                | AlterB_f'''
    p[0] = Valor(p[1])
    print("valorDato ", p[1])


def p_Alter_f(p):       # Altera ligeramente el valor de una variable y retorna dicho valor nuevo
    '''Alter_f : Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM
               | Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM'''

    p[0]=Alter(p[3],p[5], p[7])
    print("Alter_f ", p[4])

def p_AlterB_f(p):      # Altera el valor de una variables booleana (Alter_f pero solo con True y False) y retorna dicho valor nuevo
    '''AlterB_f : AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
    p[0]=AlterB(p[3])
    print("ALterB_f ", p)

def p_MoveRight_f(p):
    '''MoveRight_f : MoveRight SEMMICOLOM'''
    p[0]=MoveRight()
    print("MoveRight_f")

def p_MoveLeft_f(p):
    '''MoveLeft_f : MoveLeft SEMMICOLOM'''
    p[0]=MoveLeft()
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
    '''Repeat_f : Repeat LPARENTHESIS instrucciones Break RPARENTHESIS SEMMICOLOM'''
    p[0]=Repeat(p[3])
    print("Repeat_f", p)

def p_Until_f(p):
    '''Until_f : Until LPARENTHESIS instrucciones RPARENTHESIS condicional'''
    p[0]=Until(p[5],p[3])
    print("Until_f", p)

def p_While_f(p):
    '''While_f : While condicional LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    p[0]=While(p[2],p[4])
    print("While_f", p)

def p_Case0_f(p):
    '''Case_f : Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    p[0] = CaseWhen(p[4],p[8])
    print("Case_f ", p)

def p_Case1_f(p):
    '''Case_f :  Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS Else LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM'''
    p[0] = CaseWhenElse(p[4],p[8],p[12])
    print("Case_f ", p)
    

def p_opciones(p): # otra funcion recursiva para permitir varios "When ... Then"
    '''opciones : opciones When valorDato Then LPARENTHESIS instrucciones RPARENTHESIS
                | When valorDato Then LPARENTHESIS instrucciones RPARENTHESIS'''
    p[0] = When(p[])

def p_opciones(p):
    '''opciones : When valorDato Then LPARENTHESIS instrucciones RPARENTHESIS'''
    p[0] = When()

def p_Case2_f(p):
    '''Case2_f : Case ID opciones SEMMICOLOM'''
    p[0] = Case(p[2],p[3])

def p_CaseElse(p):
    '''CaseElse : Case ID opciones Else instrucciones SEMMICOLOM'''
    #p[0] = 

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
                 | TEXTVALUE COMMA something
                 | TEXTVALUE
                 | empty'''

    p[0]=p[1]

  
def p_something3(p):
    pass
def p_something4(p):
    pass
def p_PrintValues_f(p):
    '''PrintValues_f : PrintValues LPARENTHESIS something RPARENTHESIS SEMMICOLOM '''
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
    p[0]=p[1]

def p_IsTrue_f(p):
    '''IsTrue_f : IsTrue LPARENTHESIS ID RPARENTHESIS SEMMICOLOM
                | IsTrue LPARENTHESIS ID RPARENTHESIS'''
    p[0]=IsTrue(p[3])
    print("IsTrue_f", p)

def p_Greater_f(p):
    '''Greater_f : expresionNum Greater expresionNum SEMMICOLOM
                 | expresionNum Greater expresionNum '''
    p[0]=Binar_Expression(p[1],">",p[3])

    print("Greater_f", p)

def p_GreaterEqual_f(p):
    '''GreaterEqual_f : expresionNum GreaterEqual expresionNum SEMMICOLOM
                        |  expresionNum GreaterEqual expresionNum'''
    p[0]=Binar_Expression(p[1],">=",p[3])
    print("GreaterEqual", p)

def p_Equals_f(p):
    '''Equals_f : expresionNum Equals expresionNum SEMMICOLOM
                | expresionNum Equals expresionNum '''
    p[0]=Binar_Expression(p[1],"<=",p[3])
    print("Equals", p)

def p_Different_f(p):
    '''Different_f : expresionNum Different expresionNum SEMMICOLOM
                    | expresionNum Different expresionNum '''
    p[0]=Binar_Expression(p[1],"<>",p[3])
    print("Different_f:", p)

def p_LessEqual_f(p):
    '''LessEqual_f : expresionNum LessEqual expresionNum SEMMICOLOM
                    | expresionNum LessEqual expresionNum'''
    p[0]=Binar_Expression(p[1],"<=",p[3])
    print("LessEquals", p)

def p_Less_f(p):
    '''Less_f : expresionNum Less expresionNum SEMMICOLOM
              | expresionNum Less expresionNum'''
    p[0]=Binar_Expression(p[1],"<",p[3])
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

# LLAMAR A UNA FUNCIÓN ---------------------------------------------------------------

def p_call_f(p):
    '''call_f : CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'''
    p[0]=Call(p[3])
    print("call_f ", p)

# RECONOCIMIENTO DE ERRORES LÉXICOS --------------------------------------------------

def p_error(p):
    global errorMsg, lastLineErr, backUp

    previous_token = parser.symstack[-1]

    if p:
        currentLineErr = str(p.lineno)

        if type(previous_token) == type(p):
            print("PRIEMRA ")

            if lastLineErr != currentLineErr:
                errorMsg += "Error sintactico en linea " + str(previous_token.lineno) + "\n"
                print("\nSyntax error in  " + str(previous_token) + "in line " + str(parser.symstack[-1].lineno))
                parser.errok()
                lastLineErr = currentLineErr

        else:
            print("SEGUNDA ")
            if lastLineErr != currentLineErr:
                errorMsg += "Error sintactico en linea " + str(p.lineno) + "\n"
                print("\nSyntax error in  " + str(p) + "in line " + str(p.lineno))
                lastLineErr = currentLineErr
    
    else:
        print("END OF FILEEEEEEEE ")

    

    #backUp += [str(parser.symstack[-1].lineno)]



def returnErrorSintacticoMessage():
    return errorMsg if errorMsg!="" else True

# PRUEBA DEL PARSER EN UN ARCHIVO ----------------------------------------------------
#print("\n")
#file = 'src/TestsFiles/TagaPlateCode.tgp'
#fp = codecs.open(file)
#cadena = fp.read()
parser = yacc.yacc()
#fp.close()

def parseM(input):
    print("hey")
    return parser.parse(input)

#result =  parseM(cadena)

#result.imprimir("")
#print result
"""
fileNew=open("semanticTree.vz","w")
fileNew.write(result.transalte())
fileNew.close()"""

#print("\nParser.parse(cadena) =  " + str(parser.parse(cadena)) + "\n")

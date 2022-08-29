import codecs
import ply.lex as lex
import re

# Definition of the tokens
keywords = ["New","Num","Bool","True","False","Proc","CALL","Values","Alter","AlterB",
            "MoveRight","MoveLeft","Hammer","Stop","IsTrue","Repeat",
            "Until","While","Case", "When","Then","Else","PrintValues",
            "ADD","SUB","MUL","DIV","Norte","Sur","Este","Oeste","Break"]
tokens = keywords+["ID","Number","COMMA","LPARENTHESIS","RPARENTHESIS","SEMMICOLOM",
                    "Less","LessEqual","Greater","GreaterEqual","Equals","Different"]

# Keywords definition for lex
t_New = 'New'
t_Num = 'Num'
t_Bool = 'Bool'
t_True = "True"
t_False = "False"
t_Proc = 'Proc'
t_CALL = 'CALL'
t_Values = 'Values'
t_Alter = 'Alter'
t_AlterB = 'AlterB'
t_MoveRight = 'MoveRight'
t_MoveLeft = 'MoveLeft'
t_Hammer = 'Hammer'
t_Stop = 'Stop'
t_IsTrue = 'IsTrue'
t_Repeat = 'Repeat'
t_Until = 'Until'
t_While = 'While'
t_Case = 'Case'
t_When = 'When'
t_Then = 'Then'
t_Else = 'Else'
t_ADD = 'ADD'
t_SUB = 'SUB'
t_MUL = 'MUL'
t_DIV = 'DIV'
t_Norte = 'N'
t_Sur = 'S'
t_Este = 'E'
t_Oeste = 'O'
t_Break = 'Break'

# Special Characters
t_ignore='\t \r'
t_COMMA = r','
t_SEMMICOLOM = ';'
t_LPARENTHESIS =r'\('
t_RPARENTHESIS =r'\)'

# Conditionals
t_Less = r'<'
t_LessEqual= r'<='
t_Greater = r'>'
t_GreaterEqual= r'>='
t_Equals = r'=='
t_Different = r'<>'

# Review error with ID extension (number of characters)
def t_ID(t):
    r'@[a-zA-Z0-9_#][a-zA-Z0-9_#][a-zA-Z0-9_#]{0,7}'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_Number(t):
    r'\d'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_PrintValues(t):
    r'PrintValues(.*)'
    if t.value.upper() in keywords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_Comment(t):
     r'--.*'
     pass

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error en el token" +str(t)+" in line "+str(t.lexer.lineno)+"\n")
    t.lexer.skip(1)

file = r"..\TagaPlateCode.txt"

fp = codecs.open(file,"r","utf-8")

theString = fp.read()

analizador = lex.lex()
analizador.input(theString)

while True:
    tok = analizador.token()
    if not tok:
        break
    print(tok)
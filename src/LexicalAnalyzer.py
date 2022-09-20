# El analizador léxico se encarga de reconocer los caracteres en el código

import codecs
import ply.lex as lex


reserverdWords = ["New", "Num", "Bool", "True", "False", "Proc", "CALL", "Values", "Alter", "AlterB",
                    "MoveRight", "MoveLeft", "Hammer", "Stop", "IsTrue", "Repeat",
                    "Until", "While", "Case", "When", "Then", "Else", "PrintValues",
                    "ADD", "SUB", "MUL", "DIV", "Norte", "Sur", "Este", "Oeste", "Break", "PRINCIPAL"]
tokens = reserverdWords + ["ID", "Number", "COMMA", "LPARENTHESIS", "RPARENTHESIS", "SEMMICOLOM",
                            "Less", "LessEqual", "Greater", "GreaterEqual", "Equals", "Different","TEXTVALUE"]
                            
# reserverdWords definition for lex
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
t_ID = r'@[a-zA-Z0-9_#][a-zA-Z0-9_#][a-zA-Z0-9_#]{0,7}'

# Special Characters
t_ignore = '\t \r'
t_COMMA = r','
t_SEMMICOLOM = ';'
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_TEXTVALUE = r'\".+\"'

# Conditionals
t_Less = r'<'
t_LessEqual = r'<='
t_Greater = r'>'
t_GreaterEqual = r'>='
t_Equals = r'=='
t_Different = r'<>'

errorMessage = ""
currentLineError = 0
lastLineError = currentLineError
# Review error with ID extension (number of characters)
def t_PRINCIPAL(t):
    r'@Principal'
    if t.value.upper() in reserverdWords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_Number(t):
    r'\d'
    if t.value.upper() in reserverdWords:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_PrintValues(t):
    r'PrintValues'
    if t.value.upper() in reserverdWords:
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
    currentLineError = t.lexer.lineno
    print("Error en el token" + str(t) + " in line " + str(t.lexer.lineno) + "\n")
    t.lexer.skip(1)
    global errorMessage, lastLineError
    if lastLineError != currentLineError:
        errorMessage += "Error de sintáxis en línea "+ str(t.lexer.lineno) + "\n"
    lastLineError = currentLineError


def testLexer():
    file = r"..\src\TestsFiles\TagaPlateCodeVar.tgp"
    fp = codecs.open(file, "r", "utf-8")
    theString = fp.read()
    analizador = lex.lex() # antes tenía la palabra module dentro del paréntesis, pero daba problema porque ya no es una clase
    analizador.input(theString)

    while True:
        tok = analizador.token()
        if not tok:
            break
        print(tok)

def returnSymbolTable(file):
    symbolTable = ""
    global errorMessage
    errorMessage = ""
    fp = codecs.open(file,"r","utf-8")
    theCodeString = fp.read()
    analyzer = lex.lex()
    analyzer.input(theCodeString)
    while True:
        tok = analyzer.token()
        if not tok:
            break
        symbolTable += str(tok)+"\n"
    return symbolTable

def returnErrorLexicalMesage():
    return errorMessage if errorMessage!="" else True

analizador =lex.lex()
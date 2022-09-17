"""def p_listaInstrucciones(p):
    '''listaInstrucciones : conjuntoInstrucciones instruccion'''
    p[1].append(p[2])
    p[0] = p[1]
    print("listaInstrucciones", p[1])

def p_conjuntoInstrucciones(p):
    '''conjuntoInstrucciones : instruccion'''
    p[0] = ["conjuntoInstrucciones", p[1]]
"""


# RECONOCIMIENTO DE CONDICIONALES ------------------------------------------
        # estas son importantes para definir condiciones de finalización en funciones como: Until, While y Case When

""""
def p_condicional_f(p):
    '''condicional : Greater_f
                    | GreaterEqual_f
                    | Equals_f
                    | Different_f
                    | LessEqual_f
                    | Less_f'''
    print("condicional ", p)

def p_Greater_f(p):
    '''Greater_f : expresion Greater expresion'''
    print("Greater_f", p)

def p_GreaterEqual_f(p):
    '''GreaterEqual_f : expresion GreaterEqual expresion'''
    print("GreaterEqual", p)

def p_Equals_f(p):
    '''Equals_f : expresion Equals expresion'''
    print("Equals", p)

def p_Different_f(p):
    '''Different_f : expresion Different expresion'''
    print("Different_f:", p)

def p_LessEqual_f(p):
    '''LessEqual_f : expresion LessEqual expresion'''
    print("LessEquals", p)

def p_Less_f(p):
    '''Less_f : expresion Less expresion'''
    print("Less_f :", p)"""
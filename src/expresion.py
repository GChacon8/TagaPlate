from ast import Num
from enum import Enum


class NumberExpression():
    '''

    '''
class Identificator(NumberExpression):
    def __init__(self,id):
        self.id=id
class Valor(NumberExpression):
    def __init__(self,valor):
        self.valor=valor

class Logic(NumberExpression) :
    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class Binar_Expression(NumberExpression):
    def __init__(self,num1,operador,num2):
        self.num1=num1
        self.operador=operador
        self.num2 = num2

class ExpresionString():
    '''
    '''
class ExpresionConcatenar(ExpresionString) :
    '''
        Esta clase representa una Expresión de tipo cadena.
        Recibe como parámetros las 2 expresiones a concatenar
    '''

    def __init__(self, dato1, dato2) :
        self.dato1=dato1
        self.dato2 = dato2


class OperationA(Enum) :
    Plus = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4

class OperationL(Enum) :
    GREATER = 1
    LESS = 2
    EQUAL = 3
    DIFFERENT = 4
    GREATEREQUAL=5
    LESSEQUAL=6
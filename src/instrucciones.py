


class Instrucciones():
    '''Clase Para generar el AST'''

class Process(Instrucciones):
    def __init__(self,id,instrucciones=[]):
        self.id=id
        self.instrucciones=instrucciones

class While(Instrucciones):
    def __init__(self,condicion,instrucciones=[]):
        self.condicion=condicion
        self.instrucciones=instrucciones

class PrintValues(Instrucciones):
    def __init__(self,valor):
        self.valor=valor
        

class Assigment(Instrucciones):
    def __init__(self,id,type,valor):
        self.id=id
        self.type=type
        self.valor=valor
class Values(Instrucciones):
    def __init__(self,id,valor):
        self.id=id
        self.valor=valor

class Alter(Instrucciones):
    def __init__(self,id,operador,valor):#valor Puede ser un valor tal cual o una operacion
        self.id=id
        self.operador=operador
        self.valor=valor

class AlterB(Instrucciones):
    def __init__(self,id):#valor Puede ser un valor tal cual o una operacion
        self.id=id

class MoveRight(Instrucciones):
    def __init__(self):
        self.move=180
class MoveLefth(Instrucciones):
    def __init__(self):
        self.move=-180
        
class Hammer(Instrucciones):
    def __init__(self,position):
        self.position=position
class Stop(Instrucciones):
    pass

#condiciones booleanas
class IsTrue(Instrucciones):
    def __init__(self,id):
        self.id=id


class Repeat(Instrucciones):
    def __init__(self,instrucciones=[]):
        self.instrucciones=instrucciones

class Until():
    def __init__(self,condicion,instrucciones=[]):
        self.condicion=condicion
        self.instrucciones=instrucciones
class Call(Instrucciones):
    def __init__(self,id):
        self.id=id






        


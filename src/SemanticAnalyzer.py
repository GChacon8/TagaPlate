from textwrap import indent


txt=""
cont=0
def contadorPlus():
    global cont
    cont+=1
    conver=str(cont)
    return conver
    



class Node():
    pass
class Proced(Node):
    def __init__(self,son1,name):
        self.name=name
        self.name=son1
    
    def translate(self):
        global txt
        id=contadorPlus()
        son1=self.son1.transalte()
        txt+=id +"[label="+self.name+"]"+"\n\t"
        txt+=id+"->"+son1
        return id
    def printData(self,Ident):
        self.son1.printData(""+Ident)
        print(Ident + "Node: "+self.name)
        

        
    


    
    
class recursivo(Node):
    
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass

    





class instruccion(Node): 
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class Values_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class Alter_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class AlterB_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class MoveRight_f(Node):
   def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass



class MoveLeft_f(Node):
   def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass



class Hammer_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class Stop_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class IsTrue_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass


class Repeat_f(Node):
   def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass



class Until_f(Node):
  def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass


class While_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class Case_f(Node):
   def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass



class PrintValues_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



class empty(Node):
   
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass





# RECONOCIMIENTO DE VARIABLES---------------------------------------------------------

class varDeclaration(Node):
   def __init__(self, name):
    self.name=name
def translate(self):
    global txt
    id=contadorPlus()
    return id
def printData(self):
    pass


class tipoDatos(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass


class valorDato(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass



# definir qué es una expresion 


# LLAMAR A UNA FUNCIÓN ---------------------------------------------------------------

class call_f(Node):
    def __init__(self, name):
        self.name=name
    def translate(self):
        global txt
        id=contadorPlus()
        return id
    def printData(self):
        pass


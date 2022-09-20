class Tabla_Of_Simbols() :

    def __init__(self, simbols = {}) :
        self.simbols = simbols

    def agregar(self, simbol) :
        self.simbols[simbol.id] = simbol
    
    def obtener(self, id) :
        if not id in self.simbolos :
            print('Error: variable ', id, ' no definida.')

        return self.simbolos[id]

    def actualizar(self, simbols) :
        if not simbols.id in self.simbolos :
            print('Error: variable ', simbols.id, ' no definida.')
        else :
            self.simbols[simbols.id] = simbols




class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, type, values) :
        self.id = id
        self.tipo = type
        self.valor = values
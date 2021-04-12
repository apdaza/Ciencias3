class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


arbol = Nodo(5, Nodo(3, Nodo(1)), Nodo(10, Nodo(7), Nodo(15, None, Nodo(20))))

def en_orden(arbol):
    if arbol == None:
        return []
    else:
        return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def pre_orden(arbol):
    if arbol == None:
        return []
    else:
        return [arbol.valor] + pre_orden(arbol.izquierda) + pre_orden(arbol.derecha)

def pos_orden(arbol):
    if arbol == None:
        return []
    else:
        return pos_orden(arbol.izquierda) + pos_orden(arbol.derecha) + [arbol.valor] 

def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor > valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)
    return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor)) 

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    if arbol.valor > valor:
        return buscar(arbol.izquierda, valor)
    return buscar(arbol.derecha, valor)

print(en_orden(arbol))

arbol = insertar(arbol, 4)
arbol = insertar(arbol, 12)
print(en_orden(arbol))

print(buscar(arbol, 4))
print(buscar(arbol, 40))
print(buscar(arbol, 12))
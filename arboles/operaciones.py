class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+', '-', '*', '/']:
        return "(" + en_orden(arbol.izquierda) + str(arbol.valor) + en_orden(arbol.derecha) + ")"
    else:
        return str(arbol.valor)

def evaluar(arbol):
    if arbol == None:
        pass
    else:
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        if arbol.valor == '-':
            return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
        if arbol.valor == '*':
            return evaluar(arbol.izquierda) * evaluar(arbol.derecha)
        if arbol.valor == '/':
            return evaluar(arbol.izquierda) // evaluar(arbol.derecha)
        return int(arbol.valor)

expresion = Nodo('-', Nodo('+', Nodo('-', Nodo(10), Nodo(5)), Nodo('*', Nodo(2), Nodo(3))), Nodo('/', Nodo(5), Nodo(2)))

print(en_orden(expresion) + " = " + str(evaluar(expresion)))
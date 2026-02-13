# Clases
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.conexiones = []

class Arista:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

# Funciones de operaciones aritmeticas
def suma (x, y):
    res = x + y
    return res

def resta (x, y):
    res = x - y
    return res

def multi (x, y):
    res = x * y
    return res

def divi (x, y):
    res = x / y
    return res

# Mostrar conexiones
def mostrarConexiones(n: Nodo):
    for i in n.conexiones:
        print(i.origen.valor + " -> " + i.destino.valor)

# objetos Nodo
nodoA = Nodo("A")
nodoB = Nodo("B")
nodoC = Nodo("C")

# objetos Arista
aristaAB = Arista(nodoA, nodoB)
aristaBC = Arista(nodoB, nodoC)
aristaCA = Arista(nodoC, nodoA)

# Conexiones
nodoA.conexiones.append(aristaAB)
nodoB.conexiones.append(aristaBC)
nodoC.conexiones.append(aristaCA)
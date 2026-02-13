import grapho_ern

# Grafo ABCD
def grafoAD():
    grafo = grapho_ern.Grafo()

    #Nodos
    grafo.agregar_nodo("A") #0
    grafo.agregar_nodo("B") #1
    grafo.agregar_nodo("C") #2
    grafo.agregar_nodo("D") #3

    #Aristas
    grafo.agregar_arista(grafo.nodos[0], grafo.nodos[1]) # A-B
    grafo.agregar_arista(grafo.nodos[1], grafo.nodos[2]) # B-C
    grafo.agregar_arista(grafo.nodos[2], grafo.nodos[3]) # C-D
    grafo.agregar_arista(grafo.nodos[3], grafo.nodos[0]) # D-A

    grafo.actualizar_conexiones()

    print(grafo.trayectoria(grafo.nodos[0], grafo.nodos[3]))

grafoAD()
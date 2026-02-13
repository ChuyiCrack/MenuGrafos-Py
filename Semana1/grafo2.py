import grapho_ern

def grafoAH(): 
    grafo = grapho_ern.Grafo()

    # Nodos
    grafo.agregar_nodo("A") # 0
    grafo.agregar_nodo("B") # 1
    grafo.agregar_nodo("C") # 2
    grafo.agregar_nodo("D") # 3
    grafo.agregar_nodo("E") # 4
    grafo.agregar_nodo("F") # 5
    grafo.agregar_nodo("G") # 6
    grafo.agregar_nodo("H") # 7

    # Aristas

    # Nodo A
    grafo.agregar_arista(grafo.nodos[0], grafo.nodos[1]) # A-B
    grafo.agregar_arista(grafo.nodos[0], grafo.nodos[2]) # A-C
    grafo.agregar_arista(grafo.nodos[0], grafo.nodos[3]) # A-D
    grafo.agregar_arista(grafo.nodos[0], grafo.nodos[6]) # A-G

    # Nodo B
    grafo.agregar_arista(grafo.nodos[1], grafo.nodos[2]) # B-C

    # Nodo C
    grafo.agregar_arista(grafo.nodos[2], grafo.nodos[4]) # C-E

    # Nodo D
    grafo.agregar_arista(grafo.nodos[3], grafo.nodos[2]) # D-C

    # Nodo E
    grafo.agregar_arista(grafo.nodos[4], grafo.nodos[5]) # E-F
    grafo.agregar_arista(grafo.nodos[4], grafo.nodos[6]) # E-G
    grafo.agregar_arista(grafo.nodos[4], grafo.nodos[7]) # E-H

    # Nodo F
    grafo.agregar_arista(grafo.nodos[5], grafo.nodos[6]) # F-G

    # Nodo G
    grafo.agregar_arista(grafo.nodos[6], grafo.nodos[7]) # G-H

    grafo.actualizar_conexiones()

    print(grafo.trayectoria(grafo.nodos[0], grafo.nodos[6]))

# Generar grafo
grafoAH()
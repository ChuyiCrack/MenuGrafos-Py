from menuGrafos import grapho

class Grafo7:
    @property
    def get_grafo(self):
        miGrafo = grapho()

        A = miGrafo.agregar_nodo("A")
        B =miGrafo.agregar_nodo("B")
        C = miGrafo.agregar_nodo("C")
        D = miGrafo.agregar_nodo("D")
        E = miGrafo.agregar_nodo("E")
        F = miGrafo.agregar_nodo("F")
        G = miGrafo.agregar_nodo("G")
        H = miGrafo.agregar_nodo("H")

        miGrafo.agregar_arista(A,B)
        miGrafo.agregar_arista(A,D)
        miGrafo.agregar_arista(A,C)
        miGrafo.agregar_arista(A,G)
        miGrafo.agregar_arista(B,C)
        miGrafo.agregar_arista(C,D)
        miGrafo.agregar_arista(C,E)
        miGrafo.agregar_arista(E,F)
        miGrafo.agregar_arista(E,H)
        miGrafo.agregar_arista(E,G)
        miGrafo.agregar_arista(H,G)
        miGrafo.agregar_arista(F,G)
        
        miGrafo.actualizar_conexiones()

        return miGrafo



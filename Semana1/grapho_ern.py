class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.conexiones = []
        def __repr__(self):
            return self.valor

    class Arista:
        def __init__(self, origen, destino):
            self.origen = origen
            self.destino = destino
        def __repr__(self):
            return self.origen.valor + "-" + self.destino.valor

    def __repr__(self):
        return "Nodos " + self.nodos + " " + "Aristas " + self.Arista

    def agregar_nodo(self, valor):
        nodo = self.Nodo(valor)
        self.nodos.append(nodo)
        return nodo

    def agregar_arista(self, origen, destino):
        arista = self.Arista(origen, destino)
        self.aristas.append(arista)

    def actualizar_conexiones(self):
        for i,n in enumerate(self.nodos):
            for a in self.aristas:
                if(n==a.origen or n==a.destino):
                    self.nodos[i].conexiones.append(a)

    ##Metodo trayectoria de la clase grapho
    def trayectoria(self, inicio, fin):
            if inicio == fin:
                return [inicio]
            
            camino = [inicio]
            actual = inicio
            usadas = set()   # Creando un conjunto nota: los conjuntos no aceptan repeticiones

            while actual != fin:
                avance = False

                for a in actual.conexiones:
                    if a in usadas:
                        continue#Brincar a la siguiente iteraccion delciclo

                    # como el grafo es no  dirigido, tomo el otro extremo
                    if a.origen == actual:
                        siguiente = a.destino
                    else:
                        siguiente = a.origen

                    usadas.add(a)
                    camino.append(siguiente)
                    actual = siguiente
                    avance = True
                    break   # se toma la primera arista disponible

                if not avance:
                    return None  #No hay trayectoria. ya no avanzo
            return camino
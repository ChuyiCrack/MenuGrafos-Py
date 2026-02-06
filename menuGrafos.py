from math import factorial
import pandas as pd

class grapho:
    def __init__(self):
         self.nodos=[]
         self.aristas=[]
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
         return "Nodos " + self.nodos +" " + "Aristas "+ self.Arista
    

    def obtener_indice_nodo(self,targetValue):
        for i,nodo in enumerate(self.nodos):
            if nodo.valor == targetValue:
                return i

        return None

    def obtener_grado_nodo(self,nodo:Nodo):
        return len(nodo.conexiones)

    def trayectoria_dfs(self, nodo_inicio, nodo_final):
        visitados = set()
        recorrido = [nodo_inicio]

        def dfs(nodo):
            if nodo == nodo_final:
                return True

            visitados.add(nodo)

            for arista in nodo.conexiones:
                if nodo == arista.origen:
                    sig = arista.destino
                else:
                    sig = arista.origen

                if sig not in visitados:
                    recorrido.append(sig)
                    print(recorrido)
                    if dfs(sig):         
                        return True

                    recorrido.pop()      

            return False

        dfs(nodo_inicio)
        return recorrido
    
    def mostrarCaminoBonito(self,camino):
        if not camino:
            return "No ruta XD"
        res = ""
        for i,c in enumerate(camino):
            if i == len(camino) - 1:
                res+=str(c)
            else:
                res+= f"{str(c)} -> "
        return res 


    def mostrar_tabla_todas_rutas(self):
        df = pd.DataFrame(columns=["Origen" , "Destino" , "Grado Origen" , "Grado Destino" , "Llego" , "LongCamino" , "Nodos Explorados" , "Ruta"])
        allRutas = self.obtener_arreglo_todas_rutas
        for fr , to in allRutas:
            camino = self.trayectoria_grado(fr,to)
            df.loc[len(df)] = [fr, to, self.obtener_grado_nodo(fr) , self.obtener_grado_nodo(to),"Si" if camino else "No" , len(camino) if camino else 0,set(camino) if camino else [],self.mostrarCaminoBonito(camino)]
        print(df)

    @property
    def obetner_numero_total_rutas(self):
        return int(factorial(len(self.nodos)) / factorial(len(self.nodos) - 2))
    @property
    def obtener_arreglo_todas_rutas(self):
        res = []
        allNodos = self.nodos
        for i in range(len(allNodos)):
            for j in range(len(allNodos)):
                if i == j:
                    continue
                res.append((allNodos[i] , allNodos[j]))
        return res
    
    def mostrar_lista_todas_rutas(self):
        allRutas = self.obtener_arreglo_todas_rutas()
        print("Todas las permutaciones de rutas")
        for fr , to in allRutas:
            print(f"{fr} --> {to}")
                

    def mostrar_rutas_permutaciones(self):
        allRutas = self.obtener_arreglo_todas_rutas
        for fr , to in allRutas:
            camino = self.trayectoria_grado(fr,to)
            print(f"Ruta ({fr,to}) = {self.mostrarCaminoBonito(camino)}")

    def obtener_nodo(self,targetValue):
        for nodo in self.nodos:
            if nodo.valor == targetValue:
                return nodo

        return None


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

    def trayectoria_euristica_noVisitado(self , origen , destino) -> None:
        if origen == destino:
            return [origen]  

        camino = [origen]
        curr = origen 
        visited = set()
        VisitedAristas = set()
        avance =False
        while curr != destino:
            for a in curr.conexiones:
                if a in VisitedAristas:
                    continue

                VisitedAristas.add(a)

                if a.origen == actual:
                    siguiente = a.destino
                else:
                    siguiente = a.origen

                if siguiente in visited:
                    continue

                visited.add(siguiente)
                camino.append(siguiente)
                curr = siguiente
                avance = True
                break

            if not avance:
                print(f"Camino no encontrado -> {camino}")
                return [None]




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

    
    def trayectoria_grado(self, inicio, fin, modo="max"):
        if inicio == fin:
            return [inicio]

        camino = [inicio]
        actual = inicio
        usadas = set()  # aristas ya usadas (para no repetir)

        while actual != fin:
            # aristas disponibles desde el nodo actual
            candidatas=self.obtener_candidatas(actual,usadas)#candidatas = [ar for ar in actual.conexiones if ar not in usadas]
            if not candidatas:
                return None
            # elegir la mejor arista según la heurística de grado
            mejor_arista = None
            mejor_valor = None

            for ar in candidatas:
                # grafo no dirigido: tomar el otro extremo
                #siguiente = ar.destino if ar.origen == actual else ar.origen
                siguiente = self.obtener_siguiente(ar,actual)
                valor = self.grado_restante(siguiente,usadas)  # heurística
                mejor_arista,mejor_valor = self.mejor_arista(ar,valor,mejor_arista,mejor_valor)
            # aplicar el paso elegido
            usadas.add(mejor_arista)
            siguiente = self.obtener_siguiente(mejor_arista,actual)
            camino.append(siguiente)
            actual = siguiente

        return camino
  #return sum(1 for ar in nodo.conexiones if ar not in usadas)
    def grado_restante(self,nodo,usadas):
        contador = 0
        for arista in nodo.conexiones:
            esta_usada = arista in usadas
            if esta_usada == False:
                contador = contador + 1
        return contador
   
    def obtener_candidatas(self,nodo, usadas):
        candidatas = []
        for arista in nodo.conexiones:
            if arista not in usadas:
                candidatas.append(arista)
        return candidatas
    def obtener_siguiente(self,arista, actual):
    # 1. Verificar si el nodo actual es el origen de la arista
        if arista.origen == actual:
            siguiente = arista.destino
        else:
            siguiente = arista.origen
        return siguiente
    def mejor_arista(self,ar,valor,mejor_arista,mejor_valor,modo="max"):              
                if mejor_arista is None:
                    mejor_arista = ar
                    mejor_valor = valor
                else:
                    if modo == "max":
                        if valor > mejor_valor:
                            mejor_arista = ar
                            mejor_valor = valor
                    else:  # modo == "min"
                        if valor < mejor_valor:
                            mejor_arista = ar
                            mejor_valor = valor
               
                return mejor_arista,mejor_valor


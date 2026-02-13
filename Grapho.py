from math import factorial
from matplotlib import pyplot as plt
import pandas as pd
from Grafo_7 import grafo7
import numpy as np

class Grapho:

    # propiedades

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
        return "Nodos " + str(self.nodos) +" " + "Aristas "+ str(self.aristas)
    
    # grafos predefinidos

    def grafo_7(self):
        return grafo7(self)
    
    # metodos

    # retorna una representacion bonita del camino dado, o "No ruta" si el camino es vacio
    def camino_string(self,camino):
        if not camino:
            return "No ruta"
        res = ""
        for i,c in enumerate(camino):
            if i == len(camino) - 1:
                res+=str(c)
            else:
                res+= f"{str(c)} -> "
        return res 


    # retorna el nodo con el valor dado, o None si no se encuentra
    def obtener_nodo(self,targetValue):
        for nodo in self.nodos:
            if nodo.valor == targetValue:
                return nodo
        return None


    # agrega un nodo con el valor dado al grafo y lo retorna
    def agregar_nodo(self, valor):
        nodo = self.Nodo(valor)
        self.nodos.append(nodo)
        return nodo

    # agrega una arista entre los nodos con los valores dados
    def agregar_arista(self, origen, destino):
        arista = self.Arista(origen, destino)
        self.aristas.append(arista)
    
    # actualiza las conexiones de cada nodo según las aristas del grafo
    def actualizar_conexiones(self):
        for i,n in enumerate(self.nodos):
            for a in self.aristas:
                if(n==a.origen or n==a.destino):
                    self.nodos[i].conexiones.append(a)

    # retorna el indice en la lista de nodos del nodo con el valor dado, o None si no se encuentra
    def obtener_indice_nodo(self,targetValue):
        for i,nodo in enumerate(self.nodos):
            if nodo.valor == targetValue:
                return i

        return None
    
    # retorna el grado de un nodo
    def obtener_grado_nodo(self,nodo:Nodo):
        return len(nodo.conexiones)

    
    # retorna las aristas candidatas para avanzar desde un nodo dado, excluyendo las aristas ya usadas
    def obtener_candidatas(self,nodo, usadas):
        candidatas = []
        for arista in nodo.conexiones:
            if arista not in usadas:
                candidatas.append(arista)
        return candidatas


    # retorna el nodo destino de una arista dada el nodo actual
    def obtener_siguiente(self,arista, actual):
        return arista.destino if arista.origen == actual else arista.origen
    
    # retorna el grado de un nodo considerando solo las aristas no usadas
    def grado_restante(self,nodo,usadas):
        contador = 0
        for arista in nodo.conexiones:
            if not arista in usadas:
                contador = contador + 1
        return contador

    # retorna la mejor arista según el valor dado y el modo (max o min)
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

    # trayectorias
    @property
    def trayectoria(self):

        # retorna el camino entre dos nodos usando un recorrido voraz, o None si no se encuentra un camino
        def voraz(inicio, fin):
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

        # retorna el camino entre dos nodos usando una heuristica de nodo no visitado, o None si no se encuentra un camino
        def no_visitado(nodo_inicio, nodo_final):
            visitados = set()
            recorrido = [nodo_inicio]

            def no_visitado(nodo):
                if nodo == nodo_final:
                    return True

                visitados.add(nodo)

                for arista in nodo.conexiones:
                    sig = self.obtener_siguiente(arista,nodo)

                    if sig not in visitados:
                        recorrido.append(sig)
                        print(recorrido)
                        if no_visitado(sig):         
                            return True

                        recorrido.pop()      

                return False

            if not no_visitado(nodo_inicio):
                return None
            return recorrido

        # retorna el camino entre dos nodos usando euritstica de mayor grado, o None si no se encuentra un camino
        def mayor_grado(inicio, fin, modo="max"):
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
        
        class Helper: pass
        h = Helper()
        h.voraz = voraz
        h.no_visitado = no_visitado
        h.mayor_grado = mayor_grado
        return h
    

    # rutas

    @property
    def rutas(self):

        # retorna una lista de tuplas con todas las permutaciones de rutas posibles entre nodos, sin repetir nodos origen y destino
        def all():
            res = []
            allNodos = self.nodos
            for i in range(len(allNodos)):
                for j in range(len(allNodos)):
                    if i == j:
                        continue
                    res.append((allNodos[i] , allNodos[j]))
            return res
        
        # imprime una lista de todas las permutaciones de rutas posibles entre nodos, sin repetir nodos origen y destino
        def imprimir_lista():
            allRutas = all()
            print("Todas las permutaciones de rutas")
            for fr , to in allRutas:
                print(f"{fr} --> {to}")

        # retorna un dataframe con todas las rutas posibles entre nodos, su grado de origen y destino, si se encontro una ruta usando la heuristica de mayor grado, la longitud de esa ruta, los nodos explorados y la ruta encontrada
        def tabla():
            df = pd.DataFrame(columns=["Origen" , "Destino" , "Grado Origen" , "Grado Destino" , "Llego" , "LongCamino" , "Nodos Explorados" , "Ruta"])
            allRutas = all()
            for fr , to in allRutas:
                camino = self.trayectoria.mayor_grado(fr,to)
                #cambie el la existencia de camino a 1 y 0 para faciliutar manipulcion ----------> Anteriormente 'Si'/'No'
                df.loc[len(df)] = [fr, to, self.obtener_grado_nodo(fr) , self.obtener_grado_nodo(to),1 if camino else 0 , 10-len(camino) if camino else 10,set(camino) if camino else {},self.camino_string(camino)]
            return(df)
        
        # retorna el numero total de rutas posibles entre nodos
        def total_rutas():
            return int(factorial(len(self.nodos)) / factorial(len(self.nodos) - 2))

        # imprime todas las rutas posibles entre nodos, su grado de origen y destino, si se encontro una ruta usando la heuristica de mayor grado, la longitud de esa ruta, los nodos explorados y la ruta encontrada
        def imprimir_rutas():
            allRutas = all()
            for fr , to in allRutas:
                camino = self.trayectoria.mayor_grado(fr,to)
                print(f"Ruta ({fr,to}) = {self.camino_string(camino)}")


        # retorna un objeto con las funciones anteriores para trabajar con las rutas del grafo
        class Helper: pass
        h = Helper()
        h.all = all
        h.imprimir_lista = imprimir_lista
        h.tabla = tabla
        h.total_rutas = total_rutas
        h.imprimir_rutas = imprimir_rutas
        return h


    # graficas 


    def graficar_knn_y_recta(self, df, gradoInicialEvaluar, gradoFinalEvaluar, umbral=6):

        #Esto lo que hace es hacer 2 dataFrame. un  agarrando los que si llegaron y el otro los que bo
        siLlego=df[df['Llego']==1]
        noLlego=df[df['Llego']==0]

        plt.figure(figsize=(10,6))

        #aqui se hacen 3 graficas de dispersion. La primera es de las que si llegaron marcandose con o
        #La segunda es las que no llegaron marcando se con x y la ultima es la evaluacin que estamos haceindo marcandose con una estrella
        plt.scatter(siLlego['Grado Origen'],siLlego['Grado Destino'],marker='o',color='blue',s=50,label='Llego')
        plt.scatter(noLlego['Grado Origen'],noLlego['Grado Destino'],marker='x',color='red',s=50,label='no Llego')
        plt.scatter(gradoInicialEvaluar,gradoFinalEvaluar,marker='*',color='yellow', edgecolors='black', s=250, label="Punto Evaluado")

        #ruta heuristica/La linea
        #Esto lo que hace es que crea un numpy array que devuelve el valor minimo y maximo que en nuestro dataFrame
        #El valorY dependera del umbral. En este momento no se que define el umbra XD. pero lo que hace en forma base es
        # 6 - todo el numpy array que devolveria [6-gradoMin,6-gradoMax] 
        valorX= np.array([df['Grado Origen'].min(),df['Grado Origen'].max()])
        valorY=umbral-valorX
        #esto es lo que hace nuestra linea/ el 'plot'
        plt.plot(valorX,valorY,color='Black',linestyle='--',linewidth=2,label=f"Recta Heurística (Gi+GF={umbral})")

        #Esto es solo decoracion que el plot necesita 
        plt.title('Diagrama de Dispersión con Clasificación y Recta')
        plt.xlabel('Grado Origen (Gi)')
        plt.ylabel('Grado Destino (GF)')
        plt.legend(loc='lower left')
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.show()
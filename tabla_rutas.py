import pandas as pd
from Grapho import Grapho
grafo = Grapho().grafo_7()

start = grafo.obtener_nodo("A")
end = grafo.obtener_nodo("H")


print(grafo.trayectoria.bfs(grafo,start,end))
'''df = grafo.rutas.tabla()
print(df)'''
# print(df[['Grado Origen','Grado Destino']]) 

#Aqui solo es cambiarle los valores para obtener los nodos
#En proximas versiones esto deberia de ser 2 inputs en el menu
'''nodoInicial = grafo.obtener_nodo("A")
nodoFinal = grafo.obtener_nodo("H")

grafo.graficar_knn_y_recta(df, grafoA.grado(), grafoH.grado())
'''
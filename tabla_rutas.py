import pandas as pd
from Grapho import Grapho

grafo = Grapho().grafo_7()

start = grafo.obtener_nodo("A")
end = grafo.obtener_nodo("H")

df = grafo.rutas.tabla()

# print(df[['Grado Origen','Grado Destino']]) 

grafoA = grafo.obtener_nodo("A")
grafoH = grafo.obtener_nodo("H")

grafo.graficar_knn_y_recta(df, grafoA.grado(), grafoH.grado())
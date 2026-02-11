from Grafo_7 import Grafo7
import pandas as pd
grafo = Grafo7()

grafo = grafo.get_grafo

start = grafo.obtener_nodo("A")
end = grafo.obtener_nodo("H")

df=grafo.mostrar_tabla_todas_rutas()

print(df[['Grado Origen','Grado Destino']])    
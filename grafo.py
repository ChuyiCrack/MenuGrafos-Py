from Grafo_7 import Grafo7
import pandas
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
grafo = Grafo7()

grafo = grafo.get_grafo

start = grafo.obtener_nodo("A")
end = grafo.obtener_nodo("H")

dataframe=grafo.mostrar_tabla_todas_rutas()

umbral=6

gradIniNew=dataframe.iloc[3]['Grado Origen']
gradDesNew=dataframe.iloc[5]['Grado Destino']

siLlego=dataframe[dataframe['Llego']==1]
noLlego=dataframe[dataframe['Llego']==0]

plt.figure(figsize=(10,6))
plt.scatter(siLlego['Grado Origen'],siLlego['Grado Destino'],marker='o',color='blue',s=50,label='Llego')
plt.scatter(noLlego['Grado Origen'],noLlego['Grado Destino'],marker='x',color='red',s=50,label='no Llego')
plt.scatter(gradIniNew,gradDesNew,marker='*',color='yellow', edgecolors='black', s=250, label="Punto Evaluado")
#print(dataframe[['Grado Origen','Grado Destino']])
#print(dataframe)

#ruta heuristica
valorX= np.array([dataframe['Grado Origen'].min(),dataframe['Grado Origen'].max()])
valorY=umbral-valorX

plt.plot(valorX,valorY,color='Black',linestyle='--',linewidth=2,label=f"Recta Heurística (Gi+GF={umbral})")
plt.title('Diagrama de Dispersión con Clasificación y Recta')
plt.xlabel('Grado Origen (Gi)')
plt.ylabel('Grado Destino (GF)')
plt.legend(loc='lower left')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()
dataframe.to_excel('info.xlsx',index=False, engine='openpyxl')
'''dataframe.plot.scatter(x='Grado Origen',y='Grado Destino',c='Score',colormap='viridis',title='dispersion',)
plt.title('Dispersion de grados origen y destino')
plt.xlabel('Grado Origen')
plt.ylabel('Grado Destino')
plt.grid(True)
plt.show()'''

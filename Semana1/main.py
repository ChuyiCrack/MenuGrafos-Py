import grapho_ern

op=1
migrafo=grapho_ern.grapho()

def busca_indice(g,v):
    for i,n in enumerate(g):
        if(v==n.valor):
            return i

while(op!=3):
    print("Menu de grafos")
    print("1.Crear Grafo")
    print("2.-imprimir Grafo ")
    print("3.-Salir")

    op=int(input("Teclea una opcion"))

    if(op==1):
        num_nodos=int(input("Cuantos nodos tiene el grafo"))
        num_aristas=int(input("Cuantas aristas tiene el grafo"))

        for i in range(0,num_nodos,1):
            valor_nodo=input("Teclea el valor del nodo ")
            migrafo.agregar_nodo(valor_nodo)

        for i in range(0,num_aristas,1):
            valor_origen=input("Teclea el valor del origen ")
            indice_origen=busca_indice(migrafo.nodos,valor_origen)
            valor_destino=input("Teclea el valor del destino ")
            indice_destino=busca_indice(migrafo.nodos,valor_destino)
            migrafo.agregar_arista(migrafo.nodos[indice_origen],migrafo.nodos[indice_destino])
        
        migrafo.actualizar_conexiones()

    elif(op==2):
        print("Nodos ",migrafo.nodos)
        print("Aristas",migrafo.aristas)
        
        for n in migrafo.nodos:
            print("Conexiones nodo",n.valor," ",n.conexiones)

    elif(op==3):
        print("hasta la vista")
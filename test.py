arreglo = ['A','B','C','D','E','F','G','H']

for i in range(len(arreglo)):
    for j in range(len(arreglo)):
        if i == j:
            continue

        print((arreglo[i],arreglo[j]))
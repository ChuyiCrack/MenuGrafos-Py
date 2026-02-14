import grafo1_ern

op = 0

while (op != 6):
    print("Menu de grafos")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Crear grafo")
    print("6- Salir")

    op = float(input("Ingresa una opcion: "))

    if (op == 1):
        res = grafo1_ern.suma(10, 7)
        print("Suma = ", res)

    elif (op == 2):
        res = grafo1_ern.resta(10, 7)
        print("Resta = ", res)

    elif (op == 3):
        res = grafo1_ern.multi(10, 7)
        print("Multiplicacion = ", res)

    elif (op == 4):
        res = grafo1_ern.divi(10, 7)
        print("Division = ", res)

    elif (op == 5):
        print("Funcion de creacion")

    elif (op == 6):
        print("Cerrando programa...")
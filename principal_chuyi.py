def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División entre cero"
    return a / b


while True:
    print("\n=== Calculadora Simple ===")
    print("Operaciones disponibles:")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

    opcion = input("Elige una operación (1-5): ")

    if opcion == "5":
        print("Byeee")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado de la suma:", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado de la ressta:", restar(num1, num2))
    elif opcion == "3":
        print("Resultado de la multiplicacion:", multiplicar(num1, num2))
    elif opcion == "4":
        print("Resultado de la division:", dividir(num1, num2))
    else:
        print("Opción Invalidad")

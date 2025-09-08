
def sumar(a, b): 
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: Division por cero"
    return a / b

while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Selecciona una opcion:  ")

    if opcion == '5':
        print("Saliendo...")
        break

    if opcion in {'1', '2', '3', '4'}:
        try:
            num1 = float(input("introduzca el primer numero:  "))
            num2 = float(input("Introduzca el segundo numero: "))
        except ValueError:
            print("Entrada no valida, usa números.")
            continue

        if opcion == "1":
            print("Resultado: ", sumar(num1, num2))
    
        elif opcion == "2":
            print("Resultado: ", restar(num1, num2))

        elif opcion == "3":
            print("Resultado: ", multiplicar(num1, num2))

        elif opcion == "4":
             print("Resultado: ", dividir(num1, num2))

        else:
             print("Opcion no valida, introduce una opcion del 1 al 5. ")


    

#Ejercicio 3: Calculadora Basica
def calculator (a,b,x):
    match x:
        case "+":
            sum = a + b
            print(f"La suma de {a} y {b} es: {sum}")
        case "-":
            sub = a - b
            print(f"La resta de {a} y {b} es: {sub}")
        case "*":
            mul = a * b
            print(f"La multiplicacion de {a} y {b} es: {mul}")
        case "/":
            div = a / b
            print(f"La division de {a} y {b} es: {div}")
        case _:
            print("Operacion no valida")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
x = input("Ingrese la operacion a realizar: ")
calculator(a,b,x)
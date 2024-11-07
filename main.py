#Ejercicio 20: Conversion de calificaciones numericas a letras

print ("Exercise 20")
print("")
def conversor(calificacion):
    match calificacion:
        case calificacion if 90 <= calificacion <= 100:
            print("A")
        case calificacion if 80 <= calificacion <= 89:
            print("B")
        case calificacion if 70 <= calificacion <= 79:
            print("C")
        case calificacion if 60 <= calificacion <= 69:
            print("D")
        case calificacion if 0 <= calificacion <= 59:
            print("F")
        case _:
            print("Calificacion no valida")


calificacion = int(input("Ingrese la calificacion numerica: "))
conversor(calificacion)



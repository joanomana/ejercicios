#Ejercicio 22: Clasificacion de triangulos por sus angulos

print ("Exercise 22")
print("")
angulos = []
for x in range(3):
    angulo = int(input("Ingrese el angulo: "))
    angulos.append(angulo)
    
if sum(angulos) != 180:
        print("Los ángulos no forman un triángulo válido")
elif all(angulo < 90 for angulo in angulos):
        print("El triángulo es agudo")
elif any(angulo == 90 for angulo in angulos):
        print("El triángulo es rectángulo")
elif any(angulo > 90 for angulo in angulos):
        print("El triángulo es obtuso")
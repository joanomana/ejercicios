#Ejercicio 4: Determinacion del tipo de triangulo
print("Exercise 4")
for x in range (0,3):
    lado = float(input("Ingrese el lado del triangulo: "))
    if lado <= 0:
        print("El lado del triangulo no puede ser menor o igual a 0")
        break
    else:
        if x == 0:
            lado1 = lado
        elif x == 1:
            lado2 = lado
        elif x == 2:
            lado3 = lado
            if lado1 == lado2 and lado1 == lado3:
                print("El triangulo es equilatero")
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                print("El triangulo es isosceles")
            else:
                print("El triangulo es escaleno")
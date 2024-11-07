#Ejercicio 18: Sistema de evaluacion de creditos universitarios

print ("Exercise 18")
print("")



x = int(input("Ingrese la cantidad de materias a evaluar: "))
i=0
creditos = 0
for x in range(x):
    nota = float(input("Ingrese la nota (0 a 100): "))
    if nota >= 60 and nota <=100:
        print("Aprobado")
        creditos =creditos + 3
    elif nota >100:
        print("Nota invalida")
        break
        
    else:
        print("Reprobado")
        
    i+=1

print(f"El numero total de creditos es {creditos}")

    

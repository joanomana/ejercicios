#Ejercicio 17: Sistema de calificaciones con bonificaciones

print ("Exercise 17")
print("")


def bonificacion(nota,adicionales):
    if adicionales == "Y" and nota <100 and nota >= 0: 
        nota = (nota *0.05) + nota
        if nota > 100:
            nota = 100
    else:
        pass
    print("La nota final es:",nota)

nota = float(input("Ingrese la nota obtenida: "))
adicionales = input("¿El alumno obtuvo bonificaciones? (Y/N): ")
bonificacion(nota,adicionales)

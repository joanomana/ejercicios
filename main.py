#Ejercicio 2: Calificacion de una nota
print("EXercise 2")

def calificacion(nota):
    
    if nota >= 60:
        print("Aprobado")
    else:
        print("Reprobado")

calificacion(nota= float(input("Ingrese la nota para verificar si es Aprobado o Reprobado: ")))
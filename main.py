#Ejercicio 10: Clasificacion de notas
print("Exercise 10")

grade = int(input("Please enter a rating: "))

if grade >=90 and grade <=100:
    print("A")
elif grade >=80 and grade <=89:
    print("B")
elif grade >=70 and grade <=79:
    print("C")
elif grade >=60 and grade <=69:
    print("D") 
else:
    print("F")
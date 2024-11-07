#Ejercicio 9: Clasificacion de edades
print("Exercise 9")

age = int(input("Enter your age: "))
if age >=0 and age <=12:
    print("You are a child")
elif age >=13 and age <=17:
    print("You ara a teenager")
elif age >=18 and age <=64:
    print("You are an adult")
elif age <0:
    print(f"You can´t be {age} years old")
else:
    print("You are an old man")
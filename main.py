#Ejercicio 7: numero positivo, negativo o cero
print("Exercise 7")

num = float(input("Enter a number to check if it is positive, negative or equal to zero: "))

if num <0:
    print(f"The number {num} is negative")
elif num > 0:
    print(f"The number {num} is positive")
else: 
    print(f"The number is zero")
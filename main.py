#Ejercicio 6: Juego de adivinanzas de numeros
print("Exercise 6")

import random

x = random.randint(1,10)
print("")
print(x)
number = int(input("Enter a number between 1 an 10 to try to guess the random number: "))

if number < x:
    print("The number you entered is lower, try again")
elif number > x:
    print("The number you entered is higher, try again")
else: 
    print("You did it, you guessed the number")
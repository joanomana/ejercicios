#Ejercicio 14: Adivinanza de letras 

print ("Exercise 14")

def guess_letter(guess):
    while True:
        match guess:
            case "C":
                print("You guessed it!")
                break
            case _:
                print("Try again!")
guess = str(input("Guess the letter between (A,B,C,D): "))
guess_letter(guess.upper())
 
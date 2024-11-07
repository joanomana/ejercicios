#Ejercicio 5: Dias de la semana
print("Exercise 5")

def day (x):
    match x:
        case 1:
            print("The number 1 is Monday")
        case 2: 
            print("The number 2 is Tuesday")
        case 3:
            print("The number 3 is Wednesday")
        case 4: 
            print("The number 4 is Thursday")
        case 5: 
            print("The number 5 is Friday")
        case 6: 
            print("The number 6 is Saturday")
        case 7:
            print("The number 7 is Sunday")
        case _:
            print("Incorrect Number")
day(x=int(input("Enter a number between 1 and 7 to display the day of the week: ")))

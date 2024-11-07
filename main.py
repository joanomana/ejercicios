#Ejercicio 21: Sistema de estacionamiento con tarifas progresivas

print ("Exercise 21")
print("")

def parking(hours):
    match hours:
        case hours if hours >=0 and hours <=1:
            print("The cost of parking is $5")
        case hours if hours >=2 and hours <=4:
            cost = 4*hours
            print(f"The cost of parking is ${cost}")
        case hours if hours >4:
            total_extra = hours - 4
            cost = 3*total_extra + 16
            print(f"The cost of parking is ${cost}")
        case _:
            print("Invalid data")


hours = int(input("Enter the number of hours: "))
parking(hours)

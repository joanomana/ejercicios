#Ejercicio 11: Conversion de temperaturas
print("Exercise 11")

def convertir_temperatura(temp,x):
    match x:
        case "c":
            new_temp = temp * (9/5)+32
            print(f"The temperature in Fahrenheit is: {new_temp}")
        case "f":
            new_temp = (temp - 32) * (5/9)
            print(f"The temperature in Celsius is: {new_temp}")
        case _:
            print("Invalid option")
temp = int(input("Enter the temperature: "))
x = input("Enter the unit of temperature (c or f): ")
convertir_temperatura(temp,x)
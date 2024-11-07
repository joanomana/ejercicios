#Ejercicio 12: Calculadora de IMC
print("Exercise 12")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
imc = weight / height ** 2
if imc < 18.5:
    print("Underweight")
elif imc <= 24.9:
    print("Normal weight")
elif imc <= 29.9:
    print("Overweight")
else:
    print("Obesity")   

print(imc)
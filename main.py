#Ejercicio 14: Calculo salario neto

print ("Exercise 15")
print("")
print("Calculate your net salary")
salary = float(input("Enter your salary: "))
country = input("Enter your country (A,B,C) countries that are not on the list are calculated with 25%: ")

if country.upper() == "A":
    print("A payment of 20% in taxes is made ")
    discount = salary * 0.20
    new_salary = salary - discount
    print(f"Your new salary is: {new_salary}")
elif country.upper() == "B":
    print("A payment of 15% in taxes is made ")
    discount = salary * 0.15
    new_salary = salary - discount
    print(f"Your new salary is: {new_salary}")
elif country.upper() == "C":
    print("A payment of 10% in taxes is made ")
    discount = salary * 0.10
    new_salary = salary - discount
    print(f"Your new salary is: {new_salary}")
else:
    print("A payment of 25% in taxes is made ")
    discount = salary * 0.25
    new_salary = salary - discount
    print(f"Your new salary is: {new_salary}")
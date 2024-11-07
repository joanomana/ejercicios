#Ejercicio Estructuras Iterativas 1: Suma de los N primeros números

print ("Exercise 1")
print("")
nums =[]
n = int(input("Enter a number: "))
if n >= 0:
    for i in range(1,n+1):
        nums.append(i)
print("The sum of the first",n,"numbers is:",sum(nums))




n = int(input("Enter a number: "))
if n >= 0:
    suma = 0
    for i in range(1,n+1):
        suma += i
print("The sum of the first",n,"numbers is:",suma)
#Ejercicio 13: Comparacion de tres numeros
print("Exercise 13")

numbers = []
for i in range(3):
        num = int(input("Enter a number: "))
        numbers.append(num)
if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
        print(f"The number {numbers[0]} is the greatest")
elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
        print(f"The number {numbers[1]} is the greatest")
else:
        print(f"The number {numbers[2]} is the greatest")

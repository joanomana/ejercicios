#Ejercicio 8: Determinacion de año biciesto
print("Exercise 8")

year = int(input("Enter a year: "))

if year % 4==0 and (year %100!=0 or year %400 == 0):
    print(f"The year {year} is a leep year")
else:
    print(f"The year {year} is not a leep year")
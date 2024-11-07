#Ejercicio 16: Calculo tiempo de viaje

print ("Exercise 16")
print("")
print("Calculate travel time")

distance = float(input("Enter the distance in km: "))
speed = float(input("Enter the speed in km/h: "))

if distance > 0 and speed > 0:
    if speed > 120:
        print("You are going too fast")
    else:
        pass
    
    time = distance / speed
    if time <1:
        time = time*60
        print("The time it takes to travel is:",round(time), "minutes")
    else:
        entera = int(time)
        minutes = (time - entera)*60
        print("The time it takes to travel is: ", entera, "hours and", round(minutes), "minutes")

    

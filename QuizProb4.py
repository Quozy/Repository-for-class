dest = str(input("Where would you like to travel to? "))
dist = int(input("How far away is " + dest + " in miles? "))
speed = int(input("How fast is the plane in mph? "))
wind = int(input("Is there wind? Use negative to have the wind against you "))

speednew = (speed + wind)
time = (dist/speednew)

print("Your flight will take " + str(time) + " hours.")

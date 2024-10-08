print("You are making a turf field!")
print("Please input the measurments of your field in feet")
l = int(input("What is the length of your field? "))
w = int(input("What is the width of your field? "))
cost = int(input("How much does the turf cost per sq foot? "))

print("Area = " + str(l * w))
print("Perimeter = " + str(l + l + w +w))
print("Total Cost = " + str(l * w * cost))

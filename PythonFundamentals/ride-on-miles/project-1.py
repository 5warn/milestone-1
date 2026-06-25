#Create a python program that asks the user how far they want to travel and suggests an appropriate vehicle.
miles=float(input("How far would you like to travel in miles? "))
if miles<3:
    print("I suggest bicycle to your destination.")
elif miles>3 and miles<300:
    print("I suggest motor-cycle to your destination.")
else:
    print("I suggest Super-car to your destination.")
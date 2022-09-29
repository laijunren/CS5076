'''Write a program that calculates the speed of a car by asking for the distance and the time from the
user. This program should take into account errors that might happen as a result of wrong inputs
(arithmetic error, value error) and asks the user for the correct values.'''

distance = float(input("Enter distance: "))
while distance < 0:
    distance = float(input("Enter correct value for distance (non-negative): "))

time = float(input("Enter time: "))
while time <= 0:
    time = float(input("Enter correct value for time (greater than 0): "))

speed = distance / time
print("Speed: ", speed)
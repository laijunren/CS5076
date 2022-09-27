number = int(input("Enter a number: "))
highest = number

while number != 0:
    if number > highest:
        highest = number
    number = int(input("Enter a number: "))

print("Highest number: ", highest)


# Exercise 1

firstName = input("Please enter your first name: ")
lastName = input("Please enter your first name: ")
age = int(input("Please enter your age: "))
salary = float(input("Please enter your salary: "))
postCode = input("Please enter your post code: ")

print("Your first name is: ", firstName)
print("Your first name is: ", lastName)
print("Your first name is: ", age)
print("Your first name is: ", salary)
print("Your first name is: ", postCode)

# Exercise 2

word = input("Please enter a word: ")
number = int(input("Please enter the numebr of times to be repeated: "))

print((word + " ") * number)

# Exercise 3

number = int(input("Please enter a number: "))

print("The number is", number)
print("Double the number is", number * 2)
print("Triple the number is", number * 3)
print("Half the numebr is", number / 2)
print("Result int division by 3 is", number // 3)
print("Remainder of division by 3 is", number % 3)

# Exercise 4

salary = float(input("Please enter your yearly salary: "))

monthlySalary = salary / 12
monthlySalaryTaxed = monthlySalary * 0.80          # This is equivalent to 20%     

print("Your monthly salary before tax is ", monthlySalary)
print("Your monthly salary after tax is", monthlySalaryTaxed)

# Exercise 5

length = float(input("Please enter the length of a rectangle: "))
width = float(input("Please enter the width of a rectangle: "))

print("The area of a triangle is", length * width)

# Exercise 6

side = float(input("Please enter the side of a square: "))

print("The area of a square is", side * side)
print("The perimeter of a square is", side * 4)

# Exercise 7

time = int(input("Please enter time in seconds: "))

print("Distance that light travels in ", time, "sec is", time * 300000000 , "metres")
print("Distance that light travels in ", time, "sec is", (time * 300000000) / 1000 , "km")
print("Distance that light travels in ", time, "sec is", (time * 300000000) / 1609 , "miles")

# Exercise 8

inchesInFeet = 12
cmInInches = 2.54

print("Please enter your height in inches and feet seperately")
feet = int(input("Number of feet: "))
inches = int(input("Number of inches: "))

cm = (feet * inchesInFeet + inches) * cmInInches

print("Your height in cm is: ", cm)















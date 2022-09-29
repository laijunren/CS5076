# Exercise 2
"""Create a program that reads integers from the user until a 0 is entered. Once all of the integers have
been read your program should display all of the positive numbers, followed by all of the negative
numbers. Your program should display each value on its own line."""

positive_numbers = []
negative_numbers = []
num = int(input("Enter a number:"))
while num != 0:
    if num > 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)
    num = int(input("Enter a number:"))
for num in positive_numbers:
    print(num)
for num in negative_numbers:
    print(num)

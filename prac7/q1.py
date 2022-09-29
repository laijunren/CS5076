# Exercise 1
"""Write a program that generates two random number between 0 and 999 and asks the user for the
result of adding the two numbers. If the answer is correct then it should congratulate the user,
otherwise it should ask the user to try again."""

import random
num1 = random.randint(0,999)
num2 = random.randint(0,999)
print("What is" + str(num1) + "+" + str(num2)+"?")
answer = int(input())
if answer == num1 + num2:
    print("Correct!")
else:
    print("Incorrect,please try again.")

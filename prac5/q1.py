sum_positive_number = 0
negative_number_quantities = 0

numbers = 20
for i in range(numbers):
    number_input = int(input(f'Enter number #{i+1}: '))
    if number_input > 0:
        sum_positive_number += number_input
    elif number_input < 0:
        negative_number_quantities += 1

print('Sum of positive numbers: ', sum_positive_number)



"""A particular zoo determines the price of admission based on the age of the guest. Guests 2 years of
age and less are admitted without charge. Children between 3 and 12 years of age cost £14.00. Seniors
aged 65 years and over cost £18.00. Admission for all other guests is £23.00."""

total_cost = 0

age = int(input("Enter an age: "))
while age != "":
   if age <= 2:
       cost = 0
   elif age >= 3 and age <= 12:
       cost = 14
   elif age >= 65:
       cost = 18
   else:
       cost = 23
   total_cost += cost
   print("The cost for a person aged " + str(age) + " is $" + str(cost))
   age = int(input("Enter an age: "))

if total_cost == 0:
    print("There is no charge for this group.")
else:
    print("The total cost for the group is $" + str(total_cost))


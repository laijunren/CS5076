1.
person = {
    'first_name': 'Junren',
    'last_name':  'Lai',
    'age': 23,
    'city': 'XIAMEN',
    'salary': '$10000',
    'post code': '366300',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print(person['salary'])
print(person['post code'])

2.
a_string = "Good"
for line in range(3):
    result = a_string * 2
    print(result)

3.
num = int(input("Enter a number:"))
print("The number is:", num)
print("The number double is:", num*2)
print("The number triple is:", num*3)
print("The number halved is:", num/2)
print("The number divided by 3 is:", num//3)
print("The remainder of the division is:", num%3)

4.
yearly_salary = int(input("Please enter your yearly salary:"))
print("Your monthly salary before tax is:", (yearly_salary/12)*0.8)
print("Your monthly salary after tax is:", (yearly_salary/12)*0.6)


5.
w = int(input("Enter the width of the rectangle: "))
h = int(input("Enter the height of the rectangle: "))
area = w*h
print("area of the rectangle is: %.2f" % area)

6.
num = float(input("Enter the side length: "))
side = float(input())
perimeter = 4*side
area = side*side
print("\nArea = {:}". format(area))
print("\nPerimeter = {:}". format(perimeter))

7.
time = float(input("Enter the time in second: "))
speed = 3 * 10 ** 8
distance = speed * time
meters = distance
kilometers = meters/1000
miles = kilometers * 0.621
print("The distance in meters is: %2.f" % meters)
print("The distance in Kilometers is: %2.f" % kilometers)
print("The distance in miles is: %2.f" % miles)

8.
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches:"))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)

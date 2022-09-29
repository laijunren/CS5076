def is_triangle(x,y,z):
    if(x>y+z) or (y>x+z) or (z>x+y):
        print("No")
    else:
        print("Yes")
x=int(input("Enter the length of the first stick: "))
y=int(input("Enter the length of the second stick: "))
z=int(input("Enter the length of the third stick: "))
is_triangle(x,y,z)
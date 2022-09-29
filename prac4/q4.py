def median(a,b,c):
    if b<a and a<c:
        median = a
    elif c<a and a<b:
        median = a
    elif c<b and b<c:
        median = b
    elif a<b and b<c:
        median = b
    else:
        median = c
    return median
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print("The median is",median(a,b,c))

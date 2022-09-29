def gcd(x,y):
    r = x%y
    if r !=0:
        x = y
        y = r
        r = x%y

    return r
x = int(input("enter x: "))
y = int(input("enter y: "))

print(gcd(x,y))
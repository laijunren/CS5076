def checkFermat(a,b,c,n):
    if n <= 2:
        return
    else:
        if a**n + b**n == c**n:
            print("Holy smokes,Fermat was wrong!")
        else:
            print("No,that doesn't work.")

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
n=int(input("Enter n: "))
checkFermat(a,b,c,n)

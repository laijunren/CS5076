def month_date(day, month, year):
    if day*month == year:
        return True
    else:
        return False

day=int(input("Enter a day: "))
month=int(input("Enter a month: "))
year=int(input("Enter a year: "))

check = month_date(day, month, year)
if(check == True):
    print("The date is magic!")
else:
    print("The date is not magic!")





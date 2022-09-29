month = input("Enter name of month: ")

if month =="Feb":
    print("Number of day :28 or 29 days.")
else:
    if month == "Jan" or month == "Mar" or month == "May" or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
        print("Number of days: 31 days.")
    else:
        print("Number of days: 30 days.")
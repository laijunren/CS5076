average = 0
for days in range(7):
    print("Enter temperature for day", days+1)
    weather = float(input())
    average += weather
s=average / 7

print("Average temperature for the week: ", s)

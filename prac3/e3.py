room1_length = float(input("Enter length of room1: "))
room1_width = float(input("Enter width of room1: "))

room2_length = float(input("Enter length of room2: "))
room2_width = float(input("Enter width of room2: "))

room1_area = room1_length * room1_width
room2_area = room2_length * room2_width

if room1_area == room2_area:
    print("Both rooms have the same area.")
else:
    if room1_area > room2_area:
        print("Room1 area is bigger than room2.")
    else:
        print("Room2 area is bigger than room1.")
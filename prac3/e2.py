letter = input("Enter a letter: ")

if letter in ['a','e','o','i','u']:
    print(f"{letter} is a vowel letter.")
elif letter in ['Y','y']:
    print("y sometime it's a vowel letter.")
else:
    print(f"{letter} is a constant letter.")

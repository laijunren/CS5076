def compare_ages():
    my_age = 18
    user_age = int(input("Please enter your age: "))
    if user_age < my_age:
        if my_age - user_age == 1:
            print("You are one year younger than me.")
        else:
            print("You are", my_age - user_age, "years younger than me.")
    elif user_age > my_age:
        if user_age - my_age == 1:
            print("You are one year older than me.")
        else:
            print("You are", user_age - my_age, "years older than me.")
    else:
        print("You are the same age as me.")
compare_ages()

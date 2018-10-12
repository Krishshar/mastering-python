age = input("How old are you: ")
if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but cannot drink")
    elif age >= 21:
        print("You can enter, and you can drink")
    else:
        print("No! you cannot enter, littlebit")
else:
    print("You didn't mention your age");

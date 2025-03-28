print("Welcome to the rollercoaster!!")
height = float(input("Please enter your height in cm?\n"))
age = int(input("What is your age?:-\n"))
bill = 0
if height >=120:
    if age <= 12:
        bill = 5
        # in this section we can use as many elif condition between the if and else
        print("Child ticket is RS :- 5")
    elif age <=18:
        bill = 7
        print("Youth ticket is Rs :- 7")
        # under this else section
    else:
        bill = 12
        print("Adult ticket is Rs :- 12")

    photo = input("Do you want photo type y for Yes n for No:-\n")
    if photo == "y":
        bill += 3

    print(f"Your final bill is :- {bill}")

else:
    print("Sorry You can't Ride")
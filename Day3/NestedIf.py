print("Welcome to the rollercoaster!!")
height = float(input("Please enter your height in cm?\n"))
age = int(input("What is your age?:-\n"))
if height >=120:
    if age <= 12:
        # in this section we can use as many elif condition between the if and else
        print("You are eligible to ride you have to pay RS :- 5")
    elif age <=18:
        print("You are eligible to ride. You have to pay Rs :- 7")
        # under this else section
    else:
        print("You are eligible to ride. You have to pay Rs :- 12")

else:
    print("Sorry You can't Ride")
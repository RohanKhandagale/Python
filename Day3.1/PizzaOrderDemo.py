print("Welcome To Rohan's Pizza Shop")
size = input("What size pizza do you want?s,m or L:-\n")
pepperoni = input("Do you want pepperoni on your pizza? y or n:-\n")
extra_cheese = input("Do you want extra cheese? y or n:-\n")
bill = 0
if size == "S":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print("Please press valid key.")

    # in this section we code on pepperoni
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

    # in this section we code on extra cheese
if extra_cheese == "y":
    bill +=1

print(f"your final bill is {bill}")

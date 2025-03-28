print('''
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
''')
print("Welcome to treasure Island")
print("Your Mission to find the Treasure.")
road = input("You're at a cross road. Where do you want to go.Type left or right\n").lower()
if road == "left":
    lake = input('You\'ve come to lake there is an island in the middle of the lake '
                 'Type "Wait" for a boat. Type "Swim" for to swim across.\n').lower()
    if lake == "wait":
        house = input("You arrived at the island unharmed. There is a house with 3 doors."
                      "one red, one yellow, one blue.which door do you choose\n").lower()
        if house == "red":
            print("Room of full fire. Game Over")
        elif house == "blue":
            print("Room of snakes. Game Over")
        elif house == "yellow":
            print("You found the treasure. You win")
        else:
            print("You choose a door that doesn't exist. Game over")
    else:
        print("You died cuz of the lake is full of crocodile. Game Over")
else:
    print("You Died in accident. Game over")



# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# click on the above link and write a code for robot to complete the race

# solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()

turn_around()
turn_around()
turn_around()
turn_around()
turn_around()
turn_around()

# Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
# Make him run the course, following a path similar to the one shown, 
# but stopping at the only flag that will be shown after the race has started.
# Hurdle2 solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    turn_around()


# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# Hurdel3 solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
       turn_around()
    else:
        move()

# Maze Program Comeback after 15
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

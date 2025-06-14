import random

def start_game():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 to 100.")
    mode = input("choose a difficulty. Type 'easy' or 'hard'.:-").lower()

    if mode == 'easy':
        easy_mode()
    elif mode == 'hard':
        hard_mode()
    else:
        print("Invalid choice.")

def easy_mode():
    random_num = random.randint(1,100)
    attempt = 10
    print("you choose easy mode you have 10 choice to guess the number")

    while attempt > 0:
        guesss = int(input(f"guess the number you have({attempt} chance left):-"))

        if guesss < random_num:
            print("Too Low! Try again.")
        elif guesss > random_num:
            print("Too High! Try again.")
        else:
            print(f"Congratulation! You have guessed correct number.{random_num}")
            break
        attempt -= 1
    if attempt == 0:
        print(f"Sorry You have run out of attempts. The correct number was {random_num}")
def hard_mode():
    random_num = random.randint(1,100)
    attempt = 5
    print("You choose hard mode. You have 5 attempts to guess the number.")

    while attempt > 0:
        guesss = int(input(f" Guess the number. You have ({attempt} chance left):- "))

        if guesss < random_num:
            print("Too Low! Try again.")
        elif guesss > random_num:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You  have guessed correct number.{random_num}")
            break
        attempt -=1
    if attempt == 0:
        print(f"Sorry You have ran out of attempts. The correct number was {random_num}")

start_game()

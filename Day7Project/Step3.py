import random
word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

# placeholder

placeholder = ""
word_length = len(chosen_word)
for place in range(word_length):
    placeholder += "_"
print(placeholder)

# for correct guess
game_over = False

# store a correct guess letter
correct_letters = []



while not game_over:
    guess = input("Guess a letter:-")

    display = ""


    # comparing guess with chosen
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display +="_"

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print("You Win")
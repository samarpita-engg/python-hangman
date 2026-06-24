print("Welcome to Hangman!")

import random

word_list = ["aardvark", "baboon", "camel", "clock", "music", "weekend"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)
correct_letters = []

game_over = False 

while not game_over:
    guess = input("Guess a letter that might be in the word:\n").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.") 
print("Welcome to Hangman!")

import random

word_list = ["aardvark", "baboon", "camel", "clock", "music", "weekend"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter that might be in the word:\n").lower()

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
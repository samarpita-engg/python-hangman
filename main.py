print("Welcome to Hangman!")
from hangman_art import logo

print(logo)
import random

from hangman_words import word_list

from hangman_art import stages

lives = 6

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

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
            
    print(display)

    if "_" not in display:
        game_over = True
        print("You win.") 

print(stages[lives])
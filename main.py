print("Welcome to Hangman!")

import random 

from hangman_words import word_list

from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False 
correct_letters = []

while not game_over:
    print("************************************<???>/6 LIVES LEFT************************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

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
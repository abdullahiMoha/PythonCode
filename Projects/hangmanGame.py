
""" 
This is Little HangMan Project, its asking to guess the word
by typing it letters, if its right it continues otherwise it hangs 
one body-part of a man

The game has 6 attempts to guess the letters of the word, 
it will tell how many letters the word consist of then its up to 
you to use your mind or cheat
"""
import random
import os
from Arts.hangman_art import logo, stages


from Data.hangman_word import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
os.system("cls")
# Printing the game logo
print(logo)

# Testing code
# print(f'Pssst, the selected word has {len(chosen_word)}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    # os.system("cls")
    print(f"You have 6 guesses, and now {lives} is remaining ")
    print(
        f"The first letter of the word '{chosen_word[0].upper()}' and it has {len(chosen_word)}")
    guess = input("Guess a letter: ").lower()

    os.system("cls")
    # Checking If the user has entered a letter they've already guessed, print the letter and let them know.
    guessed_word = []
    if guess in display:
        print("Already Gussed")
        continue

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that is not in the word. You lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print("The Word was '{chosen_word}'")

    # Joining all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win. and saved life")

    print(stages[lives])

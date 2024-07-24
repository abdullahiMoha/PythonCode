""" 
This game is asking you to guess anumber between 1 to 100
It has two levels Hard/Easy you can choose btewwen them
The game will give you attempts based your difficulity level 5 for 'Hard' and 10 for 'Easy'
"""

import random
import os

from Arts.guessArt import logo


def PlayGuessGame():
    """The main function of th game"""
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("Thin of a number betwwen 1 to 100")

    level = input("Choose a Difficulty. Type 'easy' or 'hard': ").lower()
    attempt = 0
    number = random.randint(1, 100)
    if level == "hard":
        attempt = 5
    elif level == "easy":
        attempt = 10

    while attempt != 0:
        print(f"You have {attempt} attempts to guess the number")
        guess = int(input("Make a Guess: "))

        if guess < number:
            print("Too low")
            print("Guess again.")
            attempt -= 1
        elif guess > number:
            print("Too hight")
            print("Guess again.")
            attempt -= 1
        elif guess == number:
            print("You win")
            print(f"You choose: {guess} and the number was: {number}")
            attempt = 0


if input("Doyou want to play GUESS_NUMBER Game type 'y' or 'n' to exit: ").lower() == "y":
    os.system("cls")
    PlayGuessGame()

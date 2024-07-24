""" 
The Little project combares between two Entities according 
to their followers, which one has more then the other

It asks you to choose between two options A and B, who you 
think has more followers
"""

import random
import os
from Arts.Higher_Lower_Art import logo, vs
from Data.game_data import data


def get_random_account():
    """Its returnning a random from the data list"""
    return random.choice(data)


def format_data(account):
    """Printing the account into printab;e format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Yaking the guess user make and followers of accounts thne tells if user is right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def who_is_higher(account_1, account_2):
    """finding the higher in terms of followers"""
    if account_1["follower_count"] > account_2["follower_count"]:
        return account_1
    else:
        return account_2


def PlayGame():
    """ 
    The main function of the project, it runs the game
    """

    # clear the screen for fresh start
    os.system("cls")
    # printing the game logo
    print(logo)
    score = 0  # this variable is incremented whenever user chooses correct option
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    # the main go point of the game starts here you can make it function or leave it as its
    while game_should_continue:

        # generating game data
        account_a = who_is_higher(account_1=account_a, account_2=account_b)
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        # printing the names as formated
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        # Asking the user to choose between
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Checking if the user is correct
        # firstly get the followers count of accounts to compare
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # stroring the answer into valiable
        is_correct = check_answer(
            user_guess, a_follower_count, b_follower_count)

        os.system("cls")  # clearing the screen before showing the result
        print(logo)  # printing the logo after the screen is cleared

        # giving the user a feedback
        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, its wrong! Final score: {score}")
            if input("Do you want to play again. Type  'Y' or 'N': ").lower() == "y":
                PlayGame()
            else:
                break


PlayGame()

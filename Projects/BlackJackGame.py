""" 
This game allows the user to pick up a card until he reaches 
the end, also the computer will pick up a card as well then 
you will know who is the winner of the game
"""

import random
import os
from Arts.BlackJackArt import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """It returns random card"""
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """It returns the score of passed cards after calculation"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(user_score, computer_score):
    """Its compres the user score and computer score then gives the winner"""
    if user_score == computer_score:
        return "Draw 😊"
    elif computer_score == 0:
        return "loss, opponent has BlackJack 😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > 21:
        return "You went over. You lose 😁"
    elif computer_score > 21:
        return "Openent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😲"
    else:
        return "You lose 😂"


def play_game():
    """tHE MAIN FUNCTION OF GAME, IT RUNS THE GAME WHEN EVER IT CALLED"""

    # printing game logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # dealing eith user ppick up
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card or 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # dealing with computer pick ups
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"  computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play game BlackJack again? Type 'y' or 'n': ").lower() == 'y':
    os.system("cls")
    play_game()

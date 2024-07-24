""" 
This an Auction App, it allows people to make action by asking
their name and what amount they are willing to buy then it shows
the person with the highest amount and announces that e is the winner
"""
import os
from Arts.BidArt import logo


# printing the system logo
print(logo)
next_bid = True
bid_users = {}
highest_bid = 0
winner = ""

while next_bid:
    name = input("What is your name: ")
    bid = int(input("Enter your bid: $"))
    bid_users[name] = bid
    yes_no = input("Is there any user to bit 'yes' or 'no' ").lower()

    if bid_users[name] > highest_bid:
        highest_bid = bid_users[name]
        winner = name

    if yes_no == "no":
        next_bid = False
    elif yes_no == "yes":
        os.system("cls")

print(f"The winner is '{winner}' has the highest bit of {highest_bid}")
if input("Do you want to see the list 'YES' or 'NO'").lower() == "yes":
    print(bid_users)

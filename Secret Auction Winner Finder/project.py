# Welcome to the secret auction program
# What is your name? : 
# What's your bid? : 
# Are there any other bidders? Type 'yes' or 'no'
# clear entire screen

# if yes : 
# What is your name? : 
# What's your bid? : 
# Are there any other bidders? Type 'yes' or 'no'

# if no 
# The winner James with a bid of $142

# * Secret Bidings : 

from art import logo
import os
print(logo)
print("Welcome to the secret auction program")

# TODO: create a dictionary so each person name --> key && value --> bid
is_bidding_finished = False
bids = {}


def find_heighest_bidder(bids_data):
    heighest_price = 0
    winner = ""
    for name in bids_data:
        bids_amount = bids_data[name]
        if bids_amount > heighest_price:
            heighest_price = bids_amount
            winner = name
    print(f"The winner {winner} with a bid ${heighest_price}")


while not is_bidding_finished:
    name = input("What's your name? : ")
    price = int(input("What's your bid ? :  "))
    bids[name] = price
    bidding_situation = input("Are there are any other bidders? Type 'yes' or 'no'? ")

    if bidding_situation == 'no':
        find_heighest_bidder(bids)
        is_bidding_finished = True
    elif bidding_situation == 'yes':
        os.system('cls')
    else:
        print("You've entered unvalid data - Try again")

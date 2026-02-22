"""
The goal is to build a blind auction program.

Demo
https://appbrewery.github.io/python-day9-demo/

Clearing the Output
There are several ways of clearing the output. The easiest is to simply print "\n" many times so that the output scrolls down many lines.

e.g.

# This will add 20 new lines to the output
print("\n" * 20)
Functionality
Each person writes their name and bid.
The program asks if there are others who need to bid. If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
Each person's name and bid are saved to a dictionary.
Once all participants have placed their bid, the program works out who has the highest bid and prints it.
 Hint 1
Try writing out a flowchart to plan your program.
 Hint 2
The values that come from the input() function are Strings, you'll need to use the int() function to convert it to a number.
Flowchart
If you want to see my flowchart, you can download it here.
"""
from art import logo
# TODO-1: Ask the user for input
more_bidder = True
bids = {}
while more_bidder:
    print(logo)
    user_name = input("What is your name?:  ")
    user_bid = int(input("What is your bid?: $"))
# TODO-2: Save data into dictionary {name: price}
    bids[user_name] = user_bid
# TODO-3: Whether if new bids need to be added
    more_bids = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if more_bids == 'no':
        more_bidder = False
    elif more_bids == 'yes':
        print("\n" * 2000)
    else:
        more_bidder = False

# TODO-4: Compare bids in dictionary

max_item = max(bids, key=bids.get)
print("\n" * 2000)
print(f"And The winner is Mr/Mrs {max_item} with amount of ${bids[max_item]}")



# We're going to build a tip calculator.
#
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay:
#
# (150.00 / 5) * 1.12 = 33.6
#
# After formatting the result to 2 decimal places = 33.60
#
# Demo
# https://appbrewery.github.io/python-day2-demo/
#
# Very Optional Reading: Floating Point Arithmetic
# https://docs.python.org/3/tutorial/floatingpoint.html

# Day 2 Project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final_bill = ( bill + (bill * tip / 100)) / people
print(f"Each person should pay ${round(final_bill, 2)}")

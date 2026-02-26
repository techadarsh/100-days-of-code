# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
#       dispensed. The prompt should show again to serve the next customer.

# TODO: Turn off the Coffee Machine by entering “off” to the prompt
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#     the machine. Your code should end execution when this happens.

# TODO: Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5

# TODO: Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
#    esources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#   not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO: Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
#   prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#   pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
#   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#   program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
#   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places

# TODO: Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.

    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0

    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#   latte was their choice of drink

# 1. Make 3 hot flavour
# types   =>    Espresso,  Latte,  Cappuccino
# water   =>    50 ml,      200 ml, 250 ml
# coffee  =>    18g,        24g,    24g
# milk    =>    -           150ml,  100ml
# price   =>    $ 1.50,     $ 2.50, $3.00

import art
coffee_logo = "☕️"
machine_working = True
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

currency = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

def ask_user():
    """Ask user to enter coffee"""
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def turn_off_machine():
    """Turn off machine"""
    global machine_working
    print("Turn off machine.")
    machine_working = False

def print_report():
    """Print machine resources report to screen"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(coffee_type):
    """Check if machine resources are available"""
    for key in MENU[coffee_type]["ingredients"]:
        if resources[key] < MENU[coffee_type]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
        else:
            return True
    return None

def update_resources():
    """Update machine resources"""

    resources["water"] += int(input("How much Water you want to add: "))
    resources['milk'] += int(input("How much Milk you want to add: "))
    resources['coffee'] += int(input("How many Coffee you want to add: "))

def process_coin(coffee_type):
    """Process coffee and return coffee amount"""
    print(f"Price for {coffee_type} is ${MENU[coffee_type]['cost']}")
    print("Please insert coins.")

    quarter_count = round(float(input("How many quarters?: "))*0.25,2)
    dimes_count = round(float(input("How many dimes?: "))*0.10,2)
    nickles_count = round(float(input("How many nickles?: "))*0.05,2)
    pennies_count = round(float(input("How many pennies?: "))*0.01,2)

    total_amount_inserted = round(quarter_count+dimes_count+nickles_count+pennies_count,2)
    print(f"Amount paid by you is ${total_amount_inserted}")
    if MENU[coffee_type]['cost'] <= total_amount_inserted:
        change_count = round(total_amount_inserted - MENU[coffee_type]['cost'],2)
        if change_count > 0:
            print(f"Here is ${change_count} in change.")
        resources["money"] += MENU[coffee_type]['cost']
        return True
    else:
        print(f"Sorry there is not enough Money. your ${total_amount_inserted} Refunded.")
        return False

def make_coffee(coffee_type):
    """Make coffee"""
    for key in MENU[coffee_type]["ingredients"]:
        resources[key] = int(resources[key]) - int(MENU[coffee_type]["ingredients"][key])

    print(getattr(art, coffee_type, art.cup))
    print(f"Here is your {coffee_type} {coffee_logo} Enjoy!")

while machine_working:
    coffee_type = ask_user()
    if coffee_type == "off":
        turn_off_machine()
    elif coffee_type == "report":
        print_report()
    elif coffee_type == "maintenance":
        update_resources()
    else:
        if check_resources(coffee_type):
            if process_coin(coffee_type):
                make_coffee(coffee_type)

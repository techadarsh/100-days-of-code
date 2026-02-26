"""
The goal is to build the program for a coffee machine.

Program Requirements
Download the PDF for the program requirements here:
https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo

Demo Project
If you right-click on solution.py in the file navigator,
you can "Run solution" without opening the file.
You'll be able to test out the functionality in the output area and refer to the PDF
to confirm all the functionality.
"""

'''
Requirements:

1. Make 3 hot flavour
types   =>    Espresso,  Latte,  Cappuccino
water   =>    50 ml,      200 ml, 250 ml    
coffee  =>    18g,        24g,    24g
milk    =>    -           150ml,  100ml
price   =>    $ 1.50,     $ 2.50, $3.00


2. Print Report.
3. Check resources sufficient ?
4. Process Coins.
5. Check transaction Successful.
6. Make Coffee  

 


'''


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
    for k in ("water", "milk", "coffee"):
        unit = "ml" if k in ("water", "milk") else "g"
        print(f"{k.title()}: {resources[k]}{unit}")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(coffee_type):
    """Check machine resources"""
    for key, required in MENU[coffee_type]["ingredients"].items():
        if resources.get(key, 0) < required:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

def update_resources():
    for k in ("water", "milk", "coffee"):
        add = int(input(f"How much {k.title()} you want to add: "))
        if add < 0:
            print("Cannot add negative amount.")
            return
        resources[k] += add

def process_coin(coffee_type):
    print("Please insert coins.")
    total = 0.0
    for coin, value in currency.items():
        count = int(input(f"How many {coin}?: "))
        total += count * value

    total = round(total, 2)
    cost = MENU[coffee_type]["cost"]

    print(f"Amount paid by you is ${total}")

    if total >= cost:
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded. {total}")
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
    elif coffee_type in MENU:
        if check_resources(coffee_type):
            if process_coin(coffee_type):
                make_coffee(coffee_type)
    else:
        print("Invalid choice. Please select espresso/latte/cappuccino.")

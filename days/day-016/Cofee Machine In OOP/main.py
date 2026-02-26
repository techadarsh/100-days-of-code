from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects
coffee_maker = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = coffee_menu.get_items()
    user_drink = input(f"please select a drink type: ({options}): ")
    if user_drink == "off":
        is_on = False
    elif user_drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(user_drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
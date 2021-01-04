from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_start = True

while is_start:
    options = menu.get_items()
    choice = input(f"Type 'report' to get resource status and 'off' to end the machine.\nWhat would you like? ({options}): ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_start = False
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients  and is_payment_successful:
            coffee_maker.make_coffee(drink)




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

print("Welcome to use the coffee machine, type'report' to check current status or type 'off' to turn off the machine.\n" )
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
choices = ['report', 'espresso', 'latte', 'cappuccino', 'off']

is_start =  True

while is_start:
  choice = input("​What would you like? (espresso/latte/cappuccino): ")

  if choice == "report":
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}\n")
  elif choice not in choices:
    print("Please enter a given name: ")
  elif choice == "off":
    is_start = False
    print("See U next time!")
  else:
    need_money = MENU[choice]['cost']
    use_water = MENU[choice]['ingredients']['water']
    use_milk = MENU[choice]['ingredients']['milk']
    use_coffee = MENU[choice]['ingredients']['coffee']
    is_next = True

    if water < use_water:
      print("Sorry, there is not enough water.")
      is_next = False
    elif milk < use_milk:
      print("Sorry, there is not enough milk.")
      is_next = False
    elif coffee < use_coffee:
      print("Sorry, there is not enough coffee.")
      is_next = False

    while is_next:
      print(f"Your {choice} costs ${need_money}. Please insert coins:")
      quarter = int(input("How many quarters: "))
      dime = int(input("How many dimes: "))
      nickle = int(input("How many nickles: "))
      penny = int(input("How many pennies: "))
      total = 0.25*quarter + 0.1*dime + 0.05*nickle + 0.01*penny

      if total < need_money:
        print("Sorry, that's not enough money. Money refunded.\n")
        total = 0 
        is_next = False
      elif total >= need_money:
        change = float("{:.2f}".format(total - need_money))
        money += need_money
        water -= use_water
        milk -= use_milk
        coffee -= use_coffee
        is_next = False

        print(f"Here is ${change} in change.\n")
        print(f"Here is your {choice} ☕  Enjoy!\n")
"""
Its Coffee-Shop App. it prompts what type of coffe you want then checks
if there is available resource for making coffee if there is no enough resource
it will tell which one is less after that it asks you to enter amount and check the amount
if you enter an amount less than the price of the coffee it prompts a message telling you not enough amount
if everything is fine it will make the coffee for you and gives you back your changes
"""

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

profit = 0

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

next_order = True


def process_coins():
    print("Please enter coins: 🪙")
    quarter = int(input("How many are quarters: "))
    dimes = int(input("How many are dimes: "))
    nickles = int(input("How many are nickel: "))
    pennies = int(input("How many are pennies: "))
    total = 0.25 * quarter + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def process_transaction(order):
    price = MENU[order]["cost"]
    u_cost = process_coins()
    if u_cost >= price:
        changes = round(u_cost, 2) - price
        global profit
        profit += price
        print(f"Here is your ${changes} in change")
        return True
    else:
        return False


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"There is no enough {item}")
            return False
    return True


def make_coffee(order_ingredients):
    for item in drink["ingredients"]:
        resource[item] -= order_ingredients[item]
    print(f"here is your '{ordered_item}'! Enjoy your ☕")


while next_order:

    required_milk = 0
    required_water = 0
    required_coffee = 0
    ordered_item = input("What would you like? (espresso/latte/cappuccino):").lower()

    if ordered_item != "report" and ordered_item != "off":
        required_water = MENU[ordered_item]["ingredients"]["water"]
        required_coffee = MENU[ordered_item]["ingredients"]["coffee"]

        if ordered_item != "espresso":
            required_milk = MENU[ordered_item]["ingredients"]["milk"]

    if ordered_item == "off":
        print("Its Closed! by")
        next_order = False
    elif ordered_item == "report":
        print("Report is here")
        for item in resource:
            print(f"{item} : {resource[item]}")
        print(f"Money:💰 {profit}")
        # next_order = False
    else:
        drink = MENU[ordered_item]
        if is_resource_enough(drink["ingredients"]):
            if process_transaction(ordered_item):
                make_coffee(drink["ingredients"])
            else:
                print("The amount is insufficient")
        else:
            next_order = False

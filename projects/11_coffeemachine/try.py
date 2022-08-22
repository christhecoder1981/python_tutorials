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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from the coins inserted"""
    quarter = int(input("How many quarters?: "))
    quarter *= 0.25
    dime = int(input("How many dimes?: "))
    dime *= 0.10
    nickel = int(input("How many nickels?: "))
    nickel *= 0.05
    penny = int(input("How many pennies?: "))
    penny *= 0.01

    total = quarter + dime + nickel + penny

    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost, 2)
        print(f"Here's your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's no enough money.")
        return False

def make_coffee(drink_name, order_ingredient):
    """Deducts the required ingredients from the resources!"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}!")

is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

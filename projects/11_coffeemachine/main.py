from turtle import clear


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


completed = False

def process_coins(order):
    quarter = int(input("How many quarters?: "))
    quarter *= 0.25
    dime = int(input("How many dimes?: "))
    dime *= 0.10
    nickel = int(input("How many nickels?: "))
    nickel *= 0.05
    penny = int(input("How many pennies?: "))
    penny *= 0.01

    coins = quarter + dime + nickel + penny
    if coins < MENU[order]["cost"]:
        return "Not enough money..."
    rest = coins - MENU[order]["cost"] 
    return f"Here i,s {rest} in change!"

     
def compare_ingredients(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def make_coffee(order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
        return "Here is your coffee!"


    
while not completed:
    order = input("Hi and welcome to the coffee machine! What would you want to order? 'Espresso', 'Cappuccino', or 'Latte' or maybe a 'report': ")

    if order  == "off":
        completed = True
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
            
    else:
        order_ingredient = MENU[order]["ingredients"]
        coffee = MENU[order]
        if process_coins(coffee):
            payment = process_coins()
            make_coffee(coffee)

    completed = True
    
        




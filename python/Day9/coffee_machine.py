

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = .25
DIME = .10
NICKEL = .05
PENNY = .01

def check_resources(drink, resources):
    for ingredient in MENU[drink]["ingredients"]:
        if resources.get(ingredient, 0) < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    print("You have enough resources to make the drink.")
    return True

user_wallet = 0

still_serving = True
while still_serving:


    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_order == 'report':
        for x in resources:
            print(f"{x} = {resources[x]}")
    elif user_order in MENU:
        if check_resources(user_order, resources):
            # TODO: Handle payment here
            print(f"Here is your {user_order}. Enjoy!")
    elif user_order == 'off':
        still_serving = False
        



#TODO off should stop the program --- report should print out available resources

#TODO once they choose a drink they should be prompted to insert coins. How many quarters? etc. AND check resources to see if drink can be made

#TODO check the money was sufficient - if so, give change if necessary and print here is your latte/espresso...

#TODO if $$$ not enough - say so and refund the money - set to 0

#TODO decrement resources appropriately
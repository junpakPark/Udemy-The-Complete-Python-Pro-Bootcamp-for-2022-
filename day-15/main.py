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
    "money": 0,
}

Coin = {
    "penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.1,
    "Quarter": 0.25
}


# 4. Check resources sufficient?
def check_resourse(coffee):
    require = MENU[coffee]["ingredients"]
    for ingredients in require:
        if require[ingredients] > resources[ingredients]:
            print(f"Sorry there is not enough {ingredients}")
            return False     #final
    return True              #final


# 5. Process coins.
def insert_coin():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * Coin["Quarter"]
    dimes = int(input("how many dimes?: ")) * Coin["Dime"]
    nickles = int(input("how many nickles?: ")) * Coin["Nickel"]
    pennies = int(input("how many pennies?: ")) * Coin["penny"]
    return quarters + dimes + nickles + pennies


# 6. Check transaction successful?
def change_calculation(money, coffee):
    if money >= MENU[coffee]["cost"]:
        resources["money"] += MENU[coffee]["cost"]
        change = money - MENU[coffee]["cost"]
        print(f"Here is ${change} in change.")
        return True              #final
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False            #final


# 7. Make Coffee.
def make_coffee(coffee):
    require = MENU[coffee]["ingredients"]
    for ingredients in require:
        resources[ingredients] -= require[ingredients]
    print(f"Here is your {coffee} ☕️. Enjoy!")


while True:
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    # 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_input == 'off':
        break
    # 3. Print report.
    elif user_input == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif user_input in MENU.keys():
        if check_resourse(user_input):
            paid_money = insert_coin()
            if change_calculation(paid_money, user_input):
                make_coffee(user_input)
        # check_resourse(user_input)
        # paid_money = insert_coin()
        # change_calculation(paid_money, user_input)
        # make_coffee(user_input)
    else:
        print("PLZ INPUT CORRECTLY..")
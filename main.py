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
}


def change_ingredients(user_choice):
    for items in resources:
        if check_menu(user_choice, items) != 0:
            resources[items] -= MENU[user_choice]["ingredients"][items]


def check_money(user_choice, money):
    cost = MENU[user_choice]["cost"]
    if cost > money:
        return True
    else:
        return False


def check_menu(user_choice, key):
    if key in MENU[user_choice]["ingredients"]:
        return MENU[user_choice]["ingredients"][key]
    else:
        return 0


def check_resources(user_choice):
    n_water = check_menu(user_choice, "water")
    n_milk = check_menu(user_choice, "milk")
    n_coffee = check_menu(user_choice, "coffee")
    if (n_water <= resources["water"]) and (n_milk <= resources["milk"]) and (n_coffee <= resources["coffee"]):
        return False
    else:
        return True


admin_key = True

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while admin_key:
    user_sel=input("What would you like? (expresso/latte/cappuccino): ").lower()
    print(resources)

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    if user_sel == "off":
        admin_key = False

# TODO: 3. Print report \nMoney: {resources['money']}ml
    if user_sel == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml")
    else:
# TODO: 4. Check resources sufficient?
        resource_status = check_resources(user_sel)
        if resource_status:
            print("Insufficient ingredients")
        else:

# TODO: 5. Process coins
            quarters=int(input("Enter number of quarters? "))
            dimes = int(input("Enter number of dimes? "))
            nickels = int(input("Enter number of nickels? "))
            pennies = int(input("Enter number of pennies? "))
            t_money = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
            print(t_money)

# TODO: 6. Check transaction successful?
            money_status = check_money(user_sel, t_money)
            if money_status:
                print(f"The cost of the {user_sel} was ${MENU[user_sel]['cost']}")
                print("Insufficient money. Returning money!")
# TODO: 7. Make Coffee.
            else:
                change_ingredients(user_sel)
                print(f"Here is your {user_sel}")
                balance = t_money - MENU[user_sel]["cost"]
                print(f"The cost of the {user_sel} was ${MENU[user_sel]['cost']}. Here is your balance of ${balance}")

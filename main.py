# Mazen Meziad
# Project idea from 100 Days of Code: The Complete Python Pro Bootcamp for 2022

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

# TODO: Check resources sufficient?
def check_resources(order):
    # print(MENU[order]["ingredients"]["water"])
    if resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        if order != "espresso":
            if resources["milk"] < MENU[order]["ingredients"]["milk"]:
                print("Sorry there is not enough milk")
                return False
            else:
                resources["milk"] -= MENU[order]["ingredients"]["milk"]
                resources["water"] -= MENU[order]["ingredients"]["water"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
            return True
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        return True

# TODO: Process coins.
def check_money(q, d, n, p, cost):
    sum_coins = float(q) * 0.25 + float(d) * 0.10 + float(n) * 0.05 + float(p) * 0.01
    return sum_coins - cost

# TODO: Report
def report_money():
    print("Water: ", resources["water"], "ml")
    print("Milk: ", resources["milk"], "ml")
    print("Coffee: ", resources["coffee"], "g")
    print("Money: ", profit)

# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

userIn = ""

# TODO: Turn off the Coffee Machine by entering “off” to the prompt.

while userIn != "off":
    userIn = input("What would you like? (espresso/latte/cappuccino): ")
    print(userIn)

# TODO: Print report
    if userIn == "report":
        report_money()
    else:
        if check_resources(userIn) == False:
            continue
        else:
            print("Please insert the quantity of the following coins:")
            quarters = input("quarters: ")
            dimes = input("dimes: ")
            nickels = input("nickels: ")
            pennies = input("pennies: ")
            calc = check_money(quarters, dimes, nickels, pennies, MENU[userIn]["cost"])
            # TODO: Check transaction successful?
            if calc < 0:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                # TODO: Make Coffee
                print("\nYour change is: ", calc)
                profit += MENU[userIn]["cost"]
                report_money()
                print("\nHere is your", userIn,". Enjoy!")













from secrets import choice


profit = 0

resources = {
        "Water": 300,
        "Milk": 200,
        "Coffee": 100,
        "Money": 0
}

MENU = {
    "espresso": {
        "ingredients": {
            "Water": 50,
            "Coffee": 18,
        },
        "Cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "Water": 200,
            "Milk": 150,
            "Coffee": 24,
        },
        "Cost": 2.5,
    },
    "capuccino": {
        "ingredients": {
            "Water": 250,
            "Milk": 100,
            "Coffee": 24,
        },
        "cost": 3.0,
    }
}



def isSufficientResources(drink):
    isEnough = True

    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            isEnough = False
    return isEnough



def process_coins():
    print("Please inser coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05 
    pennies = float(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    return total

def isTransactionSuccessful(moneyReceived, drinkCost):

    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False


def makeCoffee(drinkName, ingredients):
    
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drinkName}")


repeat = True

while repeat:
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "report":
        print(f"Water: {resources['Water']}ml ")
        print(f"Milk: {resources['Milk']}ml ")
        print(f"Coffee: {resources['Coffee']}g ")
        print(f"Money: ${resources['Money']} ")
    elif answer == "off":
        repeat = False
        print("Goodbye")
    
    else:
        drink = MENU[answer]
        if isSufficientResources(drink["ingredients"]):
            payment = process_coins()
            if isTransactionSuccessful(payment, drink["Cost"]):
                makeCoffee(answer, drink["ingredients"])
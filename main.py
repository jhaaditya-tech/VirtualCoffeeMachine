#Created the Dictionary of the menu items available
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

def resource_check(order_ingredients):
    """Check for the ingredients in the machine, return True for order and False for no order"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f'Sorry, Not Enough {item}. Please see Cashier')
            return False
    return True

def payment():
    """Total Calculation"""
    print("Insert the Coins.")
    total=int(input("How many Quarters?"))*0.25
    total+= int(input("How many Dimes?")) * 0.10
    total+= int(input("How many Nickles?")) * 0.05
    total+= int(input("How many Pennies?")) * 0.01
    return total

def payment_check(money_collected, cost_drink):
    """Return True when Payment is made and return False for insufficient Fund"""
    if money_collected>=cost_drink:
        change=round(money_collected-cost_drink,2)
        print(f"Total Change: {change}")
        global amount_collected
        amount_collected+=cost_drink
        return True
    else:
        print("Insufficient Fund. Please collect your money and try again")
        return False

def coffee(drink_name,order_ingredients):
    """Deduct Ingredients from Resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Please enjoy your {drink_name} form our Cafe")


status=True
amount_collected=0

while status:
    user_choice=input("Choose the flavor: Espresso| Latte| Cappuccino :\t").lower();
    if user_choice=="off":
        status=False
    elif user_choice=="report":
        print(f"Remaining Water: {resources['water']} ml")
        print(f"Remaining Milk: {resources['milk']} ml")
        print(f"Remaining Coffee: {resources['coffee']} g")
        print(f"Amount Collected:  ${amount_collected}")
    else:
        drink=MENU[user_choice]
        if resource_check(drink["ingredients"]):
            collected_amount=payment()
            if payment_check(collected_amount, drink["cost"]):
                coffee(user_choice, drink["ingredients"])




















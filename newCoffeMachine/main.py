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
    "coffee": 70,
    "money": 2.5
}


def promt_user():
    user_input = input("what would you like?")
    if user_input == 'off':
        quit("off")
    if user_input == 'report':
        report()
    else:
        choice = MENU[user_input]
        is_sufficient_resourses(choice["ingredients"], choice)


def is_sufficient_resourses(order_item, choice_item):
    for items in order_item:
        if order_item[items] > resources[items]:
            print(f"sorry not enough resource:{items}")
            promt_user()
        else:
            print(f"Your cost is:{choice_item['cost']}")
            pay_input = input("proceed to pay? Y or N")
            if pay_input == 'N':
                print("Okay....")
                promt_user()
            else:
                pay = payment()
                print(f"You pay :${pay}")
                is_right_payment(choice_item, pay)


def payment():
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_right_payment(choice_item, pay):
    if choice_item["cost"] <= pay:
        change = round(pay - choice_item["cost"], 2)
        print(f"Here is ${change} in change.")
        promt_user()
    else:
        print("sorry thats not enough money")
        promt_user()


def report():
    print(resources)
    promt_user()


promt_user()

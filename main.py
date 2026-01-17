"""
indian coffee machine.
----------------------
a console-based coffee machine start with asking user for which coffee
they like to order, check if there are enough resources available, direct user 
for how many coins were inserted, calculate the change if there are any and evantually
make final coffee. 

features:
- multiple coffee varieties
- ingredient tracking
- coin based payment system
- money balance tracking
- recource availabilitu checks

"""

from main_data import resources, MENU
user_input = ""
balance = 0


def coffee_menu():
    """menu printing.. all type of coffees with their respective cost."""
    print("\n☕ Welcome to the Indian Coffee House!☕")
    print("-"*15 + " Menu " + "-"*15)
    for item in MENU:
        name = item.replace("_", " ").title()
        cost = MENU[item]["cost"]
        print(f"{name.ljust(15)}: ₹{cost}")
    print("-"*30)


def available_resources(resources):
    """what resources do we have in what amount? returns the resources with their values"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    sugar = resources["sugar"]
    cinnamon = resources["cinnamon"]
    cardamom = resources["cardamom"]
    ginger = resources["ginger"]
    dry_ginger = resources["dry_ginger"]
    jaggery = resources["jaggery"]
    pepper = resources["pepper"]

    return f"water: {water}ml \t milk: {milk}ml \t coffee: {coffee}gm \n sugar: {sugar}gm \t cinnamon: {cinnamon}gm \t cardamom: {cardamom}gm \n ginger: {ginger}gm \t dry_ginger: {dry_ginger}gm \t jaggery: {jaggery}gm \n pepper: {pepper}gm"


def required_resources(choice):
    """what resources will be required for making user's coosen coffee?"""
    ingredients = MENU[choice]["ingredients"]
    return {
        "water": ingredients.get("water", 0),
        "milk": ingredients.get("milk", 0),
        "coffee": ingredients.get("coffee", 0),
        "sugar": ingredients.get("sugar", 0),
        "cinnamon": ingredients.get("cinnamon", 0),
        "cardamom": ingredients.get("cardamom", 0),
        "ginger": ingredients.get("ginger", 0),
        "dry_ginger": ingredients.get("dry_ginger", 0),
        "jaggery": ingredients.get("jaggery", 0),
        "pepper": ingredients.get("pepper", 0),
    }


def coin_processing():
    """calculate and returns the total of all coins inserted."""
    coin1 = int(input("how many were 1(₹) coins "))
    coin2 = int(input("how many were 2(₹) coins "))
    coin5 = int(input("how many were 5(₹) coins "))
    coin10 = int(input("how many were 10(₹) coins "))
    coin20 = int(input("how many were 20(₹) coins "))
    return (coin1*1) + (coin2*2) + (coin5*5) + (coin10*10) + (coin20*20)


def making_coffee(required, available):
    """to check wether we do have required resources for making user coffee?"""
    for item in required:
        if required[item] > available.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """chech wether transaction was successful or money refunded?"""
    if money_received < drink_cost:
        print("Your total money won't cover cost of selected coffee. Money refunded.")
        return False

    else:
        money_received >= drink_cost
        change = money_received - drink_cost
        print(f"\nHere's your ₹ {change} change.")
        global balance
        balance += drink_cost
        return True


turned_off = False
while not turned_off:
    coffee_menu()
    user_choice = input(
        "what would you like? (espresso / latte / cappuccino etc...) ").lower().replace(" ", "_")

    if user_choice == "off":
        turned_off = True

    elif user_choice == "report":
        print("\n📊 Machine Report")
        print("-"*30)
        print(f"{'water'.ljust(10)}: {resources['water']}ml")
        print(f"{'milk'.ljust(10)}: {resources['milk']}ml")
        print(f"{'coffee'.ljust(10)}: {resources['coffee']}gm")
        print(f"{'sugar'.ljust(10)}: {resources['sugar']}gm")
        print(f"{'cinnamon'.ljust(10)}: {resources['cinnamon']}gm")
        print(f"{'cardamom'.ljust(10)}: {resources['cardamom']}gm")
        print(f"{'ginger'.ljust(10)}: {resources['ginger']}gm")
        print(f"{'dry_ginger'.ljust(10)}: {resources['dry_ginger']}gm")
        print(f"{'jaggery'.ljust(10)}: {resources['jaggery']}gm")
        print(f"{'pepper'.ljust(10)}: {resources['pepper']}gm")

        print(f"\nMoney: ₹ {balance}")

    elif user_choice in MENU:
        user_coffee = required_resources(user_choice)

        if making_coffee(user_coffee, resources):
            print(
                f"I can make your {user_choice.replace('_', ' ').title()}! Proceeding to payment...")
        else:
            print("Please select a different drink or refill the machine.")
            continue

        cost = MENU[user_choice]["cost"]
        print(f"total amount that need to pay: ₹ {cost} ")
        print("-"*30)
        print("💰 Please insert the coins. 1, 2, 5, 10, 20 ")
        money = coin_processing()

        if is_transaction_successful(money, cost):
            for item in user_coffee:
                resources[item] -= user_coffee[item]

            print(
                f"☕✨ Here is your {user_choice.replace('_', ' ').title()}. Enjoy! ☕")

    else:
        print("❌ Invalid choice. please try again.")

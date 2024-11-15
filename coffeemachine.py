from hangmanart import *

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 500,
            "coffee": 500,
            "money": 50,
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    def is_resources_sufficient(self, drink):
        for ingredient, amount in MENU[drink]['ingredients'].items():
            if amount > self.resources[ingredient]:
                print(f"Insufficient {ingredient}.")
                return False
        return True

    def process_coins(self):
        money_quarter = int(input("Input total amount of quarter: ")) 
        money_dime = int(input("Input total amount of dime: ")) 
        money_nickel = int(input("Input total amount of nickel: ")) 
        money_penny = int(input("Input total amount of penny: "))
        total = (money_quarter * 0.25 +
                money_dime * 0.10 +
                money_nickel * 0.05 +
                money_penny * 0.01)
        print(f"You entered a total of: ${total:.2f}")
        return total

    def make_coffee(self, drink):
        for ingredient, amount in MENU[drink]['ingredients'].items():
            self.resources[ingredient] -= amount
        self.resources['money'] += MENU[drink]['cost']

    def serve_drink(self, drink):
        print(f"Here is your {drink}, enjoy!")

class Drink:
    def __init__(self, name):
        self.name = name
        self.ingredients = MENU[name]['ingredients']
        self.cost = MENU[name]['cost']

def main():
    coffee_machine = CoffeeMachine()

    while True:
        drink_name = input("What would you like to get? ").strip().lower()
        if drink_name == "off":
            break
        elif drink_name == "report":
            coffee_machine.report()
        elif drink_name in MENU:
            drink = Drink(drink_name)
            if coffee_machine.is_resources_sufficient(drink.name):
                print(f"The price of {drink.name} is ${drink.cost}")
                user_money = coffee_machine.process_coins()
                if user_money >= drink.cost:
                    coffee_machine.make_coffee(drink.name)
                    coffee_machine.serve_drink(drink.name)
                    if user_money > drink.cost:
                        change = user_money - drink.cost
                        print(f"Your change is ${change:.2f}")
                else:
                    print(f"Insufficient funds; here is your money: ${user_money:.2f}")
        else:
            print(f"Sorry, we don't have {drink_name} on our menu.")

if __name__ == "__main__":
    main()

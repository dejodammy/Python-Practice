from hangmanart import *

def main():
    resources = {
        "water": 500,
        "milk": 500,
        "coffee": 500,
        "money": 50,
        }

    while True:
        drink = str(input("What would you like to get? ")).strip().lower()
        if drink == "off":
            break
        elif drink == "report":
            print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']}")
        elif drink in MENU:
            drink_name = MENU[drink]['ingredients']
            water_ingredent = drink_name['water']
            coffee_ingredent = drink_name['coffee']
            milk_ingredent = drink_name['milk']
            drink_price = MENU[drink]['cost']
            if water_ingredent < resources['water'] and coffee_ingredent < resources['coffee'] and milk_ingredent < resources['milk']:
                print(f"The Price of {drink} is ${drink_price}")
                money_quarter = int(input("Input total amount of quarter: ")) 
                money_dime = int(input("Input total amount of dime: ")) 
                money_nickel = int(input("Input total amount of nickel: ")) 
                money_penny = int(input("Input total amount of penny: "))
                user_money = money_quarter * 0.25 + money_dime * 0.10 + money_nickel * 0.05 + money_penny * 0.01
                if user_money == drink_price:
                    resources['water'] -= water_ingredent
                    resources['coffee'] -= coffee_ingredent
                    resources['milk'] -= milk_ingredent
                    resources['money'] += drink_price
                    print(f"Here is your {drink}, enjoy!")
                elif user_money < drink_price:
                    print(f"Insufficient funds; here is your money: ${user_money}")
                elif user_money > drink_price:
                    change = user_money - drink_price
                    resources['water'] -= water_ingredent
                    resources['coffee'] -= coffee_ingredent
                    resources['milk'] -= milk_ingredent
                    resources['money'] += drink_price
                    print(f"Here is your {drink}, enjoy! \nYour change is ${change:.2f}")
            else:
                print("Insufficient Ingredents")
                break
        else:
            print(f"Sorry we dont have {drink} on our menu")

                    
            

if __name__ == "__main__":
    main()
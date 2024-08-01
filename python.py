# print("Welcome to the Band Name Generator.")
# city = input("What's name of the city you grew up in?\n")
# pet = input("What's your pet's name?\n")
# print(f"Your band name could be {city} {pet} ")

print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
tip_percentage = tip/100 * bill
total_bill = tip_percentage + bill 
people = int(input("How many people to split the bill? "))
cut = total_bill/people
print(f"each person should pay: ${cut:.2f}")

# print(''' 
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/______/_
# ******************************************************************************* ''')
# print("Welcome to Treasure Island.Your mission is to find the treasure.")
# choice1 = input("would you like to go left or right? ")
# if choice1.lower() == "left":
#     choice2 = input("swim or wait? ")
#     if choice2.lower() == "wait":
#         choice3 = input("which door Red, Blue or Yellow? ")
#         if choice3.lower() == "red":
#           print("burned by fire gane over")
#         elif choice3.lower() == "blue":
#           print("eaten by beast Game over")
#         elif choice3.lower() == "yellow":
#           print("You Win!")
#         else:
#             print("Game Over")
#     else:
#         print("Attacked by trout Game Over")
# else:
#     print("fall into the hole game over")

# import random

# random_number = random.random()
# print(f"number is { random_number * 5} ")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][3])

# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
# computer_choice = random.randint(0,2)

# choices = [rock,paper,scissors]
# print(f"you chose: {choices[player_choice]} \ncomputer chose: {choices[computer_choice]}")

# if player_choice == computer_choice:
#     print("IT WAS A DRAW")
# elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
#     print("You won!!")
# else:
#     print("You lost")

# import random
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# symbols =  ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
# number = ["0","1","2","3","4","5","6","7","8","9"]
# print("Welcome to my password generator")
# letter_select = int(input("how many letters do you want "))
# symbols_select = int(input("how many symbols do you want "))
# number_select = int(input("how many numbers do you want "))

# scramble_letter = random.sample(letters,letter_select)
# scramble_symbols = random.sample(symbols,symbols_select)
# scramble_number = random.sample(number,number_select)

# password = scramble_letter + scramble_symbols + scramble_number

# password = ''.join(random.sample(password,len(password)))
# print("Here is your password: ", password)



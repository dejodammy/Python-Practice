# print("Welcome to the Band Name Generator.")
# city = input("What's name of the city you grew up in?\n")
# pet = input("What's your pet's name?\n")
# print(f"Your band name could be {city} {pet} ")

# print("Welcome to the tip calculator!")
# bill = float(input("what was the total bill? $"))
# tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
# tip_percentage = tip/100 * bill
# total_bill = tip_percentage + bill 
# people = int(input("How many people to split the bill? "))
# cut = total_bill/people
# print(f"each person should pay: ${cut:.2f}")

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
# from hangmanart import rock, paper,scissors

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

# # import random
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

# import random
# from hangmanart import stages,  logo

# words = ['table', 'chair', 'book', 'apple']

# def choose_word():
#     """Choose a random word from the list and return it."""
#     return random.choice(words)

# def initialize_game():
#     """Initialize game variables for a new game."""
#     global guess_words, blanks, attempts, guessed_letter
    
#     guess_words = choose_word()
#     blanks = ['_'] * len(guess_words)
#     attempts = 6
#     guessed_letter = set()

# def guess_valid(user_guess):
#     return len(user_guess) == 1 and user_guess.isalpha()

# def update_blanks(letter):
#     global blanks
#     for index, char in enumerate(guess_words):
#         if char == letter:
#             blanks[index] = letter

# def display_status():
#     print(f"Current word status: {' '.join(blanks)}")
#     print(f"Guessed letters: {', '.join(sorted(guessed_letter))}")
#     print(f"Attempts left: {attempts}")
#     print(stages[attempts])

# def main():
#     global attempts, guessed_letter, blanks, guess_words  # Declare global variables
    
#     initialize_game()  # Initialize the game state
    
#     print(logo)
#     print(f"WELCOME TO HANGMAN! HERE IS THE WORD LENGTH: {' '.join(blanks)}")
#     print(stages[6])
    
#     while attempts > 0 and '_' in blanks:
#         user_guess = input("Guess a letter: ").lower()
        
#         if not guess_valid(user_guess):
#             print("Invalid guess. Please enter a single letter.")
#             continue
        
#         if user_guess in guessed_letter:
#             print("You have already guessed that letter.")
#             continue
        
#         guessed_letter.add(user_guess)
        
#         if user_guess in guess_words:
#             update_blanks(user_guess)
#             print("Good guess!")
#         else:
#             attempts -= 1
#             print(f"Wrong guess. You have {attempts} attempts left.")
        
#         display_status()
    
#     if '_' not in blanks:
#         print("Congrats! You have guessed the word.")
#     else:
#         print(f"Game over. The word was {guess_words}.")
    
#     play_again = input("Do you want to play again? Y/N: ").strip().lower()
#     if play_again == 'y':
#         main()  # Restart the game
#     else:
#         print("Thanks for playing!")

# if __name__ == "__main__":
#     main()




# def encrypt(message, shift):
#     encrypted_message = []
#     for char in message:
#         if char.isalpha():
#             # Determine if the character is uppercase or lowercase
#             base = ord('A') if char.isupper() else ord('a')
#             # Shift the character and ensure it wraps around the alphabet
#             encrypted_char = chr((ord(char) - base + shift) % 26 + base)
#             encrypted_message.append(encrypted_char)
#         else:
#             # Non-alphabetic characters remain unchanged
#             encrypted_message.append(char)
#     return ''.join(encrypted_message)

# def decrypt(encrypted_message, shift):
#     decrypted_message = []
#     for char in encrypted_message:
#         if char.isalpha():
#             # Determine if the character is uppercase or lowercase
#             base = ord('A') if char.isupper() else ord('a')
#             # Reverse the shift to decrypt and ensure it wraps around the alphabet
#             decrypted_char = chr((ord(char) - base - shift) % 26 + base)
#             decrypted_message.append(decrypted_char)
#         else:
#             # Non-alphabetic characters remain unchanged
#             decrypted_message.append(char)
#     return ''.join(decrypted_message)

# def main():
#     while True:
#         choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()
#         if choice == "encode":
#             shift = int(input("What is the shift? "))
#             message = str(input("What is the message? "))
#             encrypted = encrypt(message, shift)
#             print(f"Encrypted Message: {encrypted}")
        
#         elif choice == "decode":
#             shift = int(input("What is the shift? "))
#             message = input("What is the message? ")
#             decrypted = decrypt(message, shift)
#             print(f"Decrypted Message: {decrypted}")
        
#         while True:
#             play_again = input("Do you want to go again? (yes or no): ").strip().lower()
#             if play_again == "yes":
#                 break
#             elif play_again == "no":
#                 print("Thanks for playing!")
#                 return  # Exit the program
#             else:
#                 print("Invalid input. Please enter 'yes' or 'no'.")

# if __name__ == "__main__":
#         main()

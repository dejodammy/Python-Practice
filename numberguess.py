


import random
def main():
    print("Welcome to guessin game")
    num_guess = random.randint(1,100)
    difficulty = str(input("Choose a difficulty easy or hard? ")).strip().lower()
    if difficulty == "easy":
        chances = 10
        while chances > 0:
            guess = int(input("Enter a guess: "))
            if guess == num_guess:
                print("Great Job You guessed the right answer")
                break
            elif guess < num_guess:
                print("Guess is too low try higher")
                chances = chances-1
                print(f"Chances left is {chances} ")
            elif guess > num_guess:
                print("Guess is too high try lower")
                chances = chances-1
                print(f"Chances left is {chances} ")
        print(f"You ran  out of chances the correct guess is: { num_guess }")
    elif difficulty == "hard":
        chances = 5
        while chances > 0:
            guess = int(input("Enter a guess: "))
            if guess == num_guess:
                print("Great Job You guessed the right answer")
                break
            elif guess < num_guess:
                print("Guess is too low try higher")
                chances = chances-1
                print(f"Chances left is {chances} ")
            elif guess > num_guess:
                print("Guess is too high try lower")
                chances = chances-1
                print(f"Chances left is {chances} ")
        print(f"You ran  out of chances the correct guess is: { num_guess }")
    play_again = str(input("Do you want to play again? ")).strip().lower()
    if play_again == "yes":
         main()
    else:
        print("Thank You for Playing")
        return
    
if __name__ == "__main__":
    main()
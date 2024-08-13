import random
from hangmanart import *

def check_winner(player_sum, dealer_sum):
    if player_sum > 21:
        return "Dealer wins"  # Player busts
    elif dealer_sum > 21:
        return "Player wins"  # Dealer busts
    else:
        # Both sums are 21 or below, determine who is closer to 21
        if player_sum > dealer_sum:
            return "Player wins"
        elif dealer_sum > player_sum:
            return "Dealer wins"
        else:
            return "It's a tie"

def main():
    print(blackjack)
    deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Hearts
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Diamonds
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Clubs
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10   # Spades
    ]
    
    still_playing =  True
    PotSize =int(input("Enter Total Pot: "))
    while still_playing:        
        user_cards = random.sample(deck,2)
        dealer_cards = random.sample(deck,2)
        initialBet = int(input("Enter Inital bet amount: "))
        print(f"Player one card {user_cards} Dealer card {dealer_cards[0]}")
        user_sum = sum(user_cards)
        while user_sum <= 21 :
            Player_hit = input("Do yount to hit or Stand: ").strip().lower()
            if Player_hit == "hit":
                user_cards.append(random.sample(deck,1)[0])
                player_sum = sum(user_cards)
                print(f"Players cards are {user_cards}")
                print(player_sum)
                if player_sum >= 21:
                    break
            elif Player_hit == "stand":
                user_total = sum(user_cards)
                print(user_total)
                break
        dealer_sum = sum(dealer_cards)
        while dealer_sum < 17:
            dealer_cards.append(random.sample(deck,1)[0])
            print(dealer_cards)
            dealer_sum = sum(dealer_cards)
            print(dealer_sum)
                
        print(f"Player Sum is {player_sum} While Dealer sum is {dealer_sum}")
        result = check_winner(player_sum, dealer_sum)
        if result == "Player wins":
            PotSize += 2 * initialBet
            print(f"You won current potsize is {PotSize}")
        elif result == "Dealer wins":
            PotSize = PotSize - initialBet
            print(f"You Lost current Pot size is {PotSize}")
        else:
            print(f"Its a tie Pot Size remains {PotSize}")
        print(result)  
        end_game = str(input("Are You Still playing Yes or No? ")).strip().lower()
        if end_game == "no":
            print("Thank You For Playing")
            return
        else:
            user_cards = []
            dealer_cards = []
            continue
        
    

if __name__ == "__main__":
    main()
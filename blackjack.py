import random
from hangmanart import *  # Ensure you have this module or comment it out

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
    print(blackjack)  # Ensure blackjack is defined in hangmanart
    deck = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Hearts
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Diamonds
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  # Clubs
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10   # Spades
    ]
    
    still_playing = True
    pot_size = int(input("Enter Total Pot: "))  # Changed variable name to pot_size
    while still_playing:
        user_cards = random.sample(deck, 2)
        dealer_cards = random.sample(deck, 2)
        initial_bet = int(input("Enter Initial bet amount: "))  # Fixed typo in 'Initial'
        print(f"Player's cards: {user_cards}, Dealer's visible card: {dealer_cards[0]}")
        
        user_sum = sum(user_cards)
        player_sum = user_sum  # Ensure player_sum is initialized before use
        
        while player_sum <= 21:
            player_hit = input("Do you want to hit or stand? ").strip().lower()  # Fixed typo 'yount'
            if player_hit == "hit":
                user_cards.append(random.choice(deck))  # Use random.choice instead of sample for a single card
                player_sum = sum(user_cards)  # Update player_sum after hitting
                print(f"Player's cards are {user_cards}")
                print(f"Player's total: {player_sum}")
                if player_sum >= 21:
                    break
            elif player_hit == "stand":
                break  # No need to sum here, already stored in player_sum
        
        dealer_sum = sum(dealer_cards)
        while dealer_sum < 17:
            dealer_cards.append(random.choice(deck))  # Use random.choice
            dealer_sum = sum(dealer_cards)
            print(f"Dealer's cards: {dealer_cards}")
            print(f"Dealer's total: {dealer_sum}")
        
        print(f"Final Player sum: {player_sum}, Dealer sum: {dealer_sum}")
        result = check_winner(player_sum, dealer_sum)
        
        if result == "Player wins":
            pot_size += 2 * initial_bet
            print(f"You won! Current pot size is {pot_size}")
        elif result == "Dealer wins":
            pot_size -= initial_bet
            print(f"You lost! Current pot size is {pot_size}")
        else:
            print(f"It's a tie! Pot size remains {pot_size}")
        
        print(result)  
        end_game = input("Are you still playing? Yes or No? ").strip().lower()
        if end_game == "no":
            print("Thank you for playing!")
            break  # Exit the while loop
        else:
            # Resetting cards for the next round is unnecessary as new cards are drawn in the loop
            continue  

if __name__ == "__main__":
    main()

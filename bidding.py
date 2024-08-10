import os
import platform
from hangmanart import*

def clear_console():
    # For Windows
    if platform.system() == "Windows":
        os.system('cls')
    # For Linux and MacOS
    else:
        os.system('clear')

def main():
    print(gavel)
    item_sold = input("Enter Item being sold: ")
    print(f"The item for sale is: {item_sold}")
    bidders = {}
    
    while True:      
        user = str(input("What is your name: "))
        bid = int(input("Enter your bid amount: "))
        bidders[user] = bid
        more_bidders = str(input("Are there more bidders yes/no: ")).strip().lower()
        if more_bidders == "yes":
            clear_console()
        else:
            break

    while True:
        max_bid = max(bidders.values())
        highest_bidders = [user for user, bid in bidders.items() if bid == max_bid]
        
        if len(highest_bidders) > 1:
            print(f"There is a tie between: {', '.join(highest_bidders)} with a bid of ${max_bid}.")
            for bidder in highest_bidders:
                new_bid = int(input(f"{bidder}, enter your new bid: "))
                bidders[bidder] = new_bid
                clear_console()
        else:
            print(f"The highest bidder is {highest_bidders[0]} with a bid of ${max_bid}.")
            break

if __name__ == "__main__":
    main()

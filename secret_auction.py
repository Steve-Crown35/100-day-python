from secret_auction_module import art
import os
print(art)

print("WELCOME TO SECRET AUCTION!")
all_bidders = {}
name = input("Enter your name\n")
bid = float(input("Enter your bid amount $"))
all_bidders[name] = bid
next_bidder = input("Is there any other bidder? yes or no\n").lower()
while next_bidder == "yes":
    os.system('cls')
    name = input("Enter your name\n")
    bid = float(input("Enter your bid amount $"))
    all_bidders[name] = bid
    next_bidder = input("Is there any other bidder? yes or no\n").lower()

def highest_bidder():
    bids = []
    max_bid = 0.0000000000000999
    for name in all_bidders:
        bids.append(all_bidders[name])
    for bid_amount in bids:
        if bid_amount > max_bid:
            max_bid = bid_amount
    print(max_bid)
    print(bids)

highest_bidder()
print(all_bidders)
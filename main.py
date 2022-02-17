# from art import logo
# print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #let bidding_record = {"Jawad": 222, "Elon":341}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is the {winner} with a bid amount ${highest_bid}")

while not bidding_finished:
    name = input("what is your name:")
    price = int(input("what is your bid: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? type 'Yes' or 'No' \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

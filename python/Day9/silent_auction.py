

still_bidding = True

while still_bidding:
    bidders = {}
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid? $"))
    bidders[name] = bid_amount

    keep_going = input("Are there anymore bidders? yes or no: ").lower()

    if keep_going == "no":
        still_bidding = False
        for key in bidders:
            high_bidder_name = ""
            high_bidder_amount = 0
            if bidders[key] > high_bidder_amount:
                high_bidder_name = key
                high_bidder_amount = bidders[key]
                print(f"The winner is {high_bidder_name} with a bid of ${high_bidder_amount}")
    else:
        still_bidding = True




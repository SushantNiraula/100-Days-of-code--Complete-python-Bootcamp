## We are building a silent auction program where users can bid on items.
## The program will keep track of the bids and determine the highest bidder at the end.
## The program will use a dictionary to store the bids, where the keys are the names of the bidders and the values are their bids.
bid_stop=False
bids={ }
bids_prices=[]
bidders=[]
while not bid_stop:
    
    bidder_name=input("Enter the bidder name: ")
    bid_price=input("Enter the bid cost: $")
    bids[bidder_name]=bid_price
    again=input("do you have another bidder? (Enter Y for yes and N for No)").upper()
    if again=='N':
        bid_stop=True
for key in bids:
    bids_prices.append(bids[key])
    bidders.append(key)

print(f"The winning bidder is: ${bidders[bids_prices.index(max(bids_prices))]}")
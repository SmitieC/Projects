print("Welcome to Silent Auction!")
print("Please enter the item you are putting up for auction:")
item = input("Item: ")
print("Please enter the reserve price.")
reserve = int(input("Reserve: "))
print("We are bidding for {} at a reserve price of ${}.".format(item, reserve))
next_bid = int(input("Next bid: "))
while next_bid != -1:
    if next_bid > reserve:
        reserve = next_bid
    else:
        print("Need a higher bid.")
    print("The highest bid so far is: ${}".format(reserve))
    print("Please enter another bid.")
    next_bid = int(input("Bid: "))
print("The highest bid is: ${}".format(reserve))
if reserve >= next_bid:
    print("{} sold for: ${}".format(item, reserve))
else:
    print("The item did not sell.")

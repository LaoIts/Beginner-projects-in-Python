bidders = []
def addBidder(name, bid):

    dic = {
        "name": name,
        "bid": bid
    }
    bidders.append(dic)

def mostBid(bidders):
    number = 0
    winnerName = ""
    for bidder in bidders:
        if bidder["bid"] > number:
            number = bidder["bid"]
            winnerName = bidder["name"]
    print(f"The winner is {winnerName} with a bid of ${number}")
        


print("Welcome to the secret auction program.")
name = input("What's your name?: ")
bid = int(input("What's your bid?: "))

addBidder(name, bid)


respuesta = input("Are there any other bidders? Type 'yes' or 'no': ")

play = True
while play:
    if respuesta == "yes":
        name = input("What's your name?: ")
        bid = int(input("What's your bid?: "))
        addBidder(name, bid)
        respuesta = input("Are there any other bidders? Type 'yes' or 'no': ")
    elif respuesta == "no":
        play = False
        
    else:
        play = False
        print("??????")

mostBid(bidders)










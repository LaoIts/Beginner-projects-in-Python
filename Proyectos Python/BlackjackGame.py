import random

def plant(myCards, computerCards):

    computerCard2 = random.randint(1,11)
    computerCards.append(computerCard2)

    if sum(myCards) > 21:
        print(f"You lose, your hand {myCards} and computer hand {computerCards}")
    elif sum(myCards) == 21 and sum(computerCards) != 21:
        print(f"You win, your hand {myCards} and computer hand {computerCards}")
    elif sum(myCards) < 21 and sum(computerCards) == 21:
        print(f"You lose, your hand {myCards} and computer hand {computerCards}")
    elif sum(computerCards) > 21:
        print(f"You win, your hand {myCards} and computer hand {computerCards}")
    elif sum(myCards) < sum(computerCards):
        print(f"You lose, your hand {myCards} and computer hand {computerCards}")
    elif sum(myCards) > sum(computerCards):
        print(f"You win, your hand {myCards} and computer hand {computerCards}")
        

def Jugar():
    myCards = []
    computerCards = []
    card1 = random.randint(1,11)
    card2 = random.randint(1,11)
    computerCard = random.randint(1,11)
    computerCards = [computerCard]
    myCards = [card1, card2]

    print(f"Your hand: {myCards}")
    print(f"Computer hand: {computerCards}")


    aCard = True
    while aCard:
        ask = input("Do you want another card? Type 'y' or 'n'")
        if ask == "y":
            card3 = random.randint(1,11)
            myCards.append(card3)
            print(f"Your hand: {myCards}")
            if sum(myCards) > 21:
                aCard = False
                plant(myCards, computerCards)
            elif sum(myCards) == 21:
                aCard = False
                plant(myCards, computerCards)
        elif ask == "n":
            aCard = False
            plant(myCards, computerCards)
            
        else:
            print("What?")

play = True

while play:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == 'y':

        Jugar()
    elif answer == 'n':

        print("Okey :(")
        play = False
    else:
        play = False
        print("Wrong response")












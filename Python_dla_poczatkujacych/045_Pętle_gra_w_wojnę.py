import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace',  'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10',   'Power': 10},
    {'Figure': '9',    'Power': 9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
# print(allCards, len(allCards))

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

player1 = allCards[:12]
player2 = allCards[12:]

print("Player's 1 hand:", player1)
print("Player's 2 hand:", player2)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stock = []
    if card1["Power"] == card2["Power"]:
        while card1 == card2:
            print("THIS IS A WAR!!!111")
            print("POWER OF PLAYER 1's CARD:", card1["Power"], "POWER OF PLAYER 2's CARD:", card2["Power"])
            stock.append(card1)
            stock.append(card2)
            if len(player1) < 2:
                player2.extend(stock)
                player2.extend(player1)
                player1 = []
                print("PLAYER 1 CARDS:", len(player1))
                print("PLAYER 2 CARDS:", len(player2))
                break
            elif len(player2) < 2:
                player1.extend(stock)
                player1.extend(player2)
                player2 = []
                print("PLAYER 1 CARDS:", len(player1))
                print("PLAYER 2 CARDS:", len(player2))
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                print("PL   AYER 1 CARDS:", len(player1))
                print("PLAYER 2 CARDS:", len(player2))
        else:
            if card1["Power"] > card2["Power"]:
                stock.append(card1)
                stock.append(card2)
                player1.extend(stock)
                print("PLAYER 1 WINS")
                print("PLAYER 1 CARDS:", len(player1))
                print("PLAYER 2 CARDS:", len(player2))
            else:
                stock.append(card1)
                stock.append(card2)
                player1.extend(stock)
                print("PLAYER 2 WINS: GET 2 CARDS")
                print("PLAYER 1 CARDS:", len(player1))
                print("PLAYER 2 CARDS:", len(player2))
if len(player1) > len(player2):
    print("PLAYER 1 WON!!!!")
else:
    print("PLAYER 2 WON!!!!")

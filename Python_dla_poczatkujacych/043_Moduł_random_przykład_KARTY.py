import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
allCards = []

for color in colors:
    for figure in figures:
        allCards.append(color + " " + figure)
print(allCards)
random.shuffle(allCards)
print(allCards)
player1 = []
player2 = []

#1 sposób pierwszy rozdawania kart graczom
max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print("Karty gracza 1:", len(player1), player1)
print("Karty gracza 2:", len(player2), player2)

#2 sposób drugi rozdawania kart graczom
player11 = []
player12 = []

player11.append(allCards[:12])
player12.append(allCards[12:])

print("Karty gracza 11:", len(player11), player11)
print("Karty gracza 12:", len(player12), player12)
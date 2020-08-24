suit = input('input a card suit:')
value = input ('input a card value:')

if suit == "diamond" or suit == "heart":
    color = "red"
else:
    color = "black"

if value == "king" or value == "queen" or value =="jack":
    isFaceCard = True
else:
    isFaceCard = False

if color== "red":
    if isFaceCard:
        print("you chose a red face card")
    else:
        print("you chose a red pip card")
else:
    if isFaceCard:
        print("you chose a black face card")
    else:
        print("you chose a black pip card")

from deck import Deck


def main():
    deck1 = Deck("mini")  # Just a few cards
    deck2 = Deck("mini")
    # deck1 = Deck()
    # deck2 = Deck()

    card1 = deck1.deal_one()
    card2 = deck2.deal_one()

    if card1 == card2:
        # 因为还没有告诉 Python 什么叫==，py 只认为如果两个是同一个 object 就是 equal
        print(card1, "and", card2, "are equal")
    else:
        print(card1, "and", card2, "are not equal")
        if (card1 > card2):
            print(card1, "beats", card2)
        else:
            print(card2, "beats", card1)

    print(repr(card1))

    # I'd like to keep counts of identical cards I see
    cards_dict = {}

    if card1 in cards_dict:
        cards_dict[card1] += 1
    else:
        cards_dict[card1] = 1

    if card2 in cards_dict:
        cards_dict[card2] += 1
    else:
        cards_dict[card2] = 1

    print(cards_dict)


main()

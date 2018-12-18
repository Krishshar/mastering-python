import random as rand


class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    @classmethod
    def get_suits(cls):
        return cls.suits

    @classmethod
    def get_values(cls):
        return cls.values


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in Card.get_values()
                      for suit in Card.get_suits()]

    def __repr__(cls):
        return "Deck of {} cards".format(len(cls.cards))

    def _deal(self, num):
        if(self.count() == 0):
            raise ValueError("All cards have been dealt")
        elif(self.count() < num):
            num = self.count()
        if(num == 1):
            return self.cards.pop()
        else:
            list_of_cards = []
            for _ in range(num):
                list_of_cards.append(self.cards.pop())
            return list_of_cards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if(self.count() < 52):
            raise ValueError("Only full decks can be shuffled")
        rand.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)


if __name__ == '__main__':
    deck1 = Deck()
    print(deck1)
    print(deck1.count())
    deck1.shuffle()
    print(deck1.deal_card())
    print(deck1.count())
    print(deck1.deal_card())
    print(deck1.count())
    print(deck1.deal_hand(5))
    print(deck1.count())

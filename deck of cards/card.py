class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, value):
        if(suit not in Card.suits):
            raise ValueError("Suit not applicable")
        if(value not in Card.values):
            raise ValueError("Value not applicable")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    @classmethod
    def get_suits(cls):
        return cls.suits

    @classmethod
    def get_values(cls):
        return cls.values


if __name__ == '__main__':
    card1 = Card("Hearts", "A")
    print(card1)
    print(Card.get_suits())
    print(Card.get_values())
    cards = [value + " of " + suit for value in Card.get_values()
             for suit in Card.get_suits()]
    print(cards)

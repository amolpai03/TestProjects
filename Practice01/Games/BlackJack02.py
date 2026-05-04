import random

class Card:
    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank["rank"]} of {self.suit}"

class Deck:
    def __init__ (self):
        self.cards =[]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
                {"rank" : "A", "value" : 11},
                {"rank" : "2", "value" : 2},
                {"rank" : "3", "value" : 3},
                {"rank" : "4", "value" : 4},
                {"rank" : "5", "value" : 5},
                {"rank" : "6", "value" : 6},
                {"rank" : "7", "value" : 7},
                {"rank" : "8", "value" : 8},
                {"rank" : "9", "value" : 9},
                {"rank" : "10", "value" : 10},
                {"rank" : "J", "value" : 10},
                {"rank" : "Q", "value" : 10},
                {"rank" : "K", "value" : 10},
                ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for i in range(number):
            card_dealt = self.cards.pop(0)
            cards_dealt.append(card_dealt)
        return cards_dealt

    def show_cards(self):
        for card in self.cards:
            print(card)


deck = Deck()
deck.show_cards()
deck.shuffle()
deck.show_cards()
hand = deck.deal(5)
print("*" * 30)
for card in hand:
    print(card)
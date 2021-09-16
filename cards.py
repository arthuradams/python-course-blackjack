import random

suits = ("Clubs", "Hearts", "Spades", "Diamonds")
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
ranks = tuple(values.keys())

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for deck_count in range(0,5):
            for suit in suits:
                for rank in ranks:
                    # This assumes the Card class has already been defined!
                    self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()

    def __str__(self):
        card_list = []
        for card in self.all_cards:
            card_list.append(str(card))
        return "\n".join(card_list)




class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.hand = [] 
        
    def add_card(self,new_card):
        self.hand.append(new_card)
    
    
    def __str__(self):
        card_list = []
        for card in self.hand:
            card_list.append(str(card))
        return f'Player {self.name} has {", ".join(card_list)} with a value of {self.hand_total()}.'

    def hand_total(self):
        total = 0
        ace_found = False
        for card in self.hand:
            if card.rank == "Ace":
                ace_found = True
            total += card.value
        if ace_found and total > 21:
            total -= 10
        return total


        
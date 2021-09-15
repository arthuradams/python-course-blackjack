class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.hand = [] 
        
    def add_card(self,new_card):
        self.hand.append(new_card)
    
    
    def __str__(self):
        card_list = ""
        for card in self.hand:
            card_list += str(card) + " "
        return f'Player {self.name} has {card_list}.'

        
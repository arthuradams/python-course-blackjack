class Player:
    
    def __init__(self,name, show_first_card=True):
        self.name = name
        self.show_first_card = show_first_card
        # A new player has no cards
        self.hand = [] 
        
    def add_card(self,new_card):
        self.hand.append(new_card)
    
    def __str__(self):
        card_list = []
        for card in self.hand:
            if len(card_list) == 0 and not self.show_first_card:
                card_list.append("Face down")
            else:
                card_list.append(str(card))

        outstr = f'{self.name} has {", ".join(card_list)}'

        if self.show_first_card:
            outstr += f" has a value of {self.hand_total()}"

        return outstr

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


        
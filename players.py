class Player:
    
    def __init__(self, name, bank, show=True):
        self.name = name
        self.bank = bank
        self.show = show
        # A new player has no cards
        self.hand = [] 
        self.bust = False
        self.wager = 0
        
    def add_card(self,new_card):
        self.hand.append(new_card)
    
    def __str__(self):
        card_list = []
        for card in self.hand:
            if len(card_list) == 0 and not self.show:
                card_list.append("Face down")
            else:
                card_list.append(str(card))

        outstr = f'{self.name} has {", ".join(card_list)}'

        if self.show:
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

    def play(self,deck):
        player_bust = False
        while True:
            if self.hand_total() > 21:
                print( "Bust" )
                player_bust = True
                break
            choice = input(f"{self.name}, do you want to (H) or (S)tand? ")
            if choice[0].upper() == "S":
                break
            elif choice[0].upper() == "H":
                self.add_card(deck.deal_one())
                print(self)
            else:
                print("Invalid selection")
        return player_bust
    
    def get_wager(self):
        bet = -1
        print(f"{self.name}, you have {self.bank}.")
        while bet < 0:
            while True:
                try: 
                    bet = int(input("How much do you want to wager? "))
                except:
                    print("Please enter a number.")
                else: 
                    break
            if bet > self.bank:
                print(f"You only have {self.bank}")
                bet = -1
            elif bet < 0:
                print("You have to wager a positive amount.")
            elif bet == 0:
                print("Okay, this one is just for fun.")
        
        self.wager = bet
    
    def reset_hand(self):
        self.hand = []




def create_player():
    name = input("What is your name? ")

    while True:
        try: 
            bank = int(input("How much money do you have? "))
        except:
            print("Please enter a number.")
        else: 
            break

    return Player(name, bank, True)

def another_game(name):
    while True:
        another_game = input(f"{name}, do you want to play another hand (Y/N)? ")[0].upper()
        if another_game == "Y":
            return True
        elif another_game == "N":
            return False
        else:
            print("Please enter Y or N")
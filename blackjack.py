import cards
import players

my_deck = cards.Deck()

my_deck.shuffle()

player1 = players.Player("Arthur", True)
dealer = players.Player("Dealer", False)

for num in range(0,2):
    player1.add_card(my_deck.deal_one())
    dealer.add_card(my_deck.deal_one())

print(player1)
print(dealer)

player_bust = False
dealer_bust = False
player_win = False
dealer_win = False

while True:
    if player1.hand_total() > 21:
        print( "Bust" )
        player_bust = True
        break
    choice = input(f"{player1.name}, do you want to (H) or (S)tand: ")
    if choice[0].upper() == "S":
        break
    elif choice[0].upper() == "H":
        player1.add_card(my_deck.deal_one())
        print(player1)
    else:
        print("Invalid selection")

if player_bust:
    print(f"{player1.name} loses")
    print(player1)

dealer.show_first_card = True

while dealer.hand_total() < 17:
    dealer.add_card(my_deck.deal_one())
    print(dealer)

if dealer.hand_total() > 21:
    print("Dealer bust")
    dealer_bust = True
elif player1.hand_total() > dealer.hand_total():
    print( f"{player1.name} wins")
else:
    print( f"{dealer.name} wins")


    
import cards
import players


my_deck = cards.Deck()

my_deck.shuffle()

dealer = players.Player("Dealer", 0, False)

player1 = players.create_player()

while True:
    for num in range(0,2):
        player1.add_card(my_deck.deal_one())
        dealer.add_card(my_deck.deal_one())

    print(player1)
    print(dealer)

    player_bust = False
    dealer_bust = False

    player1.get_wager()

    player_bust = player1.play(my_deck)

    dealer.show = True

    if player_bust:
        print(f"{player1.name} loses {player1.wager}")
        player1.bank -= player1.wager
        print(player1)
        print(dealer)
    else:
        print(dealer)
        while dealer.hand_total() < 17:
            dealer.add_card(my_deck.deal_one())
            print(dealer)
        if dealer.hand_total() > 21:
            print("Dealer bust")
            dealer_bust = True
        if player1.hand_total() > dealer.hand_total() or dealer_bust:
            print( f"{player1.name} wins {player1.wager}")
            player1.bank += player1.wager
        else:
            print( f"{player1.name} loses {player1.wager}")
            player1.bank -= player1.wager

   
    print(f"{player1.name}, you have {player1.bank}.")
    if player1.bank <= 0:
        print(f"{player1.name}, you are broke.")
        break
    if players.another_game(player1.name):
        player1.reset_hand()
        dealer.reset_hand()
        dealer.show = False
        continue
    else:
        print(f"{player1.name}, you leave with {player1.bank}")
        break


    
import cards
import players

my_deck = cards.Deck()

my_deck.shuffle()

player1 = players.Player("Name")
dealer = players.Player("Dealer")

player1.add_card(my_deck.deal_one())

print(player1)
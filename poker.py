import random

def createDeck():
	values = (list(list(range(2, 10)) + ('T J K Q A'.split())))
	suits = '♣ ♦ ♥ ♠'.split()
	deck = ['{0}{1}'.format(str(v), s) for v in values for s in suits]
	random.shuffle(deck)
	return deck, suits
	
def flop_turn_river(deck):
	flop_turn_river = [deck.pop(0) for x in range(5)]
	flop = flop_turn_river[0:3]
	turn = [flop_turn_river[3]]
	river = [flop_turn_river[4]]
	return flop, turn, river
	
def hand_simulator():
	iterations = int(input("How many iterations?: "))
	
def dealer():
	deck, suits = createDeck()
	my_hand = [deck.pop(0), deck.pop(0)]
	print('Your hand: ' + my_hand[0] + " " + " " + my_hand[1] + '\n')

	flop, turn, river = flop_turn_river(deck)

	print('Flop: ' + flop[0] + " " + flop[1] + " " + flop[2])
	print('Turn: ' + turn[0])
	print('River: ' + river[0])
	
	seven_cards = my_hand + flop + turn + river
		
dealer()

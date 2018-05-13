import random, pyperclip
from itertools import product
	
def check_flush(seven_cards, suits):
	ace_high = 'AKQJT98765432'
	flush_suit = ""
	hand_suits = [card[1] for card in seven_cards]
	for suit in suits:
		if (hand_suits.count(suit)) >= 5:
			flush_suit = suit
			sorted_flush_cards = "".join(sorted(set([card[0] for card in seven_cards if card[1] in flush_suit]), key=lambda x: ace_high.index(x[0])))
			if sorted_flush_cards == "AKQJT":
				return "Royal Flush"
			elif check_straight(sorted_flush_cards):
				return "Straight Flush"
			else:
				return "Flush"
	
def check_straight(seven_cards):
	ace_high, ace_low = 'AKQJT98765432', 'KQJT98765432A'
	sorted_cards_AH = "".join(sorted(set([card[0] for card in seven_cards]), key=lambda x: ace_high.index(x[0])))
	sorted_cards_AL = "".join(sorted(set([card[0] for card in seven_cards]), key=lambda x: ace_low.index(x[0])))
	if len(sorted_cards_AH) >= 5:
		for x in range(len(sorted_cards_AH) - 4):
			if (sorted_cards_AH[x:x+5] in ace_high) or (sorted_cards_AL[x:x+5] in ace_low):
				return "Straight"

def check_oaks_and_houses(seven_cards):
	paired = False
	card_values = [card[0] for card in seven_cards]
	for card in set(card_values):
		if card_values.count(card) == 4:
			return "Four of a Kind"
		elif card_values.count(card) == 3:
			rest_of_deck = [card_2 for card_2 in card_values if card_2 != card]
			for other_cards in set(rest_of_deck):
				if rest_of_deck.count(other_cards) >= 2:
					paired = True
			if paired:
				return "Full House"
			else:
				return "Three of a Kind"
				
def check_pairs(seven_cards):
	pairs = 0
	card_values = [card[0] for card in seven_cards]
	for card in set(card_values):
		if card_values.count(card) == 2:
			pairs += 1
	if pairs >= 2:
		return "Two Pair"
	elif pairs == 1:
		return "One Pair"
		
		
def hand_checker(seven_cards, suits):
	hand_type = ""
	if check_flush(seven_cards, suits) == "Royal Flush":
		hand_type = "Royal Flush"
	elif check_flush(seven_cards, suits) == "Straight Flush":
		hand_type = "Straight Flush"
	elif check_oaks_and_houses(seven_cards) == "Four of a Kind":
		hand_type = "Four of a Kind"
	elif check_oaks_and_houses(seven_cards) == "Full House":
		hand_type = "Full House"
	elif check_flush(seven_cards, suits) == "Flush":
		hand_type = "Flush"
	elif check_straight(seven_cards) == "Straight":
		hand_type = "Straight"
	elif check_oaks_and_houses(seven_cards) == "Three of a Kind":
		hand_type = "Three of a Kind"
	elif check_pairs(seven_cards) == "Two Pair":
		hand_type = "Two Pair"
	elif check_pairs(seven_cards) == "One Pair":
		hand_type = "One Pair"
	else:
		hand_type = "High Card"
	return hand_type
	
def create_deck():
	values, suits = 'AKQJT98765432', '♣♦♥♠'
	deck = [''.join(pair) for pair in product(values,suits)]
	random.shuffle(deck)
	return deck, suits
	
def flop_turn_river(deck):
	flop_turn_river = [deck.pop(0) for x in range(5)]
	flop, turn, river = flop_turn_river[0:3], [flop_turn_river[3]],[flop_turn_river[4]]
	return flop, turn, river
	
def dealer():
	iterations = int(input("How many hands should we deal?: "))
	
	hand_types = ["Royal Flush", "Straight Flush", "Four of a Kind",
				  "Full House", "Flush", "Straight", "Three of a Kind", 
				  "Two Pair", "One Pair", "High Card"]
	
	hand_log = {}
	for hand in hand_types:
		hand_log[hand] = 0		
	
	for x in range(iterations):
		deck, suits = create_deck()
		my_hand = [deck.pop(), deck.pop()]

		flop, turn, river = flop_turn_river(deck)
		
		seven_cards = my_hand + flop + turn + river
		
		hand_log[hand_checker(seven_cards, suits)] += 1
		
	for hand in hand_log.keys():
		print("{0}: {1:.4%}".format(hand, hand_log[hand]/iterations))
 
dealer()

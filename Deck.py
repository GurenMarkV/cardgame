import random

class Deck(object):

    def generate_cards(self):
        suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
		names = [ ("Three", 3), ("Four", 4), ("Five", 5), ("Six", 6), ("Seven", 7), 
		("Eight", 8), ("Nine", 9), ("Ten", 10), ("Jack", 11), ("Queen", 12),  
        ("King", 13), ("Ace", 14), ("Two", 15),  ("Joker", 16)]
		cards = []
		for name in names:
			if name[0] == "Joker":
				card = Card(name[0], "Joker", name[1])
				cards.append(card)
				cards.append(card)
				continue
			for suit in suits:
				card = Card(name[0], suit, name[1])
				cards.append(card)
		random.shuffle(cards)
		return cards

class Card(object):

	def __init__(self, name, suit, num):
		self.suit = suit
		self.name = name + " of " + suit
		self.num = num

	def get_suit(self):
		return self.suit

	def get_name(self):
		return self.name

	def get_num(self):
		return self.num





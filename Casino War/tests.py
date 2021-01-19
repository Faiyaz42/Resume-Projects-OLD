#from Card import Card
class Card:
	def __init__(self, rank, suit):
		assert rank in ('2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K', 'A'),'Invalid Rank'  #add small letter
		assert suit in ('H', 'C', 'D', 'S'),'Invalid Suit'    #add small letter
		self.__rank = rank
		self.__suit = suit
	
	def convert_rank(self,rank):
		if rank == 'T':
			return 10
		elif rank == 'J':
			return 11
		elif rank == 'Q':
			return 12
		elif rank == 'K':
			return 13
		elif rank == 'A':
			return 14
		elif rank == '9':
			return 9
		elif rank == '8':
			return 8
		elif rank == '7':
			return 7
		elif rank == '6':
			return 6
		elif rank == '5':
			return 5
		elif rank == '4':
			return 4
		elif rank == '3':
			return 3
		elif rank == '2':
			return 2
		else:
			return ('Invalid Rank')
		
	def get(self):
		if self.__rank.isalpha():
			return self.__rank+self.__suit
		else:
			return str(self.__rank)+self.__suit		
	
	
	def get_rank(self):
		return self.__rank
	
	
	def get_suit(self):
		return self.__suit
	
	def __gt__(self, other):
		if self.__rank == 'T':
			return 10
		elif self.__rank == 'J':
			return 11
		elif self.__rank == 'Q':
			return 12
		elif self.__rank == 'K':
			return 13
		elif self.__rank == 'A':
			return 14
		elif self.__rank == '9':
			return 9
		elif self.__rank == '8':
			return 8
		elif self.__rank == '7':
			return 7
		elif self.__rank == '6':
			return 6
		elif self.__rank == '5':
			return 5
		elif self.__rank == '4':
			return 4
		elif self.__rank == '3':
			return 3
		elif self.__rank == '2':
			return 2
		if self.__rank > other.get_rank:                                  
			return True
		elif self.__rank < other.get_rank:                                 
			return False		
		
		
		
	def __lt__(self, other):
		if self.__rank == 'T':
			return 10
		elif self.__rank == 'J':
			return 11
		elif self.__rank == 'Q':
			return 12
		elif self.__rank == 'K':
			return 13
		elif self.__rank == 'A':
			return 14
		elif self.__rank == '9':
			return 9
		elif self.__rank == '8':
			return 8
		elif self.__rank == '7':
			return 7
		elif self.__rank == '6':
			return 6
		elif self.__rank == '5':
			return 5
		elif self.__rank == '4':
			return 4
		elif self.__rank == '3':
			return 3
		elif self.__rank == '2':
			return 2
		if self.__rank > other.get_rank:                                  
			return False
		elif self.__rank < other.get_rank:                                 
			return True		
	
	
	def __eq__(self, other):
		if self.__rank == 'T':
			return 10
		elif self.__rank == 'J':
			return 11
		elif self.__rank == 'Q':
			return 12
		elif self.__rank == 'K':
			return 13
		elif self.__rank == 'A':
			return 14
		elif self.__rank == '9':
			return 9
		elif self.__rank == '8':
			return 8
		elif self.__rank == '7':
			return 7
		elif self.__rank == '6':
			return 6
		elif self.__rank == '5':
			return 5
		elif self.__rank == '4':
			return 4
		elif self.__rank == '3':
			return 3
		elif self.__rank == '2':
			return 2
		if self.__rank == other.get_rank:                                  
			return True
		elif self.__rank != other.get_rank:                                 
			return False		
	
		
	def __str__(self):
		if self.__rank.isalpha():
			return self.__rank+self.__suit
		else:
			return str(self.__rank)+self.__suit

class Player:
	def __init__(self):
		self.__chips = 0
	
	
	def add_chips(self, chips):
		assert chips >= 0 and isinstance(chips, int),'Invalid chips value'
		self.__chips = self.__chips + chips
				 
		
		
	def remove_chips(self, chips):
		assert chips >= 0 and isinstance(chips, int),'Invalid chips value'
		self.__chips = self.__chips - chips		
	
	
	def get_chips(self):
		return self.__chips

def test_card():
	#Creates a card which is the Ace of Diamonds
	my_card = Card("A", "D")
	
	#tests get function
	assert my_card.get() == "AD", "Invalid card"
	#tests rank function
	assert my_card.get_rank() == "A", "Invalid rank"
	#tests suit function
	assert my_card.get_suit() == "D", "Invalid suit"
	
	#tests a rank convertion function
	assert my_card.convert_rank("A") == 14, "Invalid conversion"
	assert my_card.convert_rank("K") == 13, "Invalid conversion"
	assert my_card.convert_rank("Q") == 12, "Invalid conversion"
	assert my_card.convert_rank("J") == 11, "Invalid conversion"
	assert my_card.convert_rank("T") == 10, "Invalid conversion"
	assert my_card.convert_rank("9") == 9, "Invalid conversion"
	assert my_card.convert_rank("8") == 8, "Invalid conversion"
	assert my_card.convert_rank("7") == 7, "Invalid conversion"
	assert my_card.convert_rank("6") == 6, "Invalid conversion"
	assert my_card.convert_rank("5") == 5, "Invalid conversion"
	assert my_card.convert_rank("4") == 4, "Invalid conversion"
	assert my_card.convert_rank("3") == 3, "Invalid conversion"
	assert my_card.convert_rank("2") == 2, "Invalid conversion"
	
	#tests that the suit has no influence on comparison __eq__
	assert Card("A","D") == Card("A","S") == Card("A","H") == Card("A","C"), "Invalid comparison =="
	
	#tests rank comparison function _gt__
	assert Card("A","H") > Card("K", "H") > Card("2", "S"), "Invalid comparison >"
	
	#tests the __str__ function
	assert str(my_card) == "AD", "Invalid string"
	
	#returns True to sinalize that it has passed all tests	
	return True
test_card()
def test_player():
	player = Player()
	player.add_chips(10)
	assert player.get_chips() == 10,'invalid'
	player.remove_chips(2)
	assert player.get_chips() == 8,'invalid'
	player.add_chips(0)
	player.remove_chips(0)
	player.add_chips(10)
	assert player.get_chips() == 18,'invalid'
	player.remove_chips(12)
	assert player.get_chips() == 6,'invalid'
	return True
test_player()
#def test_table()
	#TODO

g = test_card()
print(g)


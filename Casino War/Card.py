class Card:
	def __init__(self, rank, suit):
		assert rank in ('2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K', 'A'),'Invalid Rank'  #assertion checks
		assert suit in ('H', 'C', 'D', 'S'),'Invalid Suit'   
		self.__rank = rank
		self.__suit = suit
	
	def convert_rank(self,rank):
		if rank == 'T':                #converting rank
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
		if self.__rank.isalpha():                                       #if rank is alphabet,print str with str
			return self.__rank+self.__suit
		else:                                                          #if rank is int,convert int to str and print
			return str(self.__rank)+self.__suit		
	
	
	def get_rank(self):
		return self.__rank
	
	
	def get_suit(self):
		return self.__suit
	
	def __gt__(self, other):
		if self.__rank == 'T':
			return 10
		elif self.__rank == 'J':                                       #conversion for comparison
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
		if self.__rank > other.get_rank:                                  #return true or false 
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
		elif self.__rank == '7':                                        #same as above but for lower than,opposite
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
		elif self.__rank == '8':                                   #same as above but for equal
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
			return True                                           #if equal
		elif self.__rank != other.get_rank:                                 
			return False		
	
		
	def __str__(self):
		if self.__rank.isalpha():
			return self.__rank+self.__suit                           #str
		else:
			return str(self.__rank)+self.__suit
		

from Card import Card
from random import shuffle
#from queue import Queue

class Queue:                                                    #queue class from lecture slides
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)	
	def show(self):
		print (self.items)
	def __str__(self):
		return str(self.items)
	
	
class Table:
	def __init__(self,player_card,dealer_card,discard,shoe,bet):         #initiation
		self.player_card = player_card
		self.dealer_card = dealer_card
		self.__discard = Queue()                         #queue for discard
		self.__shoe = shoe
		self.__bet = bet
		#self.__card1 = self.__shoe.dequeue()

	def get_shoe(self):
		return self.__shoe                           #returns the current state of shoe

	def set_cards(self):                                           #set card for both players
		card1 = self.__shoe.dequeue()                      #gets a deck from queue
		self.player_card = card1.pop()                  #getiing a card for each
		self.dealer_card = card1.pop()


	def resolve_round(self, player, dealer):                                                             #get player and dealer ranks and compare ,and output appropriately
		if player.convert_rank(player.get_rank()) > dealer.convert_rank(dealer.get_rank()):
			return 1
		elif player.convert_rank(player.get_rank()) < dealer.convert_rank(dealer.get_rank()):
			return -1
		elif player.convert_rank(player.get_rank()) == dealer.convert_rank(dealer.get_rank()):
			return 0


	def set_bet(self, bets):                                                                   #set a positive integer bet that is even num
		assert bets > 0 and isinstance(bets, int),'Bet must be positive integer.'
		assert bets % 2 == 0,'Bet must be an even number.'
		self.__bet = bets


	def get_bet(self):
		return self.__bet                                  #get current bet


	def enque_discard(self,num):                                     #insert in discard queue
		card1 = self.__shoe.dequeue()                   #discards a card and insert it to self.discard
		for i in range(0,num):
			self.__discard.enqueue(card1.pop())

	def clear(self): 
		card1 = self.__shoe.dequeue()                     
		#print(self.__shoe.size())
		for items in range (0,self.__shoe.size()):                         #clear deck and the table
			self.__discard.enqueue(card1.pop())
		#print (self.__discard.qsize())	


	def create_deck(self):                                                  #list of a fresh deck
		suit = ['H', 'C', 'D', 'S']
		rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K', 'A']
		self.__deck = [Card(ranks,suits) for ranks in rank for suits in suit]
		return self.__deck


	def validate_deck(self, deck):               
		suit = ['H', 'C', 'D', 'S','h','c','d','s']
		rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T','J', 'Q', 'K', 'A','t','j','q','k','a']
		for card in deck:
			assert card.get_suit() in suit,'Invalid suit'              #check if suit is in the suit list
			assert card.get_rank() in rank,'Invalid rank'              #check '' rank '' '' '' rank list

	def get_player_card(self):
		return self.player_card                    #retrun player card
	def get_dealer_card(self):
		return self.dealer_card             #return current dealer card

	def make_shoe(self):
		six_decks = []
		for i in range(1,7):                              #create a deck 6 times and add to six deck list
			six_decks.append(self.create_deck())
		for decks in six_decks:                             #validate each deck in the above list
			self.validate_deck(decks)
		for deck in six_decks:                           #shuffle each deck in above list
			shuffle(deck)		
		Queue1 = Queue()                      #create 2 queues
		Queue2 = Queue()
		i=0
		while i<3:
			Queue1.enqueue(six_decks[i])            #insert first 3 in one queue
			i = i + 1
		j=3
		while j<6:
			Queue2.enqueue(six_decks[j])           #insert last 3 in 2nd queue
			j = j + 1

		Queue3 = Queue()
		for t in range(0,3):
			list1 = []
			list2 = []			
			deck1 = Queue1.dequeue()                   #get a deck from ech queue
			deck2 = Queue2.dequeue()
			e = 26
			for y in range(0,e):                      #take first half from each deck and add to list 1
				list1.append(deck1[y])
				list1.append(deck2[y])
				list2.append(deck1[e])          #take 2nd half from each deck and add to list2
				list2.append(deck2[e])
				e = e + 1
			shuffle(list1)               #shufle the lists
			shuffle(list2)
			Queue3.enqueue(list1)                #insert the lists in queue 3
			Queue3.enqueue(list2)
		self.__shoe = Queue3
		return self.__shoe                  
			
				
			 
		
	
	

		
		

	


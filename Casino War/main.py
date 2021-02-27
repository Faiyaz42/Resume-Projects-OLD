import pickle
from Player import Player
from Table import Table
from queue import Queue
from Card import Card


def main():
	Play = True
	player = Player()
	table = Table(None,None,None,None,None)
	bets = []
	plays = 0                                                           #initiation
	win_count = 0
	play_count = []
	war_count = 0
	table.make_shoe()                  #make shoe
	table.enque_discard(1)                      #discard first card
	
	print('\nWelcome to Casino War\n')
	while Play:                                              #global loop
			user_input = input('You currently have %d chips.\nWhat would you like to do? \nPlay(P) \nBuy chips(B) \nQuit(Q):' % (player.get_chips()))
			
			if user_input == 'B' or user_input == 'b':                                   #if buy
				user_buy = input('How many chips would you like to buy?(1-1000): ')
				user_buy = int(user_buy)

				if user_buy < 1 or user_buy > 1000:
					print('Invalid transaction, a number between 1 and 1000 should be inserted.\nReturning to main menu.')
				else:
					player.add_chips(user_buy)              #add chips to user inventory

					
			if user_input == 'p' or user_input == 'P':                    #if play
				user_bet = input('Place your bet!\nThe bet should be an even number 2-100: ')
				user_bet = int(user_bet)
				if user_bet > 100 or user_bet > player.get_chips(): #insert buy first condition
					print('Bet is too large.')                                   #checking for user input in 2-100 range and even
				elif user_bet < 2:
					print('Bet is too small.')
				elif user_bet % 2 != 0:
					print('Bet is odd, should be even.')

				else:
					if table.get_shoe().size() > 1:                           #if theres enough deck
						bets.append(user_bet)                      #add user bet to bets
						player.remove_chips(user_bet)               #remove the bet value of chips from user 
						table.set_bet(user_bet)                    #set bet for user in table
						bets.append(user_bet)                      #currents bet status after chips removed
						table.set_cards()
						player_card = table.get_player_card()              #assigning the cards to the variable
						dealer_card = table.get_dealer_card()
						
						if plays == 0:                           #if first hand
							print('First hand of the shoe, burning one card.\n')
						print('No more bets!')
						print('Player shows %s, Dealer shows %s' % (player_card,dealer_card)) #show cards
						
						if table.resolve_round(player_card,dealer_card) == 1:         #if player win
							play_count.append(user_bet)               #add bet to all the bets player made
							print('Player wins')
							player.add_chips(user_bet*2)                          #double bet number of chips for winning
							win_count = win_count +1
						
						elif table.resolve_round(player_card,dealer_card) == -1:          #if player lose
							play_count.append(-user_bet)                         #lose bet subtract from list
							print ('Dealer wins')
						
						elif table.resolve_round(player_card,dealer_card) == 0:               #if draw,go to war or surrender
							war_count = war_count + 1
							user_choice = input('War!!! Would you like to go to war(W) or surrender(S)? ')
							while user_choice not in ['S','W','w','s']:
								print('Invalid')
								user_choice = input('War!!! Would you like to go to war(W) or surrender(S)? ')
			
							if user_choice == 'w' or user_choice == 'W':                #if war
								print('We are going to war!!! You doubled up your bet.')
								player.remove_chips(user_bet)         
								table.set_bet(user_bet*2)             #double up bet
								print('Burning 3 cards')
								table.enque_discard(3)                #burn 3 cards
								table.set_cards()                      #set new cards
								player_card = table.get_player_card()
								dealer_card = table.get_dealer_card()
								print('Player shows %s, Dealer shows %s' % (player_card,dealer_card)) #show cards
								if table.resolve_round(player_card,dealer_card) == 0:                #if tie again
									play_count.append(0)                    #no adding since its doubled,but 0 appended to take into account how many plays
									print('Player wins')
									player.add_chips(user_bet*3)               #player win outcome
									win_count = win_count + 1                   #wins
								elif table.resolve_round(player_card,dealer_card) == 1:          #player win and outcome
									play_count.append(0)
									print('Player wins')
									player.add_chips(user_bet*3)
									win_count = win_count +1
								elif table.resolve_round(player_card,dealer_card) == -1:                    #if lose
									play_count.append(-2 * user_bet)            #lose double the bet
									print ('Dealer wins')
							elif user_choice == 's' or user_choice == 'S':               #if surrender
								play_count.append(int(-user_bet/2))     #lose half the bet
								print('Player surrendered,loses half of their entire wager')
								player.add_chips(int(user_bet/2))                
						plays = plays + 1                                    #increment play
					
					if table.get_shoe().size() <= 1:                  #if not enough deck left,reset the table
						table.clear()
						table.make_shoe()
						table.enque_discard(1)

					
			
			if user_input == 'q' or user_input == 'Q':                   #Quit,for some reason you need to quit a second time to exit the loop completely,I tried other methods but it's still the same.First quit gives stats of the last game played,second quit stops the game.
				                                    #stop loop,for some reason the loop does not stop eventhough the condition if false after this
				print('\nPlayed ' + str(plays) + ' hands') 
				print('From these hands, ' + str(war_count) + ' were war hands')
				profit = 0
				bet = 0                                                           #stats
				for i in play_count:
					profit = profit + i
				for j in bets:                                   #adding up the value in the list
					bet = bet + j
				
				if len(play_count) == 0:
					profit = 0
				
				if bet == 0:
					averageBet = 0
				else:
					averageBet = (bet/len(bets))
				
				print('The average bet was %0.3f chips ' % (averageBet))
				print('The average profit of the session was %0.3f' % (profit))
				try:
					print('Player won', str(win_count) ,'out of ',str(plays),'hands,or %0.3f%%' %(win_count*100/plays))
					print('Goodbye')
				except ZeroDivisionError:
					print('Player won 0 out of 0 hands,or 0.000%')
					print('Goodbye')
					input("Press Enter to exit")
				Play = False

				
		

def auto_play(action,integer):

	action = action.upper()

	if action == 'B':                                   #if buy
		with open('savefile.txt', 'rb') as f:
			table,player,bets,plays,win_count,play_count,war_count = pickle.load(f)         #loaad pickle

		user_buy = integer

		if user_buy < 1 or user_buy > 1000:
			print('Invalid transaction, a number between 1 and 1000 should be inserted.\nReturning to main menu.')
			print('False')
			return False
		else:
			player.add_chips(user_buy)                                               
			print('True')
			with open('savefile.txt', 'wb') as f:                    #save in pickle
				pickle.dump([table,player,bets,plays,win_count,play_count,war_count],f,protocol=2)
			return True

	if  action == 'P':
		with open('savefile.txt', 'rb') as f:
			table,player,bets,plays,win_count,play_count,war_count = pickle.load(f)

		if table.get_shoe() == None:
			table.make_shoe()

		user_bet = integer

		if user_bet > 100 or user_bet > player.get_chips(): #insert buy first condition
			print('Bet is too large.')                                   #checking for user input in 2-100 range and even
		elif user_bet < 2:
			print('Bet is too small.')                #no print***********
		elif user_bet % 2 != 0:
			print('Bet is odd, should be even.')

		else:

			if (user_bet*2) > player.get_chips():
				play_count.append(int(-user_bet/2))     #lose half the bet
				player.remove_chips(int(user_bet/2)) 
				print('False')
				return False

			elif table.get_shoe().size() > 1:                           #if theres enough deck
				bets.append(user_bet)                      #add user bet to bets
				player.remove_chips(user_bet)               #remove the bet value of chips from user 
				table.set_bet(user_bet)                    #set bet for user in table
				bets.append(user_bet)                      #current bet status after chips removed
				table.set_cards()
				player_card = table.get_player_card()              #assigning the cards to the variable
				dealer_card = table.get_dealer_card()

				war_count = war_count + 1
																							#if war
				player.remove_chips(user_bet)         
				table.set_bet(user_bet*2)             #double up bet
				table.enque_discard(3)                #burn 3 cards
				table.set_cards()                      #set new cards
				player_card = table.get_player_card()
				dealer_card = table.get_dealer_card() #
				if table.resolve_round(player_card,dealer_card) == 0:                #if tie again
					play_count.append(0)
					player.add_chips(user_bet*3)               #player win outcome
					win_count = win_count + 1
				elif table.resolve_round(player_card,dealer_card) == 1:          #player win and outcome
					play_count.append(0)
					player.add_chips(user_bet*3)
					win_count = win_count +1
				elif table.resolve_round(player_card,dealer_card) == -1:                    #if lose
					play_count.append(-2 * user_bet)         #lose double the bet

																#adding haalf of bet to the total chips               
				plays = plays + 1                                    #increment play

			elif table.get_shoe().size() <= 1:                  #if not enough deck left,reset the table
				table.clear()
				table.make_shoe()
				table.enque_discard(1)

		print('Player chips = %d' % (player.get_chips()))
		with open('savefile.txt', 'wb') as f:
			pickle.dump([table,player,bets,plays,win_count,play_count,war_count],f,protocol=2)        
		return player.get_chips()

	if action == 'Q':                   #if quit
		with open('savefile.txt', 'rb') as f:
			table,player,bets,plays,win_count,play_count,war_count = pickle.load(f)                                                       #stop loop,for some reason the loop does not stop eventhough the condition if false after this

		Array = []
		Percentage_list = []
		Array.append(plays)
		profit = 0
		bet = 0                                                           #stats
		for i in play_count:
			profit = profit + i
		for j in bets:
			bet = bet + j

		if len(play_count) == 0:
			profit = 0

		if bet == 0:
			averageBet = 0
		else:
			averageBet = (bet/len(bets))

		Array.append(averageBet)                                       #making array
		Array.append(profit)

		#Percentage_list.append(plays)               #total plays,probably extra then ignore
		Percentage_list.append(win_count)          #total wins
		try:
			percent = (win_count*100/plays)
			Percentage_list.append(percent)               #% of wins
		except ZeroDivisionError:
			Percentage_list.append(0)

		Array.append(Percentage_list)
		Array.append(war_count)

		print(Array)


		with open('savefile.txt', 'wb') as f:
			table = Table(None,None,None,None,None)
			player = Player()
			bets = []                                   #restting pickle
			plays = 0
			win_count = 0
			play_count = [] 
			war_count = 0
			pickle.dump([table,player,bets,plays,win_count,play_count,war_count],f,protocol=2)

		return Array              

	if action not in ['B','P','Q']:
		print('-1')
		return -1	
	

if __name__ == "__main__":
	main()







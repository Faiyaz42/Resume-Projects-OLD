class Player:
	def __init__(self):                            #initiation
		self.__chips = 0
	
	
	def add_chips(self, chips):                          #check if chip value is positive and integer
		assert chips >= 0 and isinstance(chips, int),'Invalid chips value'
		self.__chips = self.__chips + chips            #add chip value to chips
				 
		
		
	def remove_chips(self, chips2):                   #check if chip value is positive and integer
		assert chips2 >= 0 and isinstance(chips2, int),'Invalid chips value'
		self.__chips = self.__chips - chips2	 #subtract chip value	
	
	
	def get_chips(self):                        #return current chip status
		return self.__chips

		

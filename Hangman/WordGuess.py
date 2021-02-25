import random
from SecretWord import SecretWord

class WordGuess: 

    def __init__(self, wordDic):
        self.words_dict = wordDic
        self.guess_words = []                           #constructor,initiation
        self.guesses = 0
        self.random_word = ''
        self.current_guess = ''

    def play(self):
        """ Plays out a single full game of Word Guess """            #play game
        self.random_word = self.chooseSecretWord()                      #choose random word
        print('A secret word has been randomly chosen!')                
        acontainer = SecretWord()                               #container(instance) to hold random word
        sorted_container = SecretWord()                         #sorted container or instance
        acontainer.setWord(self.random_word)                 #make linked list 
        sorted_container.setWord(self.random_word)           # '' ''
        string1 = str(acontainer)                           #str of original random word
        string2 = sorted_container.sort()
        string2 = str(sorted_container)                     #str of sorted word
        find_distance = self.editDistance(string1,string2,len(string1),len(string2))        #find edit distance
        alloted_guesses = 2*find_distance                                   #find the alloted number of guesse (*2)
        if alloted_guesses < 5:
            alloted_guesses = 5
        elif alloted_guesses > 15:
            alloted_guesses = 15        
        self.guesses = int(alloted_guesses)
        while self.guesses > 0 and acontainer.isSolved() == False:
            print('You have %d guesses remaining' % (self.guesses))             #if user hasnt guessed it yet loop
            acontainer.printProgress()                                                #print progress
            self.getGuess()                                                         #get guess
            acontainer.update(self.current_guess)                                    #update
            if self.current_guess not in string1 and self.current_guess != '*':             #if wrong guess
                self.guesses = self.guesses - 1                                        #deduct
        if self.guesses > 0 and acontainer.isSolved() == True:                     #if successfully solved
            print('You solved the puzzle!')
            print('The secret word was: %s ' % (str(acontainer)))
        elif self.guesses == 0:                                                        #if failed
            print('You have run out of guesses\nGame Over')
            print('The secret word was: %s ' % (str(acontainer)))
        self.guess_words = []
        self.guesses = 0                                                                 #reset
        self.random_word = ''
        self.current_guess = ''
            
        

    def chooseSecretWord(self):
        """ Chooses the secret word that will be guessed """                            #choose a random word from the dict
        item = random.choice(list(self.words_dict))
        return  str(item )    

    def editDistance(self, s1, s2,length1,length2):                              # edit distance with length1 of string1 and length2 of string 2 ,for later recursion
        """ Recursively returns the total number of insertions and deletions required to convert S1 into S2 """              
        if length1 == 0:             #if first string is empty,return second string value since its being totally transferred
            return length2

        if length2 == 0:                #vice versa
            return length1
                
    
        if s1[length1-1]==s2[length2-1]: 
            return self.editDistance(s1,s2,length1-1,length2-1) 
                        
    
                                                                  #recursively find the distance for eahc operation and find the minimum
        return 1 + min(self.editDistance(s1, s2, length1, length2-1),           # Insert 
                       self.editDistance(s1, s2, length1-1, length2))             # Remove 
         
     
    

    def getGuess(self):                                                         
        """ Queries the user to guess a character in the secret word """
        ask = True                                                                               #ask loop
        while ask:         
            user_input = input('Enter a character that has not been guessed or * for a hint: ')
            self.current_guess = str(user_input)
            if user_input == '*':                                                          #if asked for hint
                hint = self.words_dict[self.random_word]
                print('Hint: %s' % (hint))                                          #show hint and deduct 1
                self.guesses = self.guesses - 1
                ask = False
            elif self.current_guess not in self.guess_words:                             #if guess is not repeated
                self.guess_words.append(self.current_guess)                             #add to guesses list
                ask = False
            elif user_input in self.guess_words:                                                 #if guess is repeated
                print('Invalid guess. You have already guessed this letter.')
            
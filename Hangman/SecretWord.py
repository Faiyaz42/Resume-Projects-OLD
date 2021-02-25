from Node import Node

class LinkedList:
    """ The Singly-Linked List """

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):               #adding head
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    
    def find(self,item):                     #searches and returns the data if found
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                found_data = current.getData()
            else:
                current = current.getNext()
        if found == True:
            return found_data  
        elif found == False:
            return False
         
    def find_duplicates(self,item):                         #finds duplicates and returns how many
        current = self.head
        found_counter = 0
        while current != None:
            if current.getData() == item:
                found_counter = found_counter + 1
            else:
                current = current.getNext()
        if found_counter > 1:
            return found_counter  
        elif found_counter == 1:
            return found_counter 
        else:
            return found_counter
    

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()

    def getHead(self):
        return self.head

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()

        # Additional attribute(s) go here:
        self.userGuesses = []                                    #storing user guesses(probably redundant now)
        self.linkedList_sorted = LinkedList()                    #temp linked list to store the sorted linkedlist

    def setWord(self, word):           
        """ Adds the characters in 'word' to self.linkedList in the given order """
        if len(str(word)) == 1:                        #if word is one letter
            self.linkedList.add(str(word))
        elif len(str(word)) > 1:                         #if more than one letter
            counter = 0
            while counter < len(str(word)):
                if counter == 0:                             #first letter adds to the head
                    self.linkedList.add(str(word[counter]))
                else:
                    self.linkedList.append(str(word[counter]))       #others append to the tail
                counter = counter + 1
            
            

    def sort(self):                              #insertion sort
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        head_node = self.linkedList.getHead()       #first node
        if head_node == None:                    #if empty linked list head
            return None
        sortedList = head_node                    #storing second node
        head_node = head_node.getNext()
        sortedList.setNext(None)                 #isolating head node for comparison
        while head_node != None:
            current = head_node                 #second node is current
            head_node = head_node.getNext()     #head node is now 3rd node
            if current.getData() < sortedList.getData():      #comparison with actual head node and second node
                current.setNext(sortedList)                 #insertion
                sortedList = current
            else: 
                search = sortedList   #search correct position for current
                while search.getNext() != None and current.getData() > search.getNext().getData():               #if current is bigger than head
                    search = search.getNext()                              
                current.setNext(search.getNext())   #current after search
                search.setNext(current)

        node = sortedList                    #append the nodes in temp linked list then assign it to the main,self.linked list
        while node:
            self.linkedList_sorted.append(node.getData())
            node = node.getNext()
        self.linkedList = self.linkedList_sorted
               



    def isSolved(self):          #if theres _ in string means not solved yet
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        
        if '_' in self.Progress():
            return False
        elif '_' not in self.Progress():
            return True
                 
                

    def update(self, guess):    #update the nodes to print or not to print (bool)
        """ Updates the nodes in self.linkedList that match 'guess' """
        current = self.linkedList.getHead()
        #self.userGuesses.append(guess)
        while current != None:
                if current.getData() == guess:        #if match then bool set to True for print
                    current.setDisplay(True)
                current = current.getNext() 
                

    def Progress(self):    #returns an updated string
        """ Prints the current game progress
        Ex: y _ l l _ w """
        current = self.linkedList.getHead()    
        word_progress = []
        while current != None:                            #if bool is False add _ to the list
            if current.getDisplay() == False:
                word_progress.append('_')
            elif current.getDisplay() == True:                #if true add the charcter to list
                word_progress.append(str(current.getData()))                
            current = current.getNext()
        string =  ' '.join(word_progress)           #join the list to a string
        return string    
    
    
    def printProgress(self):                   #Prints the string,rest of it is same as above
        """ Prints the current game progress
        Ex: y _ l l _ w """
        current = self.linkedList.getHead()
        word_progress = []
        while current != None:            
            if current.getDisplay() == False:
                word_progress.append('_')
            elif current.getDisplay() == True:
                word_progress.append(str(current.getData()))                
            current = current.getNext()
        string = 'Word Guess Progress: ' + ' '.join(word_progress)
        print(string)
        
        

    def __str__(self):                                                    #converts to string each nodes
        """ Converts the characters in self.linkedList into a string """
        current = self.linkedList.getHead()
        word = []
        while current != None:
            word.append(str(current.getData()))
            current = current.getNext()
        string = ''.join(word)            
        return string
        


        
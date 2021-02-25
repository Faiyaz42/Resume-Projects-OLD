from WordGuess import WordGuess


def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    file_read = open(filename,'r')   #reads file name
    Words_dic = { }                  #initiates dict
    for line in file_read:
        Item = line.split()
        word = Item[0]
        hint = Item[1]                          #inserting values and keys in dict
        Words_dic[word] = hint.strip()    
    return WordGuess(Words_dic)                   #returns instance of the word guess class with the dict passed to it  

def main(): 
    user_input = input('Please enter a Word Guess input file: ')               #hangman_words.txt    input file name
    Word_guess = readWords(user_input)
    Play = True
    while Play:                                                #play loop
        Word_guess.play()                                         #initiate play
        ask = input('Would you like to play again? (y/n): ')    #endgame
        print('\n')
        ask = ask.upper()
        if ask == 'N':
            Play = False
        elif ask == 'Y':                      #user decision verification
            Play = True


if __name__ == "__main__":
    main()
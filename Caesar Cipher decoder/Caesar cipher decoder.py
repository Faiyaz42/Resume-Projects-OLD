
while True:
    ask = input("Do you want to decipher the default file (press N if you want to enter the name of \nthe file you want to decipher)? (Y/N)\n") 
    if ask == "Y" or ask == "y" or ask == "N" or ask == "n":
        break

if ask == "Y" or ask == "y":
    read_file = open ("input_ciphers.txt",'r') 
    print ("\nDeciphered texts:\n")
else:
    file_name = input ('Enter the input filename: ')               #inputs
    try:
        read_file = open (file_name,'r')
        print ("\nDeciphered texts:\n")
    except FileNotFoundError:
        print("Oops! No file with the name %s found in the folder..." %(file_name))
        input("Press enter to close")


for lines in read_file:
    key_and_ciphertext_input = lines.strip()
    key_and_ciphertext = key_and_ciphertext_input.split(' ')
    if len(key_and_ciphertext) == 1:                             #if a line has a component missing
        t = key_and_ciphertext[0]
        if t.isdigit() == True:             
            print ('Missing text!')                              #no ciphertext
        elif t.isalpha() == True:
            print ('Missing key!')                               #no key
    if len(key_and_ciphertext) == 2:                             #if components present
        h = key_and_ciphertext[0]
        if h.isdigit() == True:                                  #check if correct format i.e key then cipher
            key = int(key_and_ciphertext[0])
            ciphertext = key_and_ciphertext[1]
            Decrypted = ''
            for alphabet in ciphertext.upper():                           #decryption
                if alphabet.isalpha():
                    alphabet_value = ord(alphabet)
                    decrypted_value = alphabet_value - key        #shift
                    Again = True                                  
                    while Again:                                    #to loop around if decrypted value is more or less than range of ord A to Z
                        if decrypted_value < ord('A'):              #if less than ord A
                            decrypted_value = decrypted_value + 26        
                        elif decrypted_value > ord('Z'):            #if more than ord Z
                            decrypted_value = decrypted_value - 26                          
                        if decrypted_value >= 65 and decrypted_value <= 90:       #if in range ord A to Z then stop the loop
                            Again = False
                        elif decrypted_value < 65 or decrypted_value > 90 :        #if still out of A to Z range then do another loop until in ord A to Z range
                            Again = True
                    Decrypted = Decrypted + chr(decrypted_value)                #join the decrypted letter to decrypted string
                                                             #print final decrypted result
            print (Decrypted)
        else:
            print ('Wrong format')                                          #if wrong format i.e cipher then key
    
    
input('Press enter to close')                                            #for CMD closing
    
    
    
    
       
                   
    
    
    
    
    
    
    
    

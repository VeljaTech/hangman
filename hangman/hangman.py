import random
import time                                                                                                                           #imports
import sys
import os
import linecache


open(r'wordlist.txt.txt', mode='r')
word = linecache.getline('wordlist.txt.txt', random.randint(1,49))                                                                    #gets random word from wordlist.txt file  
      

lenght = len(word)-1                                                                                                                  #determines lenght of the word


tries = 0                                                                               








if lenght == 2:                                                                                                                       #if there are 2 letters in the word

    letter_1= word[0]
    letter_2= word[1]                                                                                                                 #gets letters from the word
    
    character_print_1 = "_"
    character_print_2 = "_"                                                                                                           # sets _ to be printed by default

    print(character_print_1, " " , character_print_2)                                                                                 #tells the player how many letters there are
                    

    for i in range(4124):

        tries= tries+1                                                                                                                #adds one try to the try count
        
        letter_guess = input("Guess a letter: ")                                                                                      #makes player guess the letter



        if letter_guess == letter_1:
            character_print_1 = letter_1                                                                                              #checks if guessed letter is contained within
                                                                                                                                      #in the word and if it is, changes
                                                                                                                                      #character_print value to that letter
        if letter_guess == letter_2:
            character_print_2 = letter_2
                                                                                    


        print(character_print_1, " " , character_print_2)                                                                             #prints guessed letters and _ for letters that are not guessed yet
                                                                                    


        if character_print_1 != "_":                                                                                                  #checks if all letters are guessed

            if character_print_2 != "_":

                print("You have guessed the word!", tries, " tries were needed")                                                      #prints that word is guessed and prints how many tries it took
                sys.exit()












if lenght == 3:                                                                                                                       #if there are 3 letters in the word

    letter_1= word[0]
    letter_2= word[1]                                                                                                                 #gets letters from the word
    letter_3= word[2]
    
    character_print_1 = "_"
    character_print_2 = "_"                                                                                                           #sets _ to be printed by default
    character_print_3 = "_"

    print(character_print_1, " " , character_print_2, " " , character_print_3)                                                        #tells the player how many letters there are
                    

    for i in range(4124):

        tries= tries+1                                                                                                                #adds +1 to try counter after every try

        letter_guess = input("Guess a letter: ")                                                                                      #makes player guess the letter



        if letter_guess == letter_1:
            character_print_1 = letter_1

        if letter_guess == letter_2:
            character_print_2 = letter_2
                                                                                                                                      #checks if guessed letter is contained within
        if letter_guess == letter_3:                                                                                                  #in the word and if it is, changes
            character_print_3 = letter_3                                                                                              #character_print value to that letter


        print(character_print_1, " " , character_print_2, " " , character_print_3)                                                    #prints guessed letters and _ for letters that are not guessed yet
                                                                                    


        if character_print_1 != "_":                                                                                                  #checks if all letters are guessed

            if character_print_2 != "_":

                if character_print_3 !="_":

                    print("You have guessed the word!", tries, " tries were needed")                                                  #prints that word is guessed and prints how many tries it took
                    sys.exit()











if lenght == 4:                                                                                                                       #if there are 4 letters in the word

    letter_1= word[0]
    letter_2= word[1]
    letter_3= word[2]
    letter_4= word[3]
    
    character_print_1="_"
    character_print_2="_"
    character_print_3="_"
    character_print_4="_"

    print(character_print_1, " " , character_print_2, " " , character_print_3, " " , character_print_4)                               #tells the player how many letters there are
                    

    for i in range(4124):

        tries = tries+1                                                                                                               #adds +1 to try counter after every try


        letter_guess = input("Guess a letter: ")                                                                                      #makes player guess the letter



        if letter_guess == letter_1:
            character_print_1 = letter_1

        if letter_guess == letter_2:
            character_print_2 = letter_2
                                                                                                                                      # checks if guessed letter is contained within
        if letter_guess == letter_3:                                                                                                  # in the word and if it is, changes
            character_print_3 = letter_3                                                                                              # character_print value to that letter

        if letter_guess == letter_4:
            character_print_4 = letter_4

        print(character_print_1, " " , character_print_2, " " , character_print_3, " " , character_print_4)                           #prints guessed letters and _ for letters that are not guessed yet
                                                                                    


        if character_print_1 != "_":                                                                                                  #checks if all letters are guessed

            if character_print_2 != "_":

                if character_print_3 !="_":

                    if character_print_4 !="_":

                        print("You have guessed the word!", tries, " tries were needed")                                              #prints that all the letters are guessed and prints how many tries it took
                        sys.exit()














if lenght == 5:                                                                                                                       #if there are 4 letters in the word

    letter_1= word[0]
    letter_2= word[1]
    letter_3= word[2]                                                                                                                 #gets letters from the word
    letter_4= word[3]
    letter_5= word[4]
    
    character_print_1="_"
    character_print_2="_"
    character_print_3="_"                                                                                                             #sets _ to be printed as default
    character_print_4="_"
    character_print_5="_"

    print(character_print_1, " " , character_print_2, " " , character_print_3, " " , character_print_4, " " , character_print_5)      #tells the player how many letters there are
                    

    for i in range(4124):

        tries= tries+1                                                                                                                #adds +1 to try counter for every try                                   

        letter_guess = input("Guess a letter: ")                                                                                      #makes player guess the letter



        if letter_guess == letter_1:
            character_print_1 = letter_1

        if letter_guess == letter_2:
            character_print_2 = letter_2
                                                                                                                                      # checks if guessed letter is contained within
        if letter_guess == letter_3:                                                                                                  # in the word and if it is, changes
            character_print_3 = letter_3                                                                                              # character_print value to that letter

        if letter_guess == letter_4:
            character_print_4 = letter_4

        if letter_guess == letter_5:
            character_print_5 = letter_5

        print(character_print_1, " " , character_print_2, " " , character_print_3, " " , character_print_4, " ", character_print_5)   #prints guessed letters and _ for letters that are not guessed yet
                                                                                    


        if character_print_1 != "_":                                                                                                  #checks if all letters are guessed

            if character_print_2 != "_":

                if character_print_3 !="_":

                    if character_print_4 !="_":

                        if character_print_5 !="_":

                            print("You have guessed the word!",tries," tries were needed")                                           #says that the word is guessed and print number of tries it took
                            sys.exit()


###############################################################################################################################################################################################################################################################
##UNDER CONSTRUCTION!!!      restart = input("Try again Y/N: ")                    #asks the player if he wants to restart                                             #
#
#
#        #if restart == "N" or "n":                                                  #if the player say No than program exits                                          #
#            #restart()
#
#
#        #if restart == "Y" or "y":                                                  #if the player says yes starts the program again                                  #
#                                                                                                                                                                      #
#            #continue                                                                                                                                                 #
#                                                                                                                                                                      # 
#                                                                                                                                                                      #
#        #if restart != "N" or "Y" or "y" or "n":                                    #if the player says anything else reminds him of Y/N answer format                #
#            #print("Use Y/N format")                                                                                                                                  #
#                                                                                                                                                                      #
########################################################################################################################################################################













#############################################################################################################################################################################################################################################################################################


#WHAT FOLLOWS IS CODE DUMP(I found it useful to dump and save parts of code I am not using anymore for later revision)




#word1= "mom"
#word2= "dad"
#word3= "bad"
#word4= "bag"
#word5= "fly"                                                                          #Chooses random word and gets its lenght
#word6= "ban"
#word7= "bar"
#word8= "fbi"
#word9= "bee"
#word10= "ant"
#word = random.choice([word1,word2,word3])

#os.open(r'C:\Users\Veljko\Desktop\hangman')    

        
                       






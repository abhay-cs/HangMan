import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_word(words):
    # get random word from the list
    rand_word = random.choice(words) 
    # if "_" or " " found in the word keep choosing the next word..
    while ("-" in rand_word or " " in rand_word):
        rand_word = random.choice(words)
    return rand_word

def hangman():
    game = True
    while game == True:

        print("\nWelcome to HangMan\n")
        response = input("1. Press p to play\n" + "2. Press q to quit\n").lower()
        if response == 'p':
            # difficulty = input("\nPlease set difficulty level:\n" + 
            #                 " Press '1' for Easy\n" + 
            #                 " Press '2' for Medium\n" + 
            #                 " Press '3' for Hard\n")
            # # add a response check for level
            # if difficulty == '1':
            #     level = 1
            # elif difficulty == '2':
            #     level = 2
            # elif difficulty == '3':
            #     level = 3
            # else:
            #     print("Please enter a valid response")
            word = get_word(words) #random word
            word = word.upper() # make it upper case 
            word_letters = set(word) # letters from the random word
            alphabet = set(string.ascii_uppercase) # alphabet set to check valid letters input from user
            used_letters = set() # empty set of used_letter
            lives = 6 # max lives 
            while len(word_letters) > 0 and lives > 0: # if lives < 0 or word letter < 0 stop the loop
                # prints the already used letters 
                print('\nYou have',lives,'lives left and you have already used these letters: ',' '.join(used_letters))
                # if letter in used_letter return that if not return "_"
                word_list = [letter if letter in used_letters else '-' for letter in word]
                print(lives_visual_dict[lives])
                print('Current word: ',' '.join(word_list))
                # takes input from the user
                user_letter = input("Guess the letter: ").upper()
                if user_letter in alphabet - used_letters:
                    used_letters.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                    else:
                        lives = lives - 1
                        print('Your letter,',user_letter,'is not in the word')
                elif user_letter in used_letters:
                    print("You already guessed this letter!")
                else:
                    print("Type in a valid character")


            if lives == 0:
                # print hanged guy
                print(lives_visual_dict[lives])
                print('You Died!')
                print('Correct word was : ',' '.join(word))
            else:
                print("You have Guessed the word, Congratulations!!")
                print('Correct word: ',' '.join(word))
        elif response == 'q':
            print("Good bye :(")
            game = False
        else:
            print("Please enter a valid response")

if __name__ == '__main__':
    hangman()




'''
1. option to set difficutly--> lives and word length
After game ends 
2. quit
3. play again

while(game_val = true):
    show start page
    get difficlty lvl
    while game loop()


'''
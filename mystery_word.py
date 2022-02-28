from pyparsing import line_start
import random

# Files =====================================================================
# wordFile = "test-word.txt"  
wordFile = "words.txt"


def play_game():
    # Global Variables ======================================================
    chances = 8
    misses = 0
    missesLeft = chances - misses


    # Working Variables =====================================================
    guessWord = get_test_word(wordFile)
    guessWord = guessWord[0:-1]
    guessString = (len(guessWord)) * '_'
    displayString = (len(guessWord)) * '_'


    # Introduction ==========================================================
    print(f"There are {len(guessWord)} letters in the word to guess:  {formatD(displayString)}       You have {missesLeft} incorrect guesses to make before you lose!")
    print(f"<<<<<<<<< The word is: {guessWord} >>>>>>>>>>>>>")                  # For testing only
    letter = input("What letter would you like to guess?  ")


    # Game Logic =============================================================
    while (misses < chances) and (guessWord != guessString):
        if letter in guessWord:
            print(f"You selected {letter}")
            print('Great job! You guessed right!!')
            
            locations = location_list(letter, guessWord)
            displayString = updateDisplay(letter, locations, displayString)
            guessString = updateString(letter, locations, guessString)
            
            print(f'Here is what you have so far:  {formatD(displayString).rjust(30, " ")}       You have {missesLeft} incorrect guesses remaining')
            
            if guessWord != guessString:
                letter = input("What letter would you like to guess?  ")
            else:
                print("YOU DID IT!! YOU WIN!!!!!")

        else:
            print(f"You selected {letter}")
            print('Oh too bad.. guess again.')

            misses = misses + 1                     # WHYYYY DOES IT NOT UPDATE ABOVE WITHOUT THIS????
            missesLeft = missesLeft - 1

            print(f'Here is what you have so far:  {formatD(displayString).rjust(30, " ")}       You have {missesLeft} incorrect guesses remaining')

            if misses < chances:
                letter = input("What letter would you like to guess next?  ")
            else:
                print("LOSER!!!")
                print(f'The correct word was: {guessWord}')
    

# Miscellaneous Functions ================================================
def updateString(letter, locations, guessString):
    """ Return an updated version of the guess string with correct values added. """
    str_list = list(guessString)
    for n in locations:
        str_list[n] = letter
    guessString = list_to_string(str_list)
    return guessString
    
    
def updateDisplay(letter, locations, displayString):
    """Takes in a letter that is correct,
    a list of the locations that letter occurs
    and the current display string"""
    str_list = list(displayString)
    for n in locations:
        str_list[n] = letter
    displayString = list_to_string(str_list)
    return displayString
    
    
def formatD(displayString):
    """" Return the string passed in with spaces added in between. """
    newString = ""
    for n in displayString:
        newString += n + " "
    return newString 

    
def printD(displayString):
    """ Print a string with a space inbetween. """
    newString = ""
    for n in displayString:
        newString += n + " "
    print(newString) 


def list_to_string(listOfChars):
    """ Convert a list into a string with no spaces inbetween. """
    newString = ""
    for e in listOfChars:
        newString += e
    return newString


def location_list(letter, word):
    """Returns a list of the locations that letter occurs"""
    locations = []
    i = 0
    while i < len(word):
        for c in word:
            if c == letter:
                locations.append(i)
                i += 1
            else:
                i += 1
    return locations


# Trying to find the more 'Pythonic' way... doesn't work right
def location_list2(letter, word):
    """Returns a list of the locations that letter occurs"""
    locations = []
    for i in range(0,len(word)):
        for c in word:
            if c == letter:
                locations.append(i)
                i += 1
            else:
                i += 1
    return locations


def get_test_word(file):
    """Takes a file passed into it and returns a string"""
    file1 = open(file)
    strArr = file1.readlines()
    idx = random.randint(0,len(strArr)-1)
    return strArr[idx]

# Main Function ===============================================================
if __name__ == "__main__":
    play_game()
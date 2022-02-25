from pyparsing import line_start


wordFile = "test-word.txt"              # Single place to change the input file for testing

def play_game():
    chances = 8
    misses = 0
    missesLeft = chances - misses

    guessWord = get_test_word(wordFile)
    guessString = (len(guessWord)-1) * '_'
    displayString = (len(guessWord)-1) * '_'

    print(f"There are {len(guessWord)} letters in the word to guess:  {formatD(displayString)}       You have {missesLeft} incorrect guesses to make before you lose!")
    letter = input("What letter would you like to guess?  ")


    while (misses < chances) and not (False):
        if letter in guessWord:
            print(f"You selected {letter}")
            print('Great job! You guessed right!!')
            
            locations = location_list(letter, guessWord)
            displayString = updateDisplay(letter, locations, displayString)
            guessString = updateString(letter, locations, guessString)
            print(guessString)
            
            print(f'The locations that letter occurs in the word is:  {formatD(displayString)}       You have {missesLeft} incorrect guesses remaining')

            letter = input("What letter would you like to guess?  ")
        else:
            print(f"You selected {letter}")
            print('Oh too bad.. guess again.')

            misses = misses + 1                     # WHYYYY DOES IT NOT UPDATE ABOVE WITHOUT THIS????
            missesLeft = missesLeft - 1

            print(f'Here are the guesses you\'ve gotten so far:  {formatD(displayString)}       You have {missesLeft} incorrect guesses remaining')
            letter = input("What letter would you like to guess next?  ")
    

def winTest():
    """Returns true when the word is guessed"""
    return false
    
def updateString(letter, locations, guessString):
    str_list = list(guessString)
    for n in locations:
        str_list[n] = letter
    guessString = list_to_string(str_list)
    return guessString
    
def printStatus():
    pass

def updateDisplay(letter, locations, displayString):
    str_list = list(displayString)
    for n in locations:
        str_list[n] = letter
    displayString = list_to_string(str_list)
    return displayString
    
def formatD(displayString):
    newString = ""
    for n in displayString:
        newString += n + " "
    return newString 

    
def printD(displayString):
    newString = ""
    for n in displayString:
        newString += n + " "
    print(newString) 


def list_to_string(listOfChars):
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

    
    

def letter_check(char, guessWord):
    pass
    

def get_test_word(file):
    """Takes a file passed into it and returns a string"""
    file1 = open(file)
    strArr = file1.readlines()
    return strArr[0]                    # random generated number will replace 0 later

if __name__ == "__main__":
    play_game()
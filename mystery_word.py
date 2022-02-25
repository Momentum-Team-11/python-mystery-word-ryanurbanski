from pyparsing import line_start


wordFile = "test-word.txt"              # Single place to change the input file for testing

def play_game():
    guessWord = get_test_word(wordFile)
    displayString = len(guessWord) * '_'
    print(f"There are {len(guessWord)} letters in the word to guess:  {displayString}")
    letter = input("What letter would you like to guess?  ")
    print(f"You selected {letter}")
    if letter in guessWord:
        print('Great job! You guessed right!!')
        locations = location_list(letter, guessWord)
        print(f'The locations that letter occurs in the word is: {locations}')
        displayString = updateDisplay(letter, locations, displayString)
        printD(displayString)
    else:
        print('Oh too bad.. guess again.')


def updateDisplay(letter, locations, displayString):
    str_list = list(displayString)
    for n in locations:
        str_list[n] = letter
    displayString = list_to_string(str_list)
    return displayString
    
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






# GAMEPLAN =============================================
# Get test word from file
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# F: Get random word from file
# 
# 
# 
# 
# # # # # 
    
    

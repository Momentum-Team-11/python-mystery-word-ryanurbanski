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
        update_display(letter, guessWord)
    else:
        print('Oh too bad.. guess again.')
    

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
    
    

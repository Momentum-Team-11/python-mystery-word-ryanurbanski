wordFile = "test-word.txt"              # Single place to change the input file for testing

def play_game():
    get_test_word(wordFile)


def get_test_word(file):
    """Takes a file passed into it and returns a string"""
    file1 = open(file)
    strArr = file1.readlines()
    print(strArr)
    print(len(strArr))


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
    
    

letter = 'r'
word = 'breather'
display = '_ _ _ _ _ _ _'

def switch():
    # Find locations in breather where r occurs
    locations = []
    while word.find(letter) != -1:
        
        checkPoint = word.find(letter)
        locations.append(word.find(letter))

        # Perform search from the checkpoint to the end of string
        # Update checkPoint
        # Update the locations list

        print(word.find(letter))
        print(f'The checkpoint is: {checkPoint}')
        print(f'The list of locations the letter appears in the word to guess is: {locations}')

switch()
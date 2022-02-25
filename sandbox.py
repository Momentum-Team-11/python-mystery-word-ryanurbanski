letter = 'r'
word = 'breather'
display = '_ _ _ _ _ _ _'




locations = []

i = 0
while i < len(word):
    for c in word:
        if c == letter:
            locations.append(i)
            i += 1
        else:
            i += 1
        

print(locations)







# def switch():
#     # Find locations in breather where r occurs
#     locations = []

#     print (word[2:8])
#     print (word[2:8].find('r'))

#     if word[2:len(word)-1].find(letter) != -1:
        
#         checkPoint = 0
#         locations.append(word.find(letter))

#         # Perform search from the checkpoint to the end of string
#         print(word[2].find(letter))

#         # Update checkPoint
#         # checkPoint = word.find(letter)
#         # locations.append(word.find(letter))

#         # Update the locations list

#         print(word.find(letter))
#         print(f'The checkpoint is: {checkPoint}')
#         print(f'The list of locations the letter appears in the word to guess is: {locations}')

import random

print('Hangman game start')

tries = 6
randIndex = random.randint(0, 267750)

# open and get a random word from the text file
text_file = open('sowpods.txt', 'r')
wordlist = text_file.readlines()
randWord = wordlist[randIndex]
# print('word rand == ', randWord)

# split the word into individual characters and make a list out of them
splitWord = list(randWord)
# print('split word == ', splitWord)
# will remove last element of a list (the empty space, in this case)
splitWord.pop()
print('split word == ', splitWord)
import random

print('Hangman game start')

tries = 6

# open and get a random word from the text file
text_file = open('sowpods.txt', 'r')
wordlist = text_file.readlines()
wordlistLen = len(wordlist) - 1
# print('list len ==', wordlistLen)
randIndex = random.randint(0, wordlistLen)
randWord = wordlist[randIndex]
# print('word rand == ', randWord)

# split the word into individual characters and make a list out of them
splitWord = list(randWord)
# print('split word == ', splitWord)
# will remove last element of a list (the empty space, in this case)
splitWord.pop()
print('split word == ', splitWord)

#setup user answer list
userAnswer = []
wrongAnswers = []
for item in splitWord:
    userAnswer.append('_')

print('user answer == ', userAnswer)
print('wrong guesses == ', wrongAnswers)

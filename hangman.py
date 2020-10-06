import random

print('Hangman game start')

tries = 6
randIndex = random.randint(0, 267750)

text_file = open('sowpods.txt', 'r')
wordlist = text_file.readlines()
randWord = wordlist[randIndex]


print('word rand == ', randWord)


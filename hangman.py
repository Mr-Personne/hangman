import random

print('Hangman game start')


# open and get a random word from the text file
text_file = open('sowpods.txt', 'r')
wordlist = text_file.readlines()
wordlistLen = len(wordlist) - 1
randIndex = random.randint(0, wordlistLen)
randWord = wordlist[randIndex]

# split the word into individual characters and make a list out of them
splitWord = list(randWord)
# will remove last element of a list (the empty space, in this case)
splitWord.pop()

#setup user answer list
userAnswer = []
wrongAnswers = []
for item in splitWord:
    userAnswer.append('_')


def checkIfCorrect(userInput, tries):
    global correct
    if userInput in splitWord:

        wordLen = len(splitWord)
        for i in range(wordLen):
            if userInput == splitWord[i]:
                userAnswer[i] = userInput
                correct = correct + 1

        return tries

    else:
        wrongAnswers.append(userInput)
        tries -= 1
        return tries
        
            

tries = 6
correct = 0
# game loop until no tries left
while tries > 0:
    print('user answer == ', userAnswer)
    print('wrong guesses == ', wrongAnswers)
    print('tries left == ', tries)

    userLetter = input('What letter ? ==> ') or ' '
    userLetter = userLetter.capitalize()

    tries = checkIfCorrect(userLetter, tries)
    #check if user found all letters and wins
    if correct == len(splitWord):
        print('Correct answer == ', splitWord)
        print('you win')
        break


else:
    print('Correct answer == ', splitWord)
    print('you lose, try again')
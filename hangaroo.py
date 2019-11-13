# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:33:52 2019

@author: Nicole Sophia
"""
import string
y = string.ascii_letters

def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True  

def getGuessedWord(secretWord, lettersGuessed):
    
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ' '.join(result)

def getAvailableLetters (lettersGuessed):
    
    remain = []
    for i in y:
        if i not in lettersGuessed:
            remain.append(i)
    return ' '.join(remain)  

def hangaroo(secretWord):
    
    print ('Welcome to Hangaroo!')
    print ('Guess the word that is', len(secretWord), 'letters long.')
    mistakesmade = 0
    lettersGuessed = []
    
    while 3 - mistakesmade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print(' ')
            print ('ANG GALENG NAMAN NON')
            break
        else:
            print(' ')
            print('You have', 3 - mistakesmade, 'guess(es) left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            guess = str(input('PILI KA LETTER: ')).lower()
        	
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print(' ')
                print('WOWIE: ', getGuessedWord(secretWord, lettersGuessed))
        	
            elif guess in lettersGuessed:
                print(' ')
                print("yan na naman?", getGuessedWord(secretWord, lettersGuessed))
        	
            elif guess not in secretWord:
                print(' ')
                print("engk, mali ka siz, TRY AGAIN: ", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesmade += 1
        
        if 3 - mistakesmade == 0:
        	print(' ')
        	print('hay naq better luck next time. This was the word:', secretWord)
        	break
        else:
        	continue
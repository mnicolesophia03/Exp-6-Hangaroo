# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:33:52 2019

@author: Nicole Sophia
"""

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
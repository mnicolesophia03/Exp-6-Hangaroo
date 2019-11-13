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
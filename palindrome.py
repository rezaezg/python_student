"""
Write a function that takes a string as input and returns True if the string is a palindrome, and False otherwise.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.
"""

def is_palindrome(text):
  # / return fload value but // return integer
    for i in range(len(text)//2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
        

import re

def is_palindrome(phrase):
    forwards = phrase.lower()
    backwards = forwards[::-1]
    return forwards == backwards


print(is_palindrome("Go hang gnah og"))
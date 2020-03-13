"""
Words combination

Create a program that reads an input string and then creates 
and prints 5 random strings from characters of the input string.

For example, the program obtained the word ‘hello’, 
so it should print 5 random strings(words) that combine 
characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

Tips: Use random module to get random char from string)
"""

import random

word = input("enter random word: ")
for i in range(0, 5):
    random_chars = ""
    temp_word = word
    while temp_word:
        random_index = random.randrange(0, len(temp_word))
        random_chars += temp_word[random_index]
        temp_word = temp_word[0:random_index] + temp_word[random_index+1:]
    print(random_chars)

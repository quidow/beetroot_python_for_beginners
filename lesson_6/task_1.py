"""
Make a program that has some sentence (a string) on input 
and returns a dict containing all unique words as keys 
and the number of occurrences as values.
"""

string = input("enter string: ")
words = {}
for e in set(string):
    words[e] = string.count(e)

print(words)

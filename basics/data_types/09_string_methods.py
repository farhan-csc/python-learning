""" 
String methods are built-in methods used to manipulate,
search, and process strings in Python.
"""

message = "Python is fun and Python is powerful"
words = "Python, Java, c++, JavaScript"
sentence = "I love learning programming"

print(message.count('Python')) # counts occurrences of a substring.
print(message.find('powerful')) # finds the position of a substring.
print(words.split(', ')) # splits a string into a list.

words1 = words.split(', ') 
print('|'.join(words1)) # joins strings from an iterable into one string.
print(sentence.replace('programming', 'Python')) # replacing the word "programming" with "Python"
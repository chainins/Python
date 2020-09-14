# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:51:01 2020

@author: Chengpi Wu

Homework #7

1. Read a book (a file in text format)
2. Break each line into words
3. Strip whitespace and punctuation from the words
4. Convert to lowercase. 
5. Count the total number of the words, frenquency of each word
6. Print out the top 10 most frequently used words.

Book: The Call of the Wild (by Jack London)
https://www.gutenberg.org/ebooks/215


What to turn in :
◦Code and output
◦Code comment section explains program and also your name & date etc

"""

import string

# The Call of the Wild

FILE_NAME = 'Wild.txt'

with open(FILE_NAME, 'r+', encoding='utf-8') as readFile: #read a book
    wordList = []
    #Breaks each line into words
    for line in readFile: 
         lineWords = line.split()
         wordList.extend(lineWords)
         #Strip whitespace and punctuation and onvert to lowercase.
         wordList = [word.lower().strip(string.punctuation) for word in wordList]   

#Count the total number of the words
print("\nTotal number: ",len(wordList)," words.\n")    
 
wordSet = set(wordList) # No repeat
wordDict = {word: wordList.count(word) for word in wordSet}

wordSort=sorted(wordDict.items(),key=lambda x:x[1],reverse=True)
  
#Output the top 10 frequently used words and their frequency.
print("Top 10 most frequently used words:")     
for i in range(10):
    print('Word:{0}   Times:{1}'.format("%-20s" % wordSort[i][0],wordSort[i][1]))

readFile.close()


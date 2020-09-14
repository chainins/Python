# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:57:58 2020

@author: Chengpi Wu

Homework #9

rewrite last homework using a class. The class can be called FileAnalyzer. 
In addition, In you design, please add methods you think that might be useful for the class. 
Some examples maybe least used words, longest words. Implement those methods.

1. Read a book (a file in text format)
2. Break each line into words
3. Strip whitespace and punctuation from the words
4. Convert to lowercase. 
5. Count the total number of the words, frenquency of each word
6. Print out the top 10 most frequently used words.

Book: The Call of the Wild (by Jack London)
https://www.gutenberg.org/ebooks/215

"""

import string
import re

class FileAnalyzer:
# Initializer / Instance Attributes
    def __init__(self, filename):
        self.filename = filename
    def readWord(self):
        #read the file and split the words
        with open(self.filename, 'r+', encoding='utf-8') as readFile: #read a book
            wordList = []
            #Breaks each line into words
            for line in readFile: 
                 #lineWords = re.split(r'\s*(?:‘’“”!.-—|,|\t|\n|\s)\s*',line)
                 lineWords = re.findall('[a-zA-Z]+',line)
                 wordList.extend(lineWords)
                 #Strip whitespace and punctuation and onvert to lowercase.
                 wordList = [word.lower().strip(string.punctuation).strip("‘’“”!.,-—") for word in wordList]   
        readFile.close()
        return wordList
    def countWord(self):
        #Count the total number of the words
        print("\nTotal number: ",len(self.readWord())," words.\n")    
    def sortWord(self,order):
        #Sort the words according to the frequency
        listedWord = self.readWord()
        wordSet = set(listedWord) # No repeat
        wordDict = {word: listedWord.count(word) for word in wordSet}
        wordSort=sorted(wordDict.items(),key=lambda x:x[1],reverse=order)
        return wordSort
    def topWord(self,order,number):
        #output the top most/least used words, if order==Ture most,if order==False,least
        sortedWord = self.sortWord(order)
        print("\nTop ", number ," ", ("most" if order==True else "least")," used words:")     
        for i in range(number):
            print('Word:{0}   Times:{1}'.format("%-20s" % sortedWord[i][0],sortedWord[i][1]))
    def longestWord(self,order,number):
        #output the top longest/shortest words , if order==Ture longest,if order==False,shortest
        listedWord = self.readWord()
        wordSet = set(listedWord) 
        wordDict = {word: len(word) for word in wordSet}
        wordSort=sorted(wordDict.items(),key=lambda x:x[1],reverse=order)
        print("\nTop ", number ," ", ("longest" if order==True else "shortest")," words:")     
        for i in range(number):
            print('Word:{0}   Length:{1}'.format("%-20s" % wordSort[i][0],wordSort[i][1]))
        return wordSort
        

# The Call of the Wild
FILE_NAME = 'Wild.txt'
a = FileAnalyzer(FILE_NAME)

#Output the top 10 most used words
a.topWord(True,10)

#Output the top 10 least used words
a.topWord(False,10)

#Output the top 10 longest words
a.longestWord(True,10)

#Output the top 10 shortest words
a.longestWord(False,10)


 
  
#Output the top 10 most used words


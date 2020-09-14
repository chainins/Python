# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:36:45 2020

@author: Chengpi Wu

Homework #5

1. write a function that takes a string as parameter, return true 
if it’s a valid variable name, false otherwise. You can use 
keyword module’s  iskeyword() to determine if a string is keyword.

2. write a function that returns the length of a string (without using len() function)
3. write a function that counts number of vowels in a string
4. write a function that checks if a word is palindrome



"""
import keyword


def validVName(string):
    #check a string, return true if it's  a valid variable name, else false
    count=0
    valid = True
    if(  not string[count:count+1].isalpha()):
        return False
    count +=1
    while(string[count:]):
        if(  not (string[count:count+1].isalpha() or string[count:count+1].isdigit()  or string[count:count+1]=='_')):
            return False
        count +=1
    return not(keyword.iskeyword(string)) and valid

def lengthStr(string):
    #return the length of string
    count=0
    while(string[count:]):
        count +=1
    return count


def numVowel(string):
    #return the number of vowels in a string
    count=0
    vowel="AEIOU"
    pos = 0
    eachV = vowel[0:]
    for i in eachV :
        count = count + string.count(i.lower()) + string.count(i.upper())
        pos +=1
    return count

def checkPalindrome(string):
    #return True if the string is palindrome, else False
    count = len(string)
    pos = 0
    for i in range(int(count/2)) :
        if string[i:i+1].upper() != string[count-i-1:count-i].upper():
            return False
    return True

def printResult(string):
    # print results of calling functions above
    print("The word \"" + strDemo + "\"" + " is " + ("" if(validVName(strDemo)) else "not") + " a valid variable name!")
    print("Length of string \"" + strDemo + "\" is " + str(lengthStr(strDemo)))
    print("The number of vowels in the word \"" + strDemo + "\" is " + str(numVowel(strDemo)))
    print("The word \"" + strDemo + "\"" + " is " + ("" if(checkPalindrome(strDemo)) else "not") + " a palindrome!\n")



strDemo = "EndLetterofString"
printResult(strDemo)
strDemo = "Racecar"
printResult(strDemo)
strDemo = "global"
printResult(strDemo)
strDemo = "Leonardo da Vinci"
printResult(strDemo)
strDemo = "8hooh8"
printResult(strDemo)
strDemo = "abc_123"
printResult(strDemo)
strDemo = "_abba_"
printResult(strDemo)
        


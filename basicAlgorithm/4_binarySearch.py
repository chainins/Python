# -*- coding: utf-8 -*-

###############################################
#                                             #
#     Created on Wed Mar 10 01:58:24 2021     #
#         @author: Chengpi Wu                 #
#                                             #
###############################################

import random
from math import log
from math import floor
import time

def generateKNumbers(k):
  numList =[]
  for i in range(k):
    rdNum = random.randint(0,k*100)
    numList.append(rdNum)
  singleNum = numList[0]
  numList.sort()
  return numList,singleNum

def binarySearchRecursive(datalist,target,startIndex,endIndex,steps=0):
  # recursive solution
  steps += 1
  if startIndex==endIndex:
      if datalist[startIndex] == target:
          return startIndex, steps
      else:
          return -1, steps
  middleIndex = floor((startIndex + endIndex)/2)
  if datalist[middleIndex] == target:
      return middleIndex, steps
  if datalist[middleIndex] < target:
      return binarySearchRecursive(datalist,target,middleIndex+1,endIndex, steps)
  else:
      return binarySearchRecursive(datalist,target,startIndex,middleIndex-1,steps)

def binarySearchIterative(datalist, target):
  startIndex = 0
  endIndex = len(datalist) - 1
  steps = 0
  # Iterative solution
  while startIndex <= endIndex:
    steps += 1
    if startIndex == endIndex:
        return startIndex, steps    
    middleIndex = floor((endIndex + startIndex)/2)
    if datalist[middleIndex] == target:
      return middleIndex, steps
    elif datalist[middleIndex] < target:
      startIndex = middleIndex + 1
    else:
      endIndex = middleIndex - 1
  # if we don't find the target, return None    
  return -1,steps


repeatNum= 1000
sum = 0
k= random.randint(10**3,10**4)
print('Iterative binarySearch\n')
start = time.time()
for i in range(repeatNum):
    aList,searchNum = generateKNumbers(k)
    keyNum,steps = binarySearchIterative(aList, searchNum)
    sum = sum + steps
    
print("average steps: ", float(sum)/repeatNum)
end = time.time()
print('\n### TIME(s):',end - start)

print('\nRecursive binarySearch\n')
start = time.time()
sum = 0
for i in range(repeatNum):
    aList,searchNum = generateKNumbers(k)
    keyNum,steps = binarySearchRecursive(aList, searchNum, 0, len(aList) - 1,0)
    sum = sum + steps
    
print("average steps: ", float(sum)/repeatNum)

end = time.time()
print('\n### TIME(s):',end - start)

print("\nlog(base 2) k: ",log(len(aList),2))

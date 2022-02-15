import random
from math import floor
import time


def rdKNum(k):
  numList =[]
  for i in range(k):
    rdNum = random.randint(0,2**20)
    numList.append(rdNum)
  return numList 

import copy

def mergeSort(L,steps):
    r=len(L) 
    if r>0: 
      m = floor( r /2)
      if m > 1:
          listL,stepL = copy.deepcopy(mergeSort(L[0:m],steps))
      else:
          listL =[copy.deepcopy(L[0])]
          stepL = 1
      if r-m>1:
          listR,stepR = copy.deepcopy(mergeSort(L[m:r],steps))
      else:
          listR =[copy.deepcopy(L[m])]
          stepR = 1
      L,stepM = merge(listL,stepL,listR,stepR)
      return L, stepM
    else: # r=0, only one element
      return L, 0 

def merge(L,stepL,R,stepR):
  i = j = k = 0
  arr=[]
  stepM = stepL + stepR
  while i < len(L) and j < len(R): 
      arr.append(0)
      stepM += 1
      if L[i] < R[j]:  # compare once, count here !
          arr[k] = L[i]
          i += 1
      else:
          arr[k] = R[j]
          j += 1
      k += 1
  # if any elements left
  while i < len(L):
      arr.append(0)
      arr[k] = L[i]
      i += 1
      k += 1
  while j < len(R):
      arr.append(0)
      arr[k] = R[j]
      j += 1
      k += 1  
  return arr,stepM


print('When k = 2**16, \n')
k = 2**16
aList = rdKNum(k)

start = time.time()
keyNum,steps = mergeSort(aList,0)
end = time.time()


print('\n### TIME(s):',end - start)
print('\n### STEPS: ',steps)

print('\n\nWhen k = 2**17, \n')
k = 2**17
aList = rdKNum(k)

start = time.time()
keyNum,steps = mergeSort(aList,0)
end = time.time()

print('\n### TIME(s):',end - start)
print('\n### STEPS: ',steps)


'''
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
'''
import random
from math import log

from math import floor
import time



def rdKNum(k):
  numList =[]
  for i in range(k):
    rdNum = random.randint(0,k*100)
    if rdNum not in numList:
        numList.append(rdNum)
  # singleNum = numList[0]
  # numList.sort()
  return numList #,singleNum

import copy

def mergeSort(L,steps):
    r=len(L) 
    if r>0: # r=0, only one element
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
    else:
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
  # Checking if any element was left
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


k= random.randint(10**1,10**3)

aList = rdKNum(k)

# aList = [5,9, 6,3,7,4,2,1,8]
print(aList)

start = time.time()
keyNum,steps = mergeSort(aList,0)
end = time.time()

print("\nn numbers, n = ", k)

print(keyNum)
print('\n### TIME(s):',end - start)
print('\n### STEPS: ',steps, ', which is between: ')

print('n log n - n + 1: ', int(k*log(k,2) - k + 1))
print('n log n + n + (+ O(lg n)): ', int(k*log(k,2) + k))
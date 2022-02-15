# -*- coding: utf-8 -*-

###############################################
#                                             #
#     Created on Wed Mar  3 19:30:52 2021     #
#         @author: Chengpi Wu                 #
#                                             #
###############################################

def subMod(x,y,n):
    return (x - y ) % n
def modexp(x, y, n):
    # input: two n-bit integers x and N, an integer exponent y
    # output: x^y mod n
    if y == 0:
        return 1
    z = modexp(x, y//2, n)
    if y % 2 == 0:
        return (z * z) % n
    else:
        return (x * z * z) % n

print("(4^1536 - 9^4824) mod 35 = ",subMod(modexp(4,1536,35),modexp(9,4824,35),35))
# line above answer is 0

print("(4^1536 - 9^4824) mod 37 = ",subMod(modexp(4,1536,37),modexp(9,4824,37),37))
# line above answer is 25

import random

def checkCh(p):
    for i in range(128):
        a = random.randint(1,p-1)
        # print(i,a,'\n')
        if modexp(a,p-1,p) != 1:
            return False
    return True


pList=[10106665597294733930808268834911,
       557940830126698960967415391,
       2305567963945518424753102147331756071,
       169665573205075467667167]

for eachP in pList:
    if checkCh(eachP):
        print("%40d has a tiny chance(<2^-128) of not bing A PRIME!!" % eachP)
    else:
        print("%40d is Not A PRIME!" % eachP)


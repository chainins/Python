# -*- coding: utf-8 -*-

###############################################
#                                             #
#     Created on Thu Feb 11 20:06:28 2021     #
#         @author: Chengpi Wu                 #
#                                             #
###############################################

import math
def divide(x,y):
    print(x,y)
    if x == 0:
        return 0,0
    u,v = divide(math.floor(x/2),y)
    u = 2 * u
    v = 2 * v
    if x%2 ==1:
    	v = v + 1
    if v>=y :
        v=v-y
        u=u+1
    print(u,v)
    return u,v

x,y=271,35

print(str(x),'/',str(y),'=',divide(x,y))
        

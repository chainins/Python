# -*- coding: utf-8 -*-

###############################################
#                                             #
#     Created on Fri Mar  5 23:54:46 2021     #
#         @author: Chengpi Wu                 #
#                                             #
###############################################

import numpy as np 
import time
  
def divide(M): 
    # divide a given n*n matrix into 4 n/2 x n/2 matrices 
    R, C = M.shape 
    halfR, halC = R//2, C//2
    return M[:halfR, :halC], M[:halfR, halC:], M[halfR:, :halC], M[halfR:, halC:] 

def divCon7(X, Y, steps=0): # Strassen algorithm for 7 substeps
    # divide-and-conquer square matrix multiplication algorithm
    if len(X) == 1 and len(Y)==1: 
        return X * Y, steps + 1
    # divide the matrices 

    X11, X12, X21, X22 = divide(X) 
    Y11, Y12, Y21, Y22 = divide(Y) 
  
    # Computing the 7 products, recursively (Z1, Z2...Z7) 
    Z1,steps1 = divCon7(X11, Y12 - Y22)   # X11*(Y21-Y22)
    Z2,steps2 = divCon7(X11 + X12, Y22)         
    Z3,steps3 = divCon7(X21 + X22, Y11)         
    Z4,steps4 = divCon7(X22, Y21 - Y11)         
    Z5,steps5 = divCon7(X11 + X22, Y11 + Y22)         
    Z6,steps6 = divCon7(X12 - X22, Y21 + Y22)   
    Z7,steps7 = divCon7(X11 - X21, Y11 + Y12)   

    # Computing the values of the 4 quadrants of the final matrix c 
    R11 = Z5 + Z4 - Z2 + Z6   
    R12 = Z1 + Z2            
    R21 = Z3 + Z4             
    R22 = Z1 + Z5 - Z3 - Z7   
  
    # Combining the 4 quadrants into a single matrix 
    R = np.vstack((np.hstack((R11, R12)), np.hstack((R21, R22))))  
  
    return R,steps1 + steps2  + steps3 + steps4 + steps5 + steps6 + steps7

def divCon8(X, Y, steps=0):  # 8 substeps
    # divide-and-conquer square matrix multiplication algorithm
    if len(X) == 1 and len(Y)==1: 
        return X * Y, steps + 1
    # divide the matrices 

    X11, X12, X21, X22 = divide(X) 
    Y11, Y12, Y21, Y22 = divide(Y) 
  
    # Computing the 8 products, recursively (Z1, Z2...Z8) 
    Z1,steps1 = divCon8(X11, Y11)   # X11*Y11
    Z2,steps2 = divCon8(X12, Y21)         
    Z3,steps3 = divCon8(X11, Y12)         
    Z4,steps4 = divCon8(X12, Y22)         
    Z5,steps5 = divCon8(X21, Y11)      
    Z6,steps6 = divCon8(X22, Y21)   
    Z7,steps7 = divCon8(X21, Y12) 
    Z8,steps8 = divCon8(X22, Y22) 

    # Computing the values of the 4 quadrants of the final matrix c 
    R11 = Z1 + Z2   
    R12 = Z3 + Z4            
    R21 = Z5 + Z6            
    R22 = Z7 + Z8   
  
    # Combining the 4 quadrants into a single matrix 
    R = np.vstack((np.hstack((R11, R12)), np.hstack((R21, R22))))  
  
    return R,steps1 + steps2  + steps3 + steps4 + steps5 + steps6 + steps7 + steps8

def matrixMultReg(X,Y): # regular algorithm
    steps = 0
    result = np.zeros((X.shape[0],Y.shape[1]))
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            for k in range(X.shape[1]):
                result[i][j] += X[i][k] * Y[k][j]
                steps += 1
    return result, steps
  

u,v,w = 32,32,32

x = np.random.randint(10, size=(u,v))
y = np.random.randint(10, size=(v,w))


print('Matrix X*Y\n')

print('\nRegular algorithm:\n')
start = time.time()
result,steps = matrixMultReg(x,y)
print(result)
print('\nSteps: ',steps)
print('\nn**3=',32*32*32, ' for n = ',u)
end = time.time()
print('\n### TIME(s):',end - start)

print('\n\nDivide-and-conquer algorithm(non-Strassen algorithm for 8 substeps):\n')
start = time.time()
result,steps = divCon8(x,y)
print(result)
print('\nSteps: ',steps)
print('\nn**3=',32**3, ' for n = ',u)
end = time.time()
print('\n### TIME(s):',end - start)

print('\n\nDivide-and-conquer algorithm(Strassen algorithm for 7 substeps):\n')
start = time.time()
result,steps = divCon7(x,y)
print(result)
print('\nSteps: ',steps)
print('\nn**2.81= %8.2f' % 32**2.81, ' for n = ',u)
end = time.time()
print('\n### TIME(s):',end - start)




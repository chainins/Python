# -*- coding: utf-8 -*-

# DFS (Deepth First Search for a Undirected Graph Without Distance)

V0 = ['A','B','C','D','E','F','G','H','I']

Graph=[[0,1,0,0,1,0,0,0,0],
          [1,0,1,0,1,0,0,0,0],
          [0,1,0,0,0,1,0,0,0],
          [0,0,0,0,0,0,1,1,0],
          [1,1,0,0,0,1,0,0,0],
          [0,0,1,0,1,0,0,0,1],
          [0,0,0,1,0,0,0,1,0],
          [0,0,0,1,0,0,1,0,0],
          [0,0,0,0,0,1,0,0,0]]

visited = []
branchtraversed = []

currentNode = 0 # the index of the vertex in V0, start from A
startVertex = ['A']
print('The DFS Route: ')

V = ['A','B','C','D','E','F','G','H','I']
visited.append(V[currentNode])

V.remove(V[currentNode])

visitNum = 0
dicVisit = {}
dicVisit[visitNum] = V0[currentNode]
lastNode =''
i= 0
import sys

def checkTraversed(vertex):
    if(not (vertex in visited)):
        return False
    for i in range(9): # search all the vertex connected to current node, push to branchtraversed
        if Graph[V0.index(vertex)][i] == 1 and (not (V0[i] in visited)):
            return False
    return True
    
def updateTraversed():
    for vertex in V0:
        if (checkTraversed(vertex) and not (vertex in branchtraversed)):
            branchtraversed.append(vertex)

while len(V)>0: # or len(visited)<9 , but there still unreached nodes in the graph
    
    i = i + 1
    nextNode = ''
    for i in range(9): # search all the vertex connected to current node, push to branchtraversed
        if Graph[currentNode][i] == 1 and (not (V0[i] in visited)):
            nextNode = V0[i]
            break
    if not nextNode =='':
        visitNum += 1
        lastNode = currentNode
        currentNode = V0.index(nextNode) # get the index of the node
        dicVisit[visitNum] = V0[currentNode]
        print(V0[lastNode]+V0[currentNode],':Forward')
        if(not (V0[currentNode] in visited)):
            visited.append(V0[currentNode])
        V.remove(V0[currentNode]) # remove visited node from V
    else: # no next, back
        visitNum += 1
        if(not (V0[currentNode] in visited)):
            visited.append(V0[currentNode])
        lastNode = currentNode
        updateTraversed()
        if (len(V)>0  and ( (V0[currentNode] in startVertex) or ( len(branchtraversed)==len(visited)))):
            currentNode = V0.index(V[0]) # back to the start vertex, choose a new vertex not connected
            startVertex.append(V[0])
            print(V0[lastNode]+V0[currentNode],':new tree') 
            if(not (V0[currentNode] in visited)):
                visited.append(V0[currentNode])
                V.remove(V0[currentNode])
        else:  # not all visited vertices have been traversed
            currentNode =  V0.index(visited[visited.index(V0[currentNode]) -1 ])
            print(V0[lastNode]+V0[currentNode],':backword') 
        dicVisit[visitNum] = V0[currentNode]
 
    
print('\nThe sequence of the vertices visited: \n',dicVisit.values())

print('\nThe visit number of each vertex:')
for node in V0:
    print('\n',node,end = ' ')
    for number, nodename in dicVisit.items():  
        if nodename == node:
            print(number,end=' ')

print('\n')


# -*- coding: utf-8 -*-

# BFS (Breadth First Search for a Directed Graph with dis)

import copy

import heapq


Map = {
    'AB':1,
    'AE':4,
    'AF':8,
    'BC':2,
    'BF':6,
    'BG':6,
    'CD':1,
    'CG':2,
    'DH':4,
    'DG':1,
    'GH':1,
    'GF':1,
    'EF':5
}

dis = {
  'A':0,
  'B':99999999,
  'C':99999999,
  'D':99999999,
  'E':99999999,
  'F':99999999,
  'G':99999999,
  'H':99999999
}

dis0 = copy.deepcopy(dis)

V0 = ['A','B','C','D','E','F','G','H']
V = ['A','B','C','D','E','F','G','H']

def Dijkstra( map ,dis):
    lastVlist = []
    count = 0
    disTemp = copy.deepcopy(dis)
    startV = min(disTemp, key=disTemp.get)
    while (len(disTemp)>0 and count<1000): # incase negtive edge
        for key in map.keys():
            if key[0] == startV:
                lastVlist.append(key[1])
                count = count + 1
                dis[key[1]] = min(dis[key[1]],dis[key[0]] + map[key])
                disTemp[key[1]] = dis[key[1]]
        disTemp.pop(startV, None)
        if len(disTemp)>0:
            startV = min(disTemp, key=disTemp.get)
    return dis,count


def DijkstraHeap( map ,dis):
    PQ = []
    lastVlist = []
    count = 0
    disTemp = copy.deepcopy(dis)
    startV = min(disTemp, key=disTemp.get)
    heapq.heappush(PQ, startV)
    while (PQ and count<1000):
        startV = heapq.heappop(PQ)
        for key in map.keys():
            if key[0] == startV:
                lastVlist.append(key[1])
                count = count + 1
                if dis[key[1]]>dis[key[0]] + map[key]:
                    dis[key[1]] = dis[key[0]] + map[key]
                    heapq.heappush(PQ, key[1])
                    disTemp[key[1]] = dis[key[1]]
        if len(disTemp)>0:
            startV = min(disTemp, key=disTemp.get)
    return dis,count


def BellmanFord( map ,dis):
    count = 0
    for i in range(len(dis) -1):
        for key in map.keys():
            count = count + 1
            dis[key[1]] = min(dis[key[1]],dis[key[0]] + map[key])   
    checkNegCirc = False
    for key in map.keys():
        if dis[key[1]] > dis[key[0]] + map[key]:
            checkNegCirc = True
    return dis,count,checkNegCirc 
    
print('|V| = ', len(V))
print('|E| = ', len(Map))
result,steps = Dijkstra(Map,dis)
print('\nResult of Dijkstra:\n',result)
print('\nSteps(O(ElgV)):\n',steps)

dis = copy.deepcopy(dis0)
result,steps = DijkstraHeap(Map,dis)
print('\nResult of Dijkstra by PQ:\n',result)
print('\nSteps(O(ElgV)):\n',steps)

dis = copy.deepcopy(dis0)
result,steps,negCirc = BellmanFord(Map,dis)
print('\nResult of BellmanFord:\n',result)
print('\nSteps(|V|*|E|):\n',steps)

if negCirc:
    print('\nThere is a negtive circle.')
else:
    print('\nThere is no negtive circle.')
    
Map = {
    'AB':1,
    'AE':4,
    'FA':-8,
    'BC':2,
    'BF':6,
    'BG':6,
    'CD':1,
    'CG':2,
    'DH':4,
    'DG':1,
    'GH':1,
    'GF':1,
    'EF':5
}

dis = copy.deepcopy(dis0)

print('\n\n###### Test negtive edge:')
result,steps = Dijkstra(Map,dis)
print('\nResult of Dijkstra (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps = DijkstraHeap(Map,dis)
print('\nResult of Dijkstra by PQ (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps,negCirc = BellmanFord(Map,dis)
print('\nResult of BellmanFord:\n',result)
print('\nSteps(|V|*|E|):\n',steps)

if negCirc:
    print('\nThere is a negtive circle.')
else:
    print('\nThere is no negtive circle.')
    
Map = {
    'AB':1,
    'AE':4,
    'AF':8,
    'BC':2,
    'BE':3, # insert an elt
    'BF':6,
    'BG':6,
    'CD':1,
    'CG':2,
    'DH':4,
    'DG':1,
    'GH':1,
    'GF':1,
    'EF':5
}

dis = copy.deepcopy(dis0)
print('\n\n###### Insert an elt(BE=3) to PQ(edge):')
result,steps = Dijkstra(Map,dis)
print('\nResult of Dijkstra (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps = DijkstraHeap(Map,dis)
print('\nResult of Dijkstra by PQ (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps,negCirc = BellmanFord(Map,dis)
print('\nResult of BellmanFord:\n',result)
print('\nSteps(|V|*|E|):\n',steps)

if negCirc:
    print('\nThere is a negtive circle.')
else:
    print('\nThere is no negtive circle.')
 

Map = {
    'AB':1,
    'AE':4,
    'AF':8,
    'BC':5, # reinsert an elt of BC
    'BF':6,
    'BG':6,
    'CD':1,
    'CG':2,
    'DH':4,
    'DG':1,
    'GH':1,
    'GF':1,
    'EF':5
}

dis = copy.deepcopy(dis0)
print('\n\n###### Reinsert an elt(BC=5) to PQ(edge):')
result,steps = Dijkstra(Map,dis)
print('\nResult of Dijkstra (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps = DijkstraHeap(Map,dis)
print('\nResult of Dijkstra by PQ (stop at No.1000 steps):\n',result)
print('\nSteps(|E|+|V|log|V|):\n',steps)

dis = copy.deepcopy(dis0)
result,steps,negCirc = BellmanFord(Map,dis)
print('\nResult of BellmanFord:\n',result)
print('\nSteps(|V|*|E|):\n',steps)

if negCirc:
    print('\nThere is a negtive circle.')
else:
    print('\nThere is no negtive circle.')
 

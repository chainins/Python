# -*- coding: utf-8 -*-

# Group 2: Xinze Yang, Chengpi Wu

# BFS (Breadth First Search for a Directed Graph with Distance)

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

Q = []

route = {'A':'A'}

def setRoute(map):
    for eachKey in map.keys():
        if eachKey[-1] not in route.keys():
            route[eachKey[-1]]=[]
        
setRoute(Map)

def BFS(map, start):
  Q.append(start)
  while Q:
      for key in map.keys():
        if key[0] == Q[0]:
          if dis[key[1]]  > dis[key[0]] + map[key]:
              dis[key[1]] = dis[key[0]] + map[key]
              route[key[1]]= route[key[0]] + key[1]
          Q.append(key[-1])
      Q.pop(0)
  print('shortest distance:\n',dis)
  print('shortest route for each vertex:\n',route)

BFS(Map, 'A')


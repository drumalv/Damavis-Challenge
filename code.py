# -*- coding: utf-8 -*-


import numpy as np

"""
class BOARD

Represents the board of the problem
"""

class Board:

  def __init__(self,snake,n,m):
    
    self.m=m
    self.n=n
    self.board = np.zeros((n,m))
    self.head = snake[0]
    self.snake = np.copy(snake)

    for i in range(len(snake)):
      self.board[snake[i][1]][snake[i][0]]=1

"""
class Sol

Represents one posible amounts of movements 
"""

class Sol:

  def __init__(self,b,c,d): # b class Board
    self.b=Board(b.snake,b.n,b.m)
    self.c=c
    self.depth=d

"""ALGORITHM"""

""" Function to generate the snake after a movement """

def generateSnakeMovement(snake,move):
  newSnake=[]
  if move=="L":
    newSnake.append([snake[0][0]-1,snake[0][1]])
  elif move=="R":
    newSnake.append([snake[0][0]+1,snake[0][1]])
  elif move=="U":
    newSnake.append([snake[0][0],snake[0][1]-1])
  elif move=="D":
    newSnake.append([snake[0][0],snake[0][1]+1])
  
  for i in range(1,len(snake)):
    newSnake.append(snake[i-1])

  return newSnake

""" Function to generate the posible movements of a snake in a board """

def generateNeighbors(sol):

  neighbors=[]
  
  #generate posible neighbors, checking the bounds and that the box is empty

  # neighbor L
  if sol.b.head[0]-1 >= 0 and sol.b.head[0]-1 != sol.b.snake[1][0]:
    #new snake with L movement
    newSnake=generateSnakeMovement(sol.b.snake,"L")
    neighbors.append(Sol(Board(newSnake,sol.b.n,sol.b.m),sol.c+"L",sol.depth+1))
  # neighbor R
  if sol.b.head[0]+1 < sol.b.m and sol.b.head[0]+1!=sol.b.snake[1][0]:
    #new snake with R movement
    newSnake=generateSnakeMovement(sol.b.snake,"R")
    neighbors.append(Sol(Board(newSnake,sol.b.n,sol.b.m),sol.c+"R",sol.depth+1))
  # neighbor U
  if sol.b.head[1]-1 >= 0 and sol.b.head[1]-1!=sol.b.snake[1][1]:
    #new snake with U movement
    newSnake=generateSnakeMovement(sol.b.snake,"U")
    neighbors.append(Sol(Board(newSnake,sol.b.n,sol.b.m),sol.c+"U",sol.depth+1))
  # neighbor D
  if sol.b.head[1]+1 < sol.b.n and sol.b.head[1]+1!=sol.b.snake[1][1]:
    #new snake with D movement
    newSnake=generateSnakeMovement(sol.b.snake,"D")
    neighbors.append(Sol(Board(newSnake,sol.b.n,sol.b.m),sol.c+"D",sol.depth+1))

  return neighbors

""" Algorithm of the problem """
# b board
# generate neighbors until the indicate depth and return the solutions and the 
# number of posible amounts of movements
def numberOfAvailableDifferentPaths(b, depth):
    
  listofSol=[]
  solIni=Sol(b,"",0)
  depth_act=1
  
  #generate the initial neigbor
  neighbors=generateNeighbors(solIni)
  listofSol.extend(neighbors)
  
  #if its empty, return 0
  if len(neighbors)==0: return listofSol,0
  
  while(depth_act<depth):
    while(listofSol[0].depth!=depth_act+1):
        listofSol.extend(generateNeighbors(listofSol[0]))
        listofSol.pop(0)
    
    depth_act+=1
  
  
  return listofSol, len(listofSol)


snake=[[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
b = Board(snake,3,4)
lista,num=numberOfAvailableDifferentPaths(b,3)


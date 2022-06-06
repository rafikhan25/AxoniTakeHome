# Rafi Khan - AXONI TAKE HOME PROBLEM
# 06/06/2022

#PLAN: 
# 1) implement Breadth-first-search method such that it can enqueue nodes (flight stops/locations in this case) and have a data structure store the yet to be explored locations (queue) 

# 2) define solution method (shortestPaths) and separate arrange flights string into locations as keys with lists of adjacent locations (adjacency lists) as values. 

# 3) Check to see if destination can be explored from starting node using bfs. If yes, then store that path in accumulator variable and repeat with other paths

# 4) Return the accumulator variable with all paths from source to destination




class Solution:
  
  visitedNodes = []
  queuedNodes = []

  def bfs(visitedNodes, graph, location):
    visitedNodes = []
    queuedNodes = []
    visitedNodes.append(location)

    queuedNodes.append(location)

    while queuedNodes:
      x = queuedNodes.pop(0)

      for adjacent in graph[x]:
        if adjacent not in visitedNodes:
          visitedNodes.append(adjacent)
          queuedNodes.append(adjacent)
  
  def shortestPaths(self,flights,src,dest,):
    new = []
    if src not in flights or dest not in flights:
      return None
      
    #this line separates each line in the variable "flights"
    x = flights.split("\n")

    #these next three lines add every location to the "new" variable
    for line in x:
      y = line.split("->")
      new.append(y)


  

#INCOMPLETE CODE
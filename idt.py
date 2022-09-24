from collections import defaultdict
from time import process_time
import sys
'''
Developed by: Mikey Joyce 
    for HW2 with group Jake Rogers and Roshan Neupane

!!! DISCLAIMER !!!
This code was adapted from https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
I used this link to help adapt this program and must give credit where credit is due.
'''

myTime = process_time()

# This class represents our 20 room environment
class Room:
    def __init__(self, vertices, map):
        self.V = vertices
        self.room = defaultdict(list)
        self.map = map

        #stores costs
        self.left = 1.0
        self.right = 0.9
        self.up = 0.8
        self.down = 0.7
        self.suck = 0.6
        self.cost = 0.0

        self.dirty = 0
        self.getDirtyRooms()
 
    # Returns the amount of dirty rooms at the start
    def getDirtyRooms(self):
        for row in self.map:
            for node in row:
                if node == 1:
                    self.dirty += 1

    def addEdge(self, index, target):
        self.room[index].append(target)

    # A function to perform a Depth-Limited search from given source
    def DLS(self, src, target, maxDepth, path, generated, root):
        if self.map[src[0]][src[1]] == target:
            self.map[src[0]][src[1]] = 0
            self.cost += self.suck
            self.dirty -= 1
            return True
 
        # If reached the maximum depth then stop recursing.
        if maxDepth <= 0 : return False
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.room[src]:
            #print(i)
            if i not in generated and i != root:
                generated.append(i)
            if(self.DLS(i,target,maxDepth-1, path, generated, root)):
                path.append(i)
                return True
        return False
 
    # Iterative Deepening Search
    def idt_search(self, src, target, maxDepth, path, generated, root):
        # Repeatedly depth-limit search till the maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i, path, generated, root)):
                return True
        return False
    
    # This function finds the total cost that the algorithm took
    def findCost(self, last, current):
        if(current[0] == last[0]+1):
            self.cost += self.down
        elif(current[0] == last[0]-1):
            self.cost += self.up
        elif(current[1] == last[1]+1):
            self.cost += self.right
        elif(current[1] == last[1]-1):
            self.cost += self.left
    
def createRoom(map):
    # Create an interconnected room structure given by the 20 room environment in the HW2 pdf
    room = Room (20, map)
    room.addEdge((0,0), (0,1))
    room.addEdge((0,0), (1,0))

    room.addEdge((1,0), (1,1))
    room.addEdge((1,0), (2,0))
    room.addEdge((1,0), (0,0))

    room.addEdge((2,0), (2,1))
    room.addEdge((2,0), (3,0))
    room.addEdge((2,0), (1,0))

    room.addEdge((3,0), (3,1))
    room.addEdge((3,0), (2,0))

    room.addEdge((3,1), (3,2))
    room.addEdge((3,1), (2,1))
    room.addEdge((3,1), (3,0))

    room.addEdge((2,1), (1,1))
    room.addEdge((2,1), (2,2))
    room.addEdge((2,1), (3,1))
    room.addEdge((2,1), (2,0))

    room.addEdge((1,1), (1,2))
    room.addEdge((1,1), (0,1))
    room.addEdge((1,1), (1,0))
    room.addEdge((1,1), (2,1))

    room.addEdge((0,1), (0,2))
    room.addEdge((0,1), (0,0))
    room.addEdge((0,1), (1,1))

    room.addEdge((0,2), (1,2))
    room.addEdge((0,2), (0,3))
    room.addEdge((0,2), (0,1))

    room.addEdge((1,2), (1,3))
    room.addEdge((1,2), (2,2))
    room.addEdge((1,2), (1,1))
    room.addEdge((1,2), (0,2))

    room.addEdge((2,2), (2,3))
    room.addEdge((2,2), (3,2))
    room.addEdge((2,2), (2,1))
    room.addEdge((2,2), (1,2))

    room.addEdge((3,2), (3,3))
    room.addEdge((3,2), (3,1))
    room.addEdge((3,2), (2,2))

    room.addEdge((3,3), (3,4))
    room.addEdge((3,3), (2,3))
    room.addEdge((3,3), (3,2))

    room.addEdge((2,3), (2,4))
    room.addEdge((2,3), (1,3))
    room.addEdge((2,3), (2,2))
    room.addEdge((2,3), (3,3))

    room.addEdge((1,3), (1,4))
    room.addEdge((1,3), (0,3))
    room.addEdge((1,3), (1,2))
    room.addEdge((1,3), (2,3))

    room.addEdge((0,3), (0,4))
    room.addEdge((0,3), (1,3))
    room.addEdge((0,3), (0,2))

    room.addEdge((0,4), (1,4))
    room.addEdge((0,4), (0,3))

    room.addEdge((1,4), (2,4))
    room.addEdge((1,4), (0,4))
    room.addEdge((1,4), (1,3))

    room.addEdge((2,4), (3,4))
    room.addEdge((2,4), (1,4))
    room.addEdge((2,4), (2,3))

    room.addEdge((3,4), (2,4))
    room.addEdge((3,4), (3,3))

    return room

def algorithm(room, starting_position, path, target_state, maxDepth, generated, root):
    while(room.dirty != 0):
        temp = [starting_position]
        if room.idt_search(starting_position, target_state, maxDepth, temp, generated, root) == True:
            temp.pop(0)
            i=len(temp)
            while(i!=0):
                path.append(temp[i-1])
                i -= 1

            starting_position = path[-1]
        else:
            print ("Error")

    for i in range(len(path)-1):
        room.findCost(path[i], path[i+1])
    print("Cost: ", room.cost)
    print("Path: ", path)
    print("generated: ", generated)

room1 = createRoom([[0,1,0,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1],
                    [0,0,0,0,0]])

room2 = createRoom([[0,1,0,0,0],
                    [1,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]])

path1 = [(1,1)] #initialized with the starting position
path2 = [(2,1)] #initialized with the starting position
#keep track of expanded and generated nodes
generated1, generated2 = [], []
target_state = 1
maxDepth = 8

if(sys.argv[1] == "0"):
    algorithm(room1, path1[0], path1, target_state, maxDepth, generated1, path1[0])
else:
    algorithm(room2, path2[0], path2, target_state, maxDepth, generated2, path2[0])

stop = process_time()
print("CPU Time: ", stop-myTime)
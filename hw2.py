from tokenize import ContStr

x, y = 4, 5

#0 indicates clean; 1 indicates dirty
#data set for uniform cost tree search
room1_UCT = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]]
room2_UCT = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]

#data set for uniform cost graph search
room1_UCG = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]]
room2_UCG = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]

#data set for iterative deepening tree search
room1_IDT = [[0,1,0,0,0],
             [0,2,0,1,0],
             [0,0,0,0,1],
             [0,0,0,0,0]]
room2_IDT = [[0,1,0,0,0],
             [1,0,0,1,0],
             [0,2,1,0,0],
             [0,0,0,0,0]]

#costs
left = 1.0
right = 0.9
up = 0.8
down = 0.7
suck = 0.6


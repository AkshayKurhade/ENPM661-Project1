import numpy as np
import os
import collections
import Functions

# import warnings
# warnings.filterwarnings(action='ignore', category=FutureWarning)

# Node_state = [[0, 0]]  # storing parent child state info

Final_node_state = []  # Final state info

initial_state = []  # matrix to store initial configuration

final_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # final puzzle configuration

# Reading the initial puzzle configuration
print("enter the initial state list")
for x in range(3):
    initial_state.append(list(map(int, input().rstrip().split())))

# initial_state = [[1, 7, 3], [5, 8, 2], [6, 0, 4]]
start_config = np.array(initial_state)

testarray = start_config.flatten()
##Before starting checking whether the puzzle is solvable
solvable = Functions.IsPuzzleSolvable(testarray) == 1

if solvable == 1:
    print(" Puzzle is solvable\n Solving the puzzle....\n Please be patient this may take a while..")
    visited = set()
    parent_index = 0
    child_index = 0
    nodes_list = []
    # start_node = start_config
    start_node = Functions.mattostring(start_config)
    nodes_list.append([start_node, -1])
    queue = collections.deque()
    queue.append(0)
    i = 0
    temp = np.empty(4, dtype='object')  # All nodes after a move are stored as an object to reduce to access type
    reached_finalstate = False

    live_node = ""
    while queue:
        parent_index = queue.popleft()
        live_node = nodes_list[parent_index][0]
        # Locate and move blank tile if possible
        temp[0] = Functions.ActionMoveLeft(live_node)
        temp[1] = Functions.ActionMoveRight(live_node)
        temp[2] = Functions.ActionMoveUp(live_node)
        temp[3] = Functions.ActionMoveDown(live_node)

        for b in range(0, 4):
            # Check if the move action returns empty or is already visited
            if (temp[b] is not None) and (temp[b] not in visited):
                visited.add(temp[b])  # add it to the list of visited nodes
                Functions.WriteNode(temp[b])  # Write Traversed Node to "Nodes.txt"
                Functions.WriteNodeInfo(len(nodes_list) - 1, parent_index)  # write parent child info to "NodesInfo.txt"
                nodes_list.append([temp[b], parent_index])
                queue.append(len(nodes_list) - 1)

                if (temp[b] == Functions.mattostring(final_state)):
                    goal_node = len(nodes_list)
                    queue.clear()
                    reached_finalstate = True
                    break
            if reached_finalstate:
                break
    print("Path Found..\n Wrapping Up..")
    Final_node_state.append(nodes_list[-1][0])  # Goal
    parent = nodes_list[-1][1]  # parent to the goal
    while parent != -1:
        Final_node_state.append(nodes_list[parent][0])
        parent = nodes_list[parent][1]
    # Reverse the path so its from start to goal
    Final_node_state.reverse()
    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    file = open("nodePath.txt", "w")
    for count, move in enumerate(Final_node_state):
        emptystring = ""
        for i in range(0, len(move)):
            emptystring = emptystring + str(move[i]) + " "
        emptystring = emptystring + "\n"
        file.write(emptystring)


else:
    print("Puzzle is unsolvable..\n Try a Different Combination")

import numpy as np
import os
import collections

info_file = open("NodesInfo.txt", "a+")
nodes_file = open("Nodes.txt", "a+")
# import warnings
#
# warnings.filterwarnings(action='ignore', category=FutureWarning)

Node_state = [[0, 0]]  # storing parent child state info

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


def mattostring(testarray):
    i = 0
    nospace = ""  # Create an empty string which will be the single line print out
    for col in range(0, 3):
        for row in range(0, 3):
            nospace = nospace + str(testarray[row, col])
            i += 1
    return nospace


def stringtomat(nonspaced_str):
    nonspaced_str = list(nonspaced_str)
    i = 0
    mat = np.empty([3, 3])
    mat = mat.astype('int')
    for col in range(0, 3):
        for row in range(0, 3):
            mat[row, col] = int(nonspaced_str[i])
            i += 1
    return mat


# finding blank tile location
def BlankTileLocation(CurrentNode):
    row, col = np.where(CurrentNode == 0)
    return row, col


# Move Blank Tile to Left
def ActionMoveLeft(CurrentNode):
    CurrentNode = stringtomat(CurrentNode)
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j == 0:
        status = False
        return
    else:
        status = True
        newNode[i, j] = CurrentNode[i, j - 1]
        newNode[i, j - 1] = 0
        newNode = mattostring(newNode)
    return newNode


# Move Blank Tile to Right
def ActionMoveRight(CurrentNode):
    CurrentNode = stringtomat(CurrentNode)
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j == 2:
        status = False
        return
    else:
        status = True
        newNode[i, j] = CurrentNode[i, j + 1]
        newNode[i, j + 1] = 0
        newNode = mattostring(newNode)

    return newNode


# Move Blank Tile UP
def ActionMoveUp(CurrentNode):
    CurrentNode = stringtomat(CurrentNode)
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i == 0:
        status = False
        return
    else:
        status = True
        newNode[i, j] = CurrentNode[i - 1, j]
        newNode[i - 1, j] = 0
        newNode = mattostring(newNode)
    return newNode


# Move Blank Tile DOWN
def ActionMoveDown(CurrentNode):
    CurrentNode = stringtomat(CurrentNode)
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i == 2:
        status = False
        return
    else:
        status = True
        newNode[i, j] = CurrentNode[i + 1, j]
        newNode[i + 1, j] = 0
        newNode = mattostring(newNode)

    return newNode


def CheckNodePresence(testnode, list):
    l = len(list)
    testnode_copy = testnode.copy()
    for k in range(l):
        state = False
        if np.array_equal(list[k], testnode_copy):
            state = True
            break
    return state


def IsPuzzleSolvable(puzzletest):
    inv_count = 0
    for i in range(0, 8):
        for j in range(i + 1, 9):
            if (puzzletest[j] and puzzletest[i] and puzzletest[i] > puzzletest[j]):
                inv_count += 1
    return inv_count % 2 == 0


def WriteNode(flatarray):
    temp_string = ""
    for i in range(0, 9):
        temp_string = temp_string + str(flatarray[i]) + " "
    temp_string = temp_string + "\n"
    nodes_file.write(temp_string)


def WriteNodeInfo(child_index, parent_index):
    write_row = str(child_index) + " " + str(parent_index) + " " + str(0) + "\n"
    info_file.write(write_row)


a = IsPuzzleSolvable(testarray) == 1

if a == 1:
    print(" Puzzle is solvable\n Solving the puzzle....\n Please be patient this may take a while..")
    board_tracker = set()
    parent_index = 0
    child_index = 0
    nodes_list = []
    # start_node = start_config
    start_node = mattostring(start_config.copy())
    nodes_list.append([start_node, -1])
    queue = collections.deque()
    queue.append(0)
    i = 0
    temp = np.empty(4, dtype='object')
    reached_finalstate = False
    # Final_node_state.append(start_node)
    live_node = ""
    while queue:
        parent_index = queue.popleft()
        live_node = nodes_list[parent_index][0]
        temp[0] = ActionMoveLeft(live_node)
        temp[1] = ActionMoveRight(live_node)
        temp[2] = ActionMoveUp(live_node)
        temp[3] = ActionMoveDown(live_node)

        for b in range(0, 4):
            # Don't want empty entries and don't want any repeat entries
            if (temp[b] is not None) and (temp[b] not in board_tracker):
                board_tracker.add(temp[b])  # add it to the board_tracker
                WriteNode(temp[b])
                WriteNodeInfo(len(nodes_list) - 1, parent_index)
                nodes_list.append([temp[b], parent_index])
                queue.append(len(nodes_list) - 1)

                if (temp[b] == mattostring(final_state)):
                    goal_node = len(nodes_list)  # -1 #-1 to compensate for 0 index
                    # Clear everything else so the program stops here
                    queue.clear()
                    reached_finalstate = True
                    break
            if reached_finalstate:
                break
    print("Path Found..\n Wrapping Up")
    Final_node_state.append(nodes_list[-1][0])  # Goal
    parent = nodes_list[-1][1]  # parent to the goal
    while (parent != -1):
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
    print("Puzzle is unsolvable")

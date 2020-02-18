import numpy as np
import os

Node_state = [[0, 0]]  # storing parent child state info

Final_node_state = []  # Final state info

initial_state = []  # matrix to store initial configuration

final_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # final puzzle configuration

# Reading the initial puzzle configuration
print("enter the initial state list")
for x in range(3):
    initial_state.append(list(map(int, input().rstrip().split())))

start_config = np.array(initial_state)

testarray= start_config.flatten()

# finding blank tile location
def BlankTileLocation(CurrentNode):
    row, col = np.where(CurrentNode == 0)
    return row, col

# Move Blank Tile to Left
def ActionMoveLeft(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j == 0:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i, j - 1]] = newNode[[i, j - 1]], newNode[[i, j]]
    return status, newNode


# Move Blank Tile to Right
def ActionMoveRight(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j < 2:
        status = True
        newNode[[i, j]], newNode[[i, j + 1]] = newNode[[i, j + 1]], newNode[[i, j]]
    else:
        status = False

    return status, newNode


# Move Blank Tile UP
def ActionMoveUp(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i == 0:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i - 1, j]] = newNode[[i - 1, j]], newNode[[i, j]]
    return status, newNode


# Move Blank Tile DOWN
def ActionMoveDown(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i < 2:
        status = True
        newNode[[i, j]], newNode[[i + 1, j]] = newNode[[i + 1, j]], newNode[[i, j]]
    else:
        status = False

    return status, newNode


def CheckNodePresence(testnode, list):
    l=len(list)
    testnode_copy=np.copy(testnode)
    for k in range(l):
        state = False
        if np.array_equal(list[k], testnode_copy):
            state = True
            break
    return state
def IsPuzzleSolvable(puzzletest):
    inv_count=0
    for i in range(0,8):
        for j in range (i+1,9):
            if(puzzletest[j] and puzzletest[i] and puzzletest[i] > puzzletest[j]):
                inv_count+=1
    return inv_count % 2 == 0
a=IsPuzzleSolvable(testarray) == 1
print(a)
if(a ==1):
    print("is solvable")

    parent_index = 0
    child_index = 0
    start_node = start_config
    Final_node_state.append(start_node)

    while child_index <= len(Final_node_state):
        live_node = Final_node_state[parent_index]

        status, left_temp = ActionMoveLeft(live_node)
        if status == 1:
            if CheckNodePresence(left_temp, Final_node_state) == False:
                Final_node_state.append(left_temp)
                child_index += 1
        Node_state.append([parent_index, child_index])

        status, right_temp = ActionMoveRight(live_node)
        if status == 1:
            if CheckNodePresence(right_temp, Final_node_state) == 0:
                Final_node_state.append(right_temp)
                child_index += 1
        Node_state.append([parent_index, child_index])

        status, up_temp = ActionMoveUp(live_node)
        if status == 1:
            if CheckNodePresence(up_temp, Final_node_state) == 0:
                Final_node_state.append(up_temp)
                child_index += 1
        Node_state.append([parent_index, child_index])

        status, down_temp = ActionMoveDown(live_node)
        if status == 1:
            if CheckNodePresence(down_temp, Final_node_state) == 0:
                Final_node_state.append(down_temp)
                child_index += 1
        Node_state.append([parent_index, child_index])

        parent_index += 1

        if np.array_equal(left_temp, final_state):
            print(left_temp)
            break
        if np.array_equal(right_temp, final_state):
            print(right_temp)
            break
        if np.array_equal(up_temp, final_state):
            print(up_temp)
            break
        if np.array_equal(down_temp, final_state):
            print(down_temp)
            break

    lists =[]
    final_state = final_state.transpose()
    lists.append(final_state)
    NodeState_length = len(Node_state)
    Node_state = np.array(Node_state)

    X = Node_state[NodeState_length-1]
    element1 = X[0]
    element2 = X[1]
    print(element2, element1)
    count = 0
    while element1 != 0:
        for i in range(NodeState_length):
            X = Node_state[i]
            if X[1] == element1:
                element1 = X[0]
                element2 = X[1]
                Y = Final_node_state[element2]
                Y = np.array(Y)
                Y = Y.T
                listY = Y.tolist()
                lists.append(listY)
                count += 1
                print(element2, element1)

    start_node = np.array(start_config)
    start_node = start_node.T
    lists.append(start_node)
    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")

    file = open("Nodes.txt", "a")
    X = Final_node_state
    for item in X:
        for element in item.T:
            for index in element:
                file.write("%i\t" % index)
        file.write("\n")
    file.close()

    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")

    file = open("NodesInfo.txt", "a")
    Z = Node_state.tolist()
    for item in Z:
        for index in reversed(range(2)):
            file.write("%i\t" % item[index])
        file.write("0")
        file.write("\n")
    file.close()

    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    file = open("nodePath.txt", "w")
    for a in reversed(lists):
        for element in a:
            for index in element:
                file.write("%i\t" % index)
        file.write("\n")
    file.close()

    print("no of nodes created: ", len(Final_node_state))
else:
    print("unsolvable")

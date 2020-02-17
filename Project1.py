import numpy as np

Node_state = [[0, 0]]  # storing parent child state info

Final_node_state = []  # Final state info

initial_state = []  # matrix to store initial configuration

final_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # final puzzle configuration

# Reading the initial puzzle configuration
print("enter the initial state list")
for x in range(3):
    initial_state.append(list(map(int, input().rstrip().split())))

start_config = np.array(initial_state)
print(initial_state)


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
    if j == 2:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i, j + 1]] = newNode[[i, j + 1]], newNode[[i, j]]
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
    if i == 2:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i + 1, j]] = newNode[[i + 1, j]], newNode[[i, j]]
    return status, newNode


def CheckNodePresence(testnode,list):
    l=len(list)
    testnode_copy=np.copy(testnode)
    for k in range(l):
        state=0
        if np.array_equal(list(k),testnode_copy):
            state=1
            break
    return state


parent_index = 0
child_index = 0
Final_node_state.append(start_config)

while child_index <= len(Final_node_state):
    live_node = Final_node_state[parent_index]

    status, left_temp = ActionMoveLeft(live_node)
    if status == 1:
        if CheckNodePresence(left_temp,Final_node_state) == 0:
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
            Final_node_state.append(ActionMoveUp())
            child_index += 1
    Node_state.append([parent_index, child_index])

    status, down_temp = ActionMoveDown(live_node)
    if status == 1:
        if CheckNodePresence(down_temp, Final_node_state) == 0:
            Final_node_state.append(down_temp)
            child_index += 1
    Node_state.append([parent_index, child_index])
parent_index += 1


if np.array_equal(left_temp,final_state):
    print(left_temp)
    break
if np.array_equal(right_temp,final_state):
    print(right_temp)
    break
if np.array_equal(up_temp,final_state):
    print(up_temp)
    break
if np.array_equal(down_temp,final_state):
    print(down_temp)
    break




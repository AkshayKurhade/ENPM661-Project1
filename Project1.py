import numpy as np

Node_state = [[0, 0]]  # storing parent child state info

Final_node_state = []  # Final state info

initial_state = []  # matrix to store initial configuration
print("enter the initial state list")
for x in range(3):
    initial_state.append(list(map(int, input().rstrip().split())))

start_config = np.array(initial_state)
print(initial_state)


# finding blank tile location

def BlankTileLocation(CurrentNode):
    row, col = np.where(CurrentNode == 0)
    return row, col


def ActionMoveLeft(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j == 0:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i, j-1]] = newNode[[i, j-1]], newNode[[i, j]]
    return status, newNode

def ActionMoveRight(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if j == 2:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i, j+1]] = newNode[[i, j+1]], newNode[[i, j]]
    return status, newNode

def ActionMoveUp(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i == 0:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i-1, j]] = newNode[[i-1, j]], newNode[[i, j]]
    return status, newNode

def ActionMoveDown(CurrentNode):
    newNode = np.copy(CurrentNode)
    [i, j] = BlankTileLocation(newNode)
    if i == 2:
        status = False
    else:
        status = True
    newNode[[i, j]], newNode[[i+1, j]] = newNode[[i+1, j]], newNode[[i, j]]
    return status, newNode



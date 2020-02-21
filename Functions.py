import numpy as np

info_file = open("NodesInfo.txt", "a+")
nodes_file = open("Nodes.txt", "a+")


# mattostring converts a 3x3 matrix to a single nonspaced string
def mattostring(testarray):
    i = 0
    nospace = ""  # Create an empty string which will be the single line print out
    for col in range(0, 3):
        for row in range(0, 3):
            nospace = nospace + str(testarray[row, col])
            i += 1
    return nospace


# stringtomat converts a nonspaced string to a 3x3 matrix
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

        return
    else:

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

        return
    else:

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

        return
    else:

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

        return
    else:

        newNode[i, j] = CurrentNode[i + 1, j]
        newNode[i + 1, j] = 0
        newNode = mattostring(newNode)

    return newNode


# IsPuzzleSolvable checks for the solvability of the puzzle
def IsPuzzleSolvable(puzzletest):
    inv_count = 0
    for i in range(0, 8):
        for j in range(i + 1, 9):
            if (puzzletest[j] and puzzletest[i] and puzzletest[i] > puzzletest[j]):
                inv_count += 1
    return inv_count % 2 == 0


# WriteNode writes all visited nodes to "Nodes.txt" file
def WriteNode(flatarray):
    temp_string = ""
    for i in range(0, 9):
        temp_string = temp_string + str(flatarray[i]) + " "
    temp_string = temp_string + "\n"
    nodes_file.write(temp_string)


# WriteNodeInfo writes the parent child node relationships to the "NodesInfo.txt file
#   0 padding is for algorithms involving costs
def WriteNodeInfo(child_index, parent_index):
    write_row = str(child_index) + " " + str(parent_index) + " " + str(0) + "\n"
    info_file.write(write_row)

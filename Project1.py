import numpy as np

Node_state = [[0, 0]]  # storing parent child state info

Final_node_state = []  # Final state info

initial_state = []  # matrix to store initial configuration
print("enter the initial state list")
for i in range(3):
    initial_state.append(list(map(int, input().rstrip().split())))

start_config = np.array(initial_state)
print(initial_state)


# finding blank tile location

def blanktile_location(at_node):
    row, col = np.where(at_node == 0)
    return row, col

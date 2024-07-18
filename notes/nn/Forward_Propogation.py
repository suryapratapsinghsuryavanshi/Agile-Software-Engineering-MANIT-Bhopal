import numpy as np

input_data = np.array([1, 2])

weights = {
    'node0': np.array([1, 1]),
    'node1': np.array([-1, 1]),
    'output': np.array([2, -1])
}

# Calculate the node0, node1 value with corsponding weights
node_0_value = (input_data * weights['node0']).sum()
node_1_value = (input_data * weights['node1']).sum()

hidden_layer_result = np.array([node_0_value, node_1_value])
print(hidden_layer_result) # [3 1]

output = (hidden_layer_result * weights['output']).sum()
print(output) # 5

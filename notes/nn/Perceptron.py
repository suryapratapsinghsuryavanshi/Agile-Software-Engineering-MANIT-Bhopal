import numpy as np
THETA = 0

def step_activation(y_in):
    if y_in > THETA:
        return 1
    elif y_in == 0:
        return 0
    elif y_in < THETA:
        return -1

input_data = np.array([
    [1, 1, 1, 1],
    [-1, 1, -1, -1],
    [1, 1, 1, -1],
    [1, -1, -1, 1]
])

target_data = np.array([1, 1, -1, -1])
weights = np.array([0, 0, 0, 0])
bias = 0
alpha = 1
epoch = 0

cnt = 0
while cnt != 1:
    epoch += 1
    for i in range(4):
        sm = (input_data[i] * weights).sum() + bias
        output = step_activation(sm)
        print(sm, weights, output, output == target_data[i])
        if output != target_data[i]:
            weights = (weights + (alpha * (target_data[i] * input_data[i])))
            bias = (bias + (alpha * target_data[i]))
            cnt -= 1
    cnt += 1

print(f'''
Perceptron Network for : AND Logic gete
Epoch: {epoch}
Weight: {weights}
Bias: {bias}
''')
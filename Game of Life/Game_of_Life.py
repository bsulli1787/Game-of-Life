import pandas as pd
import numpy as np

input_size = 10

initial_array = np.random.randn(input_size + 2, input_size + 2)
initial_array = np.array([i >= 0.5 for i in initial_array], dtype = int)
cycle_array = np.zeros_like(initial_array, dtype=int)

for j in range(1, np.shape(initial_array)[0] - 1):
    for i in range(1, np.shape(initial_array)[1] - 1):
        cycle_array[i][j] = np.sum(initial_array[i - 1][j - 1: j + 1] + initial_array[i][j - 1: j + 1] + initial_array[i + 1][j - 1: j + 1]).astype(int)
        print('slice = ', initial_array[i - 1][j - 1: j + 1], initial_array[i][j - 1: j + 1], initial_array[i + 1][j - 1: j + 1])
        print('i, j = ', i, j, 'cell = ', cycle_array[i][j])
        #i += 1
    #j+=1
print(initial_array)
print(cycle_array)



import pandas as pd
import numpy as np

input_size = 100

initial_array = np.random.randn(input_size + 2, input_size + 2)
initial_array = [i >= 0.5 for i in initial_array]
cycle_array = []
#df_layout = pd.DataFrame(initial_matrix, dtype = int)
#df_cycle = pd.DataFrame().reindex_like(df_layout)
for j in range(1, np.shape(initial_array)[0] - 1):
    for i in range(1, np.shape(initial_array)[1] - 1):
        cycle_array[i,j] = sum(initial_array[i - 1: i + 1][j - 1: j + 1])
        i += 1
    j+=1
print(cycle_array)



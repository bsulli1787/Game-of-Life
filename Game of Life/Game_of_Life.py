import pandas as pd
import numpy as np

input_size = 100

initial_matrix = np.random.randn(input_size + 2, input_size + 2)
initial_matrix = [i >= 0.5 for i in initial_matrix]

df_layout = pd.DataFrame(initial_matrix, dtype = int)
df_cycle = pd.DataFrame().reindex_like(df_layout)
df_cycle.iloc[1:input_size - 1, 1:input_size - 1] = df_layout.loc[i - 1: i + 1, i - 1: i + 1].sum()
print(df_layout)



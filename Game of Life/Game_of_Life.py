import pandas as pd
import numpy as np

initial_matrix = np.random.randn(100,100)
initial_matrix = [i >= 0.5 for i in initial_matrix]

df_layout = pd.DataFrame(initial_matrix, dtype = int)

print(df_layout)



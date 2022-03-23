import numpy as np
import pandas as pd


df = pd.DataFrame([['a', 1, 2], ['b', np.nan, 4], ['a', 5, 6]], columns = ['x', 'y', 'z'])

y_is_na = df['y'].isna()
df[y_is_na]

z_biger_than_2 = df['z'] > 2
df[z_biger_than_2]

df.groupby('x').sum()

df['a'] = [1, 2, 3]

del df['a']

df



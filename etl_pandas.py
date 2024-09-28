import pandas as pd

df = pd.read_csv('data/measurements.txt',
                 sep=";",
                 header=None,
                 names=['station', 'measure']
                 )
print(df)




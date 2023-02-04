import pandas as pd

df1 = pd.read_csv('data/read_csv_sample.csv')
print(df1)
print()

# header = *0 /None/인덱스명
# index_col = *None /컬럼명
df2 = pd.read_csv('data/read_csv_sample.csv',
                  header=None)
print(df2)
print()

df3 = pd.read_csv('data/read_csv_sample.csv',
                  index_col=None)
print(df3)
print()

df4 = pd.read_csv('data/read_csv_sample.csv',
                  index_col='c0')
print(df4)

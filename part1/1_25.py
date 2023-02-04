import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print(type(df))
print()

addition = df + 10
print(addition.head())
print(type(addition))
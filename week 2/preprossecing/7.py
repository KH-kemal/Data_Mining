import pandas as pd

dataset = pd.read_csv('titanic.csv')
sex_counts = dataset['Sex'].value_counts()
print(sex_counts)
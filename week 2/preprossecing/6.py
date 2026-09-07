import pandas as pd

dataset = pd.read_csv('titanic.csv')
pclass_counts = dataset['Pclass'].value_counts().sort_index()
print(pclass_counts)
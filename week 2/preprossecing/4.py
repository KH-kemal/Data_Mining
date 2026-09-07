import pandas as pd

dataset = pd.read_csv('titanic.csv')
kelas = dataset[['Survived']]
print(kelas)
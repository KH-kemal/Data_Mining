import pandas as pd

dataset = pd.read_csv('titanic.csv')
data = dataset[['Age','Fare']].copy()
print('Data Fitur: \n',data)
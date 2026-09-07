import pandas as pd 

dataset = pd.read_csv('titanic.csv')
data = dataset[['Name', 'Sex', 'Age', 'Pclass', 'Fare']]

print(data)
import pandas as pd

dataset = pd.read_csv('titanic.csv')
data = dataset[['Name', 'Sex', 'Age', 'Pclass', 'Fare']].copy()
data['Relatives'] = dataset['SibSp'] + dataset['Parch']
print(data)
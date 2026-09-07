import pandas as pd

dataset = pd.read_csv('titanic.csv')
survived_pclass = pd.crosstab(dataset['Pclass'], dataset['Survived'])
print(survived_pclass)
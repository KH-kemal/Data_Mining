import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('titanic.csv')

# Convert Sex ke numerik (male=1, female=0)
sex_numeric = (dataset['Sex'] == 'male').astype(int)

plt.figure(figsize=(10, 4))
plt.scatter(dataset.index, sex_numeric, c=dataset['Survived'], cmap='Paired')
plt.colorbar(label='Survived')
plt.xlabel('Urutan data')
plt.ylabel('Sex (0=Female, 1=Male)')
plt.title('Visualisasi Survived berdasarkan Sex')
plt.savefig('plot_9.png', dpi=100, bbox_inches='tight')
plt.show()
import pandas as pd
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 100]

median_age = 29

color = '#ff392f'

plt.axvline(median_age, color=color, label="Age Median", linewidth=1)

plt.title("Ages of respondents")
plt.hist(ages, bins=bins, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Total Responmdets')

plt.tight_layout()


plt.show()

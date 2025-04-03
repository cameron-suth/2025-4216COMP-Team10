import matplotlib.pyplot as plt
import pandas as pd 

excel = pd.read_csv("Spotify_dataset.csv")
table_dance = excel.energy
table_popular = excel.tempo

fig, ax = plt.subplots(figsize=(20, 20))
ax.scatter(table_dance, table_popular)
# ax.plot([1,100], color='red')
plt.ylabel('Tempo')
plt.xlabel('Energy')
plt.show()
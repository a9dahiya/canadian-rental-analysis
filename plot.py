import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_csv('numeric_prices_data.csv')

waterloo_data = data['Waterloo']
toronto_data = data['Toronto']
vancouver_data = data['Vancouver']
ottawa_data = data['Ottawa']
montreal_data = data['Montreal']
calgary_data = data['Calgary']

fig, axs = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Rental Prices Distribution')

axs[0, 0].hist(waterloo_data, bins=20, alpha=0.5, color='blue')
axs[0, 0].set_title('Waterloo')
axs[0, 1].hist(toronto_data, bins=20, alpha=0.5, color='green')
axs[0, 1].set_title('Toronto')
axs[0, 2].hist(vancouver_data, bins=20, alpha=0.5, color='orange')
axs[0, 2].set_title('Vancouver')
axs[1, 0].hist(ottawa_data, bins=20, alpha=0.5, color='red')
axs[1, 0].set_title('Ottawa')
axs[1, 1].hist(montreal_data, bins=20, alpha=0.5, color='purple')
axs[1, 1].set_title('Montreal')
axs[1, 2].hist(calgary_data, bins=20, alpha=0.5, color='brown')
axs[1, 2].set_title('Calgary')

for ax in axs.flat:
    ax.set(xlabel='Price (CAD)', ylabel='Frequency')
    ax.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

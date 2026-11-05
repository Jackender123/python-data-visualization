import matplotlib.pyplot as plt
import numpy as np

months = np.arange(1, 13)
sales = np.array([120, 135, 150, 160, 190, 220,
                  210, 240, 280, 310, 330, 380])
temperature = np.array([25, 26, 28, 30, 32, 34,
                        33, 32, 31, 29, 27, 25])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(months, sales, marker='o', color='navy',
         label='Doanh so')
ax1.set_title('Doanh so theo thang')
ax1.set_xlabel('Thang')
ax1.set_ylabel('Doanh so (trieu VND)')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.scatter(temperature, sales, color='crimson',
            s=60, alpha=0.8)
ax2.set_title('Nhiet do va doanh so')
ax2.set_xlabel('Nhiet do (do C)')
ax2.set_ylabel('Doanh so (trieu VND)')
plt.tight_layout()
plt.show()
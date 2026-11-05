import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
scores = np.random.normal(loc=7.0, scale=1.5, size=200)
scores = np.append(scores, [1.0, 1.5, 10.0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.hist(scores, bins=15, color='teal',
         edgecolor='black', alpha=0.7)
ax1.set_title('Phan bo diem thi')
ax1.set_xlabel('Diem so')
ax1.set_ylabel('Tan suat')

ax2.boxplot(scores, vert=True, patch_artist=True,
            boxprops=dict(facecolor='gold'))
ax2.set_title('Boxplot diem thi')
ax2.set_ylabel('Diem so')

plt.tight_layout()
plt.show()
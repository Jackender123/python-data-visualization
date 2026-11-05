import numpy as np
import matplotlib.pyplot as plt

subjects = ['Lap trinh Python', 'Co so du lieu', 'Mang may tinh']
cntt1 = [8.5, 7.8, 8.2]
cntt2 = [8.0, 8.2, 7.5]

x = np.arange(len(subjects))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 4.5))

rects1 = ax.bar(x - width/2, cntt1, width, label='CNTT1', color='gold')
rects2 = ax.bar(x + width/2, cntt2, width, label='CNTT2', color='black')

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

ax.set_xticks(x, subjects)
ax.set_xlabel('Mon hoc')
ax.set_ylabel('Diem trung binh')
ax.set_title('So sanh diem trung binh giua CNTT1 va CNTT2')
ax.set_xticks(x)
ax.set_xticklabels(subjects)
ax.set_ylim(0, 10)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
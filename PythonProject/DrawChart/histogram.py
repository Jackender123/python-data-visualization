import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(0)
low_score = np.random.randint(0,41,140)
high_score = np.random.randint(41,101,60)
score = np.concatenate((low_score,high_score))
print(score)
df=pd.DataFrame({'score':score})
print(df)
mean = df['score'].mean()
median = df['score'].median()
std=df['score'].std()
plt.figure(figsize=(10,6))
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1.5, label=f'trung binh: {mean:.2f}')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1.5, label=f'trung vi: {median:.2f}')
n,bins,patches=plt.hist(df['score'],bins=10,color='skyblue',edgecolor='black')
plt.text(mean + 1, max(n) * 0.8, f'STD: {std:.2f}', fontsize=10, color='red', rotation=90)
for i in range(len(n)):
    midpoint = (bins[i] + bins[i + 1]) / 2
    plt.text(midpoint, n[i], int(n[i]), ha='center', va='bottom', fontsize=10, color='black')
plt.title('phan phoi deim thi cua hoc vien')
plt.xlabel("diem thi")
plt.ylabel("so luong hoc vien")
plt.legend()
plt.show()
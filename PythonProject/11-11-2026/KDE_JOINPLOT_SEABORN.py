import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Tao du lieu phan bo chuan 2 chieu
data = np.random.multivariate_normal([0, 0], [[1, 0.8], [0.8, 1]], size=2000)
df = pd.DataFrame(data, columns=['x', 'y'])

# 1. Ve bieu do mat do Kernel Density Estimation (KDE 2D)
sns.kdeplot(data=df, x='x', y='y', cmap='Blues', fill=True)

# 2. Ve bieu do Jointplot dang to ong Hexbin
with sns.axes_style('white'):
    g = sns.jointplot(x='x', y='y', data=df, kind='hex')                        
plt.show()
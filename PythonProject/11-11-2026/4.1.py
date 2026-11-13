import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
	'Mobile': pd.Series(dtype='float64'),
	'TV': pd.Series(dtype='float64'),
})

df.plot.bar(figsize=(10, 6), color=['#1f77b4', '#ff7f0e'])
plt.title('Sales Comparison of Mobile and TV', fontsize=16)
plt.tight_layout()
plt.show()
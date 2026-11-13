import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({"A": [1], "B": [2]})

df.plot.bar(stacked=True, figsize=(8, 4), rot=0)
plt.title("stacked sales volume")
plt.tight_layout()
plt.show()
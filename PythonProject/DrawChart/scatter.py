import matplotlib.pyplot as plt
import pandas as pd

companies = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
costs =[20,30,32,38,28,22,28,43,38,42]
revenues = [30,45,40,45,50,32,38,42,48,52]
df = pd.DataFrame({'company':companies,'cost':costs,'revenues':revenues})
print(df)
color=[]
for cost, revenue in zip(df['cost'], df['revenues']):
    if cost >= revenue:
        color.append('red')
    else:color.append('skyblue')
plt.scatter(df['cost'], df['revenues'], color=color)
plt.title("moi quan he giua ci phi va danh thu cua cac cong ty")
plt.xlabel("chi phi (trieu dong)")
plt.ylabel("doanh thu(trieu dong)")
for i,row in df.iterrows():
    plt.text(row['cost'], row['revenues'], row['company'], fontsize=12, ha='right', va='bottom')
plt.grid(True)
plt.show()
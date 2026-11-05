import matplotlib.pyplot as plt
import pandas as pd

data = {'month':['january','february','march','april','may'],'sales':[350,400,550,300,600]}
df = pd.DataFrame(data)

colors = ['skyblue'if value < 500 else 'orange' for  value in df['sales']]
plt.bar(df['month'],df['sales'],color = colors, edgecolor = 'black', linewidth=1.5)

for i, value in enumerate(df['sales']):
    plt.text(i,value+8,value,ha="center")
plt.title("bieu do cot doanh so ban hang theo thang")
plt.xlabel('thang')
plt.ylabel('doanh so ban hang theo thang')
plt.ylim(0,700)
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
data = {'month':['january','february','march','april','may'],'sales':[350,400,550,300,600]}
df = pd.DataFrame(data)
plt.plot(df['month'],df['sales'],label='doanh so ban hang',color='green',linewidth=2,linestyle='-.',marker='o',markerfacecolor='red',markersize=6)
plt.title("bieu dien doanh thu theo thang")
plt.xlabel("thang")
plt.ylabel("sales")
plt.legend(loc = 'upper left')
plt.show()
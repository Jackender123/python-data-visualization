import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
plt.show()
data = {'month':['january','february','march','april','may'],'sales':[350,400,550,300,600]}
df = pd.DataFrame(data)

print(df)
data={'x':[1,2,3,4,5],'y':[2,4,6,8,10]}
df = pd.DataFrame(data)
plt.plot(df['x'],df['y'],label='do thi truong')
plt.title('do thi truong don gian tu dataframe')
plt.xlabel("truc x")
plt.ylabel("truc y")
plt.legend()
plt.show()
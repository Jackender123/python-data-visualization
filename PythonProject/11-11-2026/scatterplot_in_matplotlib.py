import matplotlib.pyplot as plt

# Du Lieu Doanh so Ca phe da (X) va Nhiet do F (Y)
X = [100, 250, 400, 550, 700, 900]
Y = [15, 18, 20, 26, 31, 37]

plt.style.use('seaborn-v0_8-whitegrid')
plt.scatter(X, Y, s=60, c='red', marker='^')

plt.xlim(0, 1000)
plt.ylim(0, 100)
plt.title('Relationship Between Temperature and Iced Coffee Sales')
plt.xlabel('Sold Coffee (Cups)')
plt.ylabel('Temperature in Fahrenheit')
plt.show()
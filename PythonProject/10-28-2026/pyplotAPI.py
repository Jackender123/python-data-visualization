import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Cách 1: Pyplot API
plt.figure(figsize=(6, 3))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='--')
plt.title('Do thi Sin - Pyplot')
plt.xlabel('Bien X')
plt.ylabel('Bien Y')
plt.legend()
plt.grid(True)
plt.show()

# Cách 2: Object-Oriented API
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(x, y, label='sin(x)', color='red', linewidth=2)
ax.set_title('Do thi Sin - OOP')
ax.set_xlabel('Bien X')
ax.set_ylabel('Bien Y')
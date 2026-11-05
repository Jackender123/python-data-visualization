
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Khai báo dữ liệu
courses = ["Python", "Java", "Web", "AI"]
students = [20, 35, 25, 40]

# 2. Tạo biểu đồ 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# 3. Vị trí và kích thước các cột
x = [0, 1, 2, 3]
y = [0, 0, 0, 0]
z = [0, 0, 0, 0]

dx = [0.5, 0.5, 0.5, 0.5]
dy = [0.5, 0.5, 0.5, 0.5]
dz = students

# 4. Vẽ các cột 3D
ax.bar3d(x, y, z, dx, dy, dz, color="skyblue")

# 5. Đặt tên trục và tiêu đề
ax.set_title("Số lượng sinh viên đăng ký khóa học")
ax.set_xlabel("Khóa học")
ax.set_ylabel("Chiều sâu")
ax.set_zlabel("Số lượng sinh viên")

# 6. Hiển thị tên khóa học trên trục X
ax.set_xticks([0.25, 1.25, 2.25, 3.25])
ax.set_xticklabels(courses)

# 7. Hiển thị biểu đồ
plt.show()

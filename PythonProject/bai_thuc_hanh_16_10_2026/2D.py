
import matplotlib.pyplot as plt

# 1. Khai báo dữ liệu
courses = ["Python", "Java", "Web", "AI"]
students = [20, 35, 25, 40]

# 2. Vẽ biểu đồ cột 2D
plt.bar(courses, students, color="skyblue")

# 3. Đặt tiêu đề và tên các trục
plt.title("Số lượng sinh viên đăng ký khóa học")
plt.xlabel("Khóa học")
plt.ylabel("Số lượng sinh viên")

# 4. Hiển thị lưới
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 5. Hiển thị biểu đồ
plt.show()

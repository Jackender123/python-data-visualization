import numpy as np
#khoi tao mang 2D
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float64)
#kiem tra cac thuoc tinh bo nho cua mang
print("--THUOC TINH MANG ARR2D--")
print("Kich thuoc cua mang:", arr_2d.shape) # (3, 4) --> 3 dong, 4 cot
print("So chieu cua mang:", arr_2d.ndim) # 2
print("Kieu du lieu:", arr_2d.dtype) # float64
print("So phan tu:", arr_2d.size) # 12
print("Kich thuoc moi phan tu:", arr_2d.itemsize) # 8 bytes
#khoi tao mang bang cac ham dac biet
zero_matrix = np.zeros((3, 4)) # ma tran 3x4 toan so 0
identity_matrix = np.eye(3) # ma tran don vi 3x3
grid_seq = np.arange(10, 50, 10) # tao mang tu 10 den 50 voi buoc nhay la 10
linspace_seq = np.linspace(0, 1, 5) # tao mang tu 0 den 1 voi 5 phan tu
print("\n day linspace phant tu:", linspace_seq)
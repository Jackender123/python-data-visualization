import numpy as np
matrix = np.arange(1, 26).reshape(5, 5)
print ("Ma tran 5x5:\n", matrix)

sub_view = matrix[1:4, 1:4]
print("Ma tran con 3x3:\n", sub_view)

sub_view[:] = 999
print("Ma tran sau khi thay doi:\n", matrix)

matrix_clean = np.arange(1, 26).reshape(5, 5)
sub_copy = matrix_clean[1:4, 1:4].copy()
sub_copy[:] = -888
print("Ma tran sau khi thay doi (copy):\n", matrix_clean)
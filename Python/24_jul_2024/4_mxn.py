import numpy as np

# Define matrices of different dimensions
A = np.array([[1, 2, 3], [4, 5, 6]])  # A is a 2x3 matrix
B = np.array([[7, 8], [9, 10], [11, 12]])  # B is a 3x2 matrix

# Perform matrix multiplication
C = np.dot(A, B)
# Alternatively, you can use the @ operator for matrix multiplication in Python 3.5+
# C = A @ B

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of matrix multiplication A * B:")
print(C)

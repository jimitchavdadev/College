import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

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

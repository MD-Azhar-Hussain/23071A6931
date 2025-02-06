import numpy as np

# Creating two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
print("Addition:\n", A + B)

# Matrix subtraction
print("Subtraction:\n", A - B)

# Matrix multiplication
print("Multiplication:\n", np.dot(A, B))

# Transpose of A
print("Transpose of A:\n", A.T)

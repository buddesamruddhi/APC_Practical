
import numpy as np

# Create two 2D arrays
A = np.array([[10, 20],
              [30, 40]])

B = np.array([[2, 4],
              [5, 8]])

print("Array A:")
print(A)

print("Array B:")
print(B)

# Addition
print("Addition:")
print(A + B)

# Subtraction
print("Subtraction:")
print(A - B)

# Multiplication
print("Multiplication:")
print(A * B)

# Division
print("Division:")
print(A / B)

# Transpose
print("Transpose of Array A:")
print(A.T)

# Exponential
print("Exponential of Array A:")
print(np.exp(A))
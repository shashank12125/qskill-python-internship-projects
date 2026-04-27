import numpy as np

print("Enter values for Matrix A (2x2")
a11 = int(input("A[1][1]: "))
a12 = int(input("A[1][2]: "))
a21 = int(input("A[2][1]: "))
a22 = int(input("A[2][2]: "))

A = np.array([[a11,a12],
              [a21,a22]])

print("Enter values for Matrix B (2x2)")
b11 = int(input("B[1][1]: "))
b12 = int(input("B[1][2]: "))
b21 = int(input("B[2][1]: "))
b22 = int(input("B[2][2]: "))


B = np.array([[b11,b12],
              [b21,b22]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(A+B)

print("\nSubstraction:")
print(A-B)

print("\nMultiplication:")
print(np.dot(A,B))

print("\nTranspose:")
print(A.T)

print("\nDeterminant:")
print(np.linalg.det(A))
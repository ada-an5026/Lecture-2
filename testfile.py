import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])

m = np.array([[0, -5, 4], [-1, 2, -3]])
print(m[m < 0])

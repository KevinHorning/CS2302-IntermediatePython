#part2

import numpy as np

W = np.random.uniform(-1, 1, (3, 5))

v = np.ones((5, 3))
b = np.ones((3, 3))

results = np.zeros((3, 3))
for i in range(len(W)):
   for j in range(len(v[0])):
       for k in range(len(v)):
           results[i][j] += W[i][k] * v[k][j]
       results[i][j] += b[i][j]

np.add(np.matmul(W, v), b)

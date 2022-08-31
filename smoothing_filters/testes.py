import numpy as np

k = 3

horizontal_prewitt_kernel = np.ones((k,k))

for x in range(k):
  horizontal_prewitt_kernel [(x,0)] = -1
  
for y in range (k):
  horizontal_prewitt_kernel [(y,1)] = 0

print(horizontal_prewitt_kernel)

vertical_prewitt_kernel = np.ones((k,k))

for i in range (k):
  vertical_prewitt_kernel [(0,i)] = -1
for j in range (k):
  vertical_prewitt_kernel [(1,j)] = 0

print(vertical_prewitt_kernel)
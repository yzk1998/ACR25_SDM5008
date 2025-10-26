import numpy as np

A = np.array([[1,-2,4],[1,-1,1],[1,0,0],[1,1,1]])
B = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
b = np.array([[0],[0],[1],[0]])
print(f"A:{A}\nB:{B}\nb:{b}")

print(f"The second row of A: {A[1, :]}")
print(f"The third column of B: {B[:,2]}")

print(f"A+B: {A+B}")

print(f"B append to A:{np.append(A,B,axis=1)}")

#矩阵相乘
print(f"AT*B: {A.T@B}")

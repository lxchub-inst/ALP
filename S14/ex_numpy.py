import numpy as np

tb = np.zeros([2, 4])
tc = np.array([[1, 2, 3], [4, 5, 6]])

print(tb)

print("lignes :", tb.shape[0])
print("colonnes :", tb.shape[1])

print("lignes :", tb.shape)
print("colonnes :", tb.shape[0])

print(tc)

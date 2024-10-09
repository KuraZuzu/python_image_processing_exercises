import numpy as np

matrix = np.zeros((2, 3, 4))  # 3行3列のすべての要素がぜの配列を作成
print(matrix)

# 1から9までの値を持つ配列を作成
matrix2 = np.arange(1, 10).reshape((3, 3)) # 1から9までの数値を使って3x3の配列を作成
print(matrix2)

import numpy as np

# 2つの3x3の配列を作成
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 配列同士の足し算
matrix_sum = matrix_a + matrix_b
print(f"足し算の結果:\n{matrix_sum}\n")

# 配列同士の引き算
matrix_diff = matrix_a - matrix_b
print(f"引き算の結果:\n{matrix_diff}\n")

# 配列同士の掛け算
matrix_prod = matrix_a * matrix_b
print(f"掛け算の結果:\n{matrix_prod}\n")

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"元の配列:\n{matrix}\n")

# 2行3列目の要素にアクセスして変更
matrix[1, 2] = 99
print(f"2行3列目を変更:\n{matrix}\n")

# 1行目全体を変更
matrix[0, :] = [10, 20, 30]
print(f"1行目全体を変更:\n{matrix}\n")

# 1列目全体を変更
matrix[:, 0] = [90, 80, 70]
print(f"1列目全体を変更:\n{matrix}\n")

matrix_4x4 = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])
print(f"4x4の元の配列:\n{matrix_4x4}\n")

# 配列のスライシング： 2行目から3行目、、２列目から3列目を抽出
sub_matrix = matrix_4x4[1:3, 1:3]
print(f"スライシングした配列:\n{sub_matrix}\n")

matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"元の3x3配列:\n{matrix_3x3}\n")

# 5より大きい値をすべて0にする
matrix_3x3[matrix_3x3 > 5] = 0
print(f"5より多き値を0にした配列:\n{matrix_3x3}\n")
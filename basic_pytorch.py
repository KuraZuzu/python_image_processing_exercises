import torch

# 2x2のランダムなテンソルを作成
random_tensor = torch.rand((2, 2))  # 2行2列のランダムな数値を持つテンソルを作成
print(f"ランダムなテンソル:\n{random_tensor}\n")

# テンソルの要素にアクセス
print(f"テンソルの1行2列目の要素\n:{random_tensor[0, 1]}\n")

# すべての要素を1で初期化したテンソルを作成
ones_tensor = torch.ones((3, 3))
print(f"全ての要素を1で初期化したテンソル:\n{ones_tensor}\n")

# 2つのテンソルの足し算
tensor_a = torch.tensor([[1, 2], [3, 4]])
tensor_b = torch.tensor([[5, 6], [7, 8]])
tensor_sum = tensor_a + tensor_b
print(f"足し算をしたテンソル:\n{tensor_sum}\n")
# print(f":\n{}\n")
# print(f":\n{}\n")
# print(f":\n{}\n")
# print(f":\n{}\n")
# print(f":\n{}\n")

import numpy as np

# 1. 维度变换
x = np.arange(12).reshape(3,4)
print(x)
print(x.T)          # 转置，就像旋转表格：把行标题变成列标题
print(x.flatten())  # 展平一维

# 2. 数组合并
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])
print(np.vstack([m1,m2]))  # 上下合并
print(np.hstack([m1,m2]))  # 左右合并

# 3. 矩阵运算（AI最常用）
print('# 3. 矩阵运算（AI最常用）')
# 元素相乘
print(m1 * m2)


# 矩阵乘法 重点！
print(m1 @ m2)
print(np.dot(m1, m2))

# 4. 统计函数
print('# 4. 统计函数')
arr = np.array([[1,3,5],[2,4,6]])
print(np.mean(arr))   # 均值
print(np.sum(arr))    # 求和
print(np.max(arr))    # 最大值
print(np.argmax(arr)) # 最大值下标
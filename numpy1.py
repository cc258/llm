# 1. 导入
import numpy as np

# 查看numpy版本
print('numpy version：',np.__version__)

# 2. 创建数组
arr1 = np.array([1,2,3,4])          # 一维
arr2 = np.array([[1,2],[3,4]])      # 二维

# 3. 快速初始化
zero_arr = np.zeros((3,3))         # 全0
one_arr = np.ones((2,4))           # 全1

# 函数 empty 创建一个初始内容随机且依赖于内存状态的数组。
# 默认创建数组的 dtype 是 float64，
# 但可以通过关键字参数 dtype 来指定。
# empty_arr = np.empty((2,3), dtype=int)

range_arr = np.arange(0,10,2)      # 等差序列
line_arr = np.linspace(1,10,5)     # 均分5个数

# 4. 查看属性
print(arr2.shape)   # 形状
print(arr2.ndim)    # 维度
print(arr2.dtype)   # 数据类型

# 5. 切片索引
print(arr2[0,1])    # 取第一行第二个
print(arr2[:,0])    # 所有行第一列

# 6. 基础运算
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)    #数值相加
print(a * b)    #数值相乘
print(a ** 2)   #平方

# 7. 广播（重点）
print(a + 10)   #全部+10


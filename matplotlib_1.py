import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 中文显示必备（解决方框乱码）
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'Arial Unicode MS', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 折线图
x = [1,2,3,4,5]
y = [10,20,15,25,30]
plt.plot(x,y)   # 画线图
plt.title("基础折线图") # 标题
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()      # 弹出图片


# 柱状图
name = ["张三","李四","王五"]
score = [85,92,78]
plt.bar(name,score,color=["g","orange","b"])
plt.show()

# 散点图
x = [1,3,5,7,9]
y = [2,5,3,8,6]
plt.scatter(x,y,s=50,color="purple")
plt.show()

# 饼图
data = [30,25,20,25]
lab = ["吃饭","睡觉","学习","娱乐"]
plt.pie(data,labels=lab,autopct="%1.1f%%")
plt.show()


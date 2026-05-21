import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 中文显示必备（解决方框乱码）
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'Arial Unicode MS', 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('pandas_csv.csv')
# 直接调用绘图
df.plot(kind="bar",x="姓名",y="总分")
plt.show()
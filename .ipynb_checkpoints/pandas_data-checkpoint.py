import pandas as pd
data = {
    "姓名": ["小明", "小红", "小刚", "依依", "胖胖", "小曾"],
    "年龄": [20, 21, 19, 17, 16, 15],
    "成绩": [90, 85, 88, 99, 88, 77]
}

df = pd.DataFrame(data)
print(df)

print(df.head())      # 看前5行
print(df.tail())      # 看后5行
print(df.info())      # 查看数据类型、是否缺失
print(df.describe())  # 自动统计：均值、最大最小、标准差
print(df.shape)       # 查看行数、列数
print(df.columns)     # 查看列名


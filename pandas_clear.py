import numpy as np
import pandas as pd

# 读取
df = pd.read_csv("pandas_csv.csv",encoding="utf-8")
# pd.read_excel("a.xlsx")

# 保存
# df.to_csv("out.csv",index=False)
# df.to_excel("out.xlsx",index=False)

print(df.isnull())          # 判断缺失
print(df.isnull().sum())    # 统计缺失数量
print(df.dropna())          # 删除缺失行
# 填充
df["年龄"].fillna(np.random.randint(11, 14))

# 去重
df.duplicated()                 # 判断重复
df.drop_duplicates()            # 整行去重
df.drop_duplicates(subset=["姓名"]) # 指定列去重

# 类型转换
df["年龄"] = df["年龄"].astype(int)
df["总分"] = df["总分"].astype(float)

print('总分之和： ', df["总分"].sum())    # 求和
print('年龄平均： ', df["年龄"].mean())   # 均值
print('年龄最大： ', df["年龄"].max())    # 最大
print('年龄最小： ', df["年龄"].min())    # 最小
print('年龄个数： ', df["年龄"].count())  # 非空计数

# 单聚合
# df.groupby("姓名")["总分"].mean()
# 多聚合
# print(df.groupby("姓名")["总分"].agg(["mean","max","min"]))


# 上下拼接
# pd.concat([df1,df2],ignore_index=True)
# 左右匹配连接
# pd.merge(df1,df2,on="id",how="left")

# how="left" 左连接：保留左表全部数据
# how="right" 右连接：保留右表全部数据
# how="inner" 内连接：只保留两边都匹配到的数据
# how="outer" 全连接：保留两边所有数据

# 分组后结果是分组索引，转成普通数字行号
group_df = df.groupby("班级")["总分"].mean().reset_index()

# drop=True 直接删掉原来旧索引列
df_new = df.sort_values("总分").reset_index(drop=True)


df_new.to_csv("pandas_clear.csv",index=False)


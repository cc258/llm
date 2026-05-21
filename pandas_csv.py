import pandas as pd
import numpy as np

# 设置随机种子，保证结果可复现
np.random.seed(42)

# 生成学生数据
students = []
for i in range(1, 51):  # 生成50个学生
    student = {
        '学号': f'2024{1000 + i:03d}',
        '姓名': f'学生{i}',
        '班级': np.random.choice(['高一(1)班', '高一(2)班', '高一(3)班']),
        'age': np.random.randint(11, 14),
        '语文': np.random.randint(60, 100),
        '数学': np.random.randint(55, 100),
        '英语': np.random.randint(60, 98),
        '物理': np.random.randint(50, 96),
        '化学': np.random.randint(58, 97),
        '生物': np.random.randint(62, 95)
    }
    students.append(student)

# 创建DataFrame
df = pd.DataFrame(students)

# 添加总分和平均分
df['总分'] = df[['语文', '数学', '英语', '物理', '化学', '生物']].sum(axis=1)
df['平均分'] = (df['总分'] / 6).round(2)


# 显示前几行预览
print("\n前5行数据预览：")
print(df.head())

# 找出前总分10名学生
top10 = df.nlargest(10, '总分')[['学号' ,'姓名', '班级', '总分']]
print(top10)

# 计算各科平均分
print("各科平均分：")
print(df[['语文', '数学', '英语', '物理', '化学', '生物']].mean().round(2))

# 各班平均分对比
print("\n各班平均总分：")
print(df.groupby('班级')['总分'].mean().round(2))


# 新增
df["new_col"] = 1

# 重命名列
df.rename(columns={"age":"年龄"},inplace=True)

# 修改
df["年龄"] = df["年龄"] +1
# 删除列
df.drop("new_col",axis=1,inplace=True)
# 删除第二行
df.drop(1,axis=0,inplace=True)

# 条件筛选
print(df[df['总分'] > 500])
print(df[(df["年龄"]>11) & (df["年龄"]<14)])

print(df['年龄'].unique())        # 唯一值
print(df['年龄'].value_counts())  # 统计频次


# sort

df.sort_values("总分",ascending=True) # 升序
df.sort_values("总分",ascending=False)# 降序


df.to_csv('pandas_csv.csv', index=False, encoding='utf-8-sig')
print("CSV文件已生成：pandas_csv.csv")
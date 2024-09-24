import numpy as np
import pandas as pd


# CSV文件路径
csv_file_path = ['10MW-3f-2wdir-1_devc.csv','10MW-3f-2wdir-2_devc.csv','10MW-3f-2wdir-3_devc.csv','10MW-3f-2wdir-4_devc.csv','10MW-3f-2wdir-5_devc.csv']
# npy文件保存路径
npy_file_path = ['10MW-3f-2d-400x3x300x300-1.npy','10MW-3f-2d-400x3x300x300-2.npy','10MW-3f-2d-400x3x300x300-3.npy','10MW-3f-2d-400x3x300x300-4.npy', '10MW-3f-2d-400x3x300x300-5.npy']

# 对每一个csv文件进行清洗和过滤
for i in range(len(csv_file_path)):
    # 读取 CSV 文件
    df = pd.read_csv(csv_file_path[i])

    # 丢弃第一列数据
    df = df.drop(df.columns[0], axis=1)

    # 丢弃前两行数据
    df = df.iloc[2:]  # iloc用于基于行的切片

    # 将所有数据转换为浮点数类型
    df = df.astype(float)

    # 将 DataFrame 转换为 NumPy 数组
    data = df.values

    # 定义每个子列的长度
    sub_column_length = 300

    # 目前维度为400x27000(T*dnum)
    # 目标转换为(T,dtype,row,col)
    # 重塑数据为 (400, 3, 300, 300)
    reshaped_data = data.reshape(400, 3, sub_column_length, -1)

    print(reshaped_data.shape)

    # 保存为.npy文件
    np.save(npy_file_path[i], reshaped_data)

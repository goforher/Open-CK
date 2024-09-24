import numpy as np

# 读取 .npy 文件
file_path = '10MW-3f-2d-400x3x300x300-1.npy'
data = np.load(file_path)

# 输出数据维度
print(f"The dimensions of the data are: {data.shape}")

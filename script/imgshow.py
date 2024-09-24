import numpy as np
import matplotlib.pyplot as plt

# 假设 temperature_data 是一个 200x300x300 的 NumPy 数组，代表200秒内每300x300网格的温度变化
# 我们将为20s、50s、100s和200s的时间点创建热图

# 加载存储在.npy文件中的时间索引
temperature_data = np.load('300x300/300x300x300-5.npy')

print(temperature_data.shape)

# 设置要可视化的时间点索引
time_indices = [20, 50, 100, 200]

# 为每个时间点创建热图并保存
for i, time_index in enumerate(time_indices):
    # 选择特定时间点的温度数据
    temp_data = temperature_data[time_index-1, :, :]  # 时间索引需要减1，因为Python索引从0开始
    
    # 创建一个新的图形
    plt.figure()
    
    # 使用imshow创建热图
    plt.imshow(temp_data, interpolation='nearest', cmap='rainbow', 
               origin='lower', extent=[0, 300, 0, 300], clim=(20, 20.5))
    
    # 设置标题，例如 "Temperature Distribution at 20s"
    plt.title(f'Temperature Distribution at {time_index}s')
    
    # 隐藏坐标轴的刻度
    plt.xticks([])
    plt.yticks([])
    
    # 保存图形
    plt.savefig(f'temperature_distribution_{time_index}s.png', dpi=300, bbox_inches='tight')
    
    # 关闭图形以释放内存
    plt.close()
import pandas as pd
import numpy as np

# 读取confounds文件，通常是一个.tsv或者.csv文件
confounds = pd.read_csv('/Users/fan/Desktop/sub-HCD0008117_task-rest_desc-confounds_timeseries.csv')

import pandas as pd
import numpy as np

# 读取confounds文件
confounds_file = '/Users/fan/Desktop/sub-HCD0008117_task-rest_desc-confounds_timeseries.csv'
confounds = pd.read_csv(confounds_file)

# 提取头部运动参数，包括平移和旋转
movement_params = confounds[['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z']].values

# 计算FD
fd = np.zeros((movement_params.shape[0],))
for i in range(1, movement_params.shape[0]):
    # 计算相邻时间点的平移和旋转差异
    diff = movement_params[i] - movement_params[i-1]
    diff[3:] *= 50 * (np.pi / 180.0)  # 将旋转差异转换为弧度
    fd[i] = np.sum(np.abs(diff))

# 将FD值存储为一个新的列
confounds['fd'] = fd

# 保存包含FD值的confounds文件
confounds.to_csv('./output_file.csv', index=False)
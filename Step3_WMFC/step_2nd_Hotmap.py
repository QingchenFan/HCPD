import seaborn as sns
import pandas as pd
import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
mm = scio.loadmat('/Users/fan/Documents/Data/HCPData/HCPDtest/HCPDFC/sub-HCD0001305_FC2.mat')
mm = mm['data']

label = pd.read_csv('/Users/fan/Documents/Data/HCPData/JHU_ICBM/rICBM_DTI_81_WMPM_FMRIB58_68_2.csv', header=None)
newlabel = []
for i in range(0, 68):
    if i <10:
      newlabel.append(label[0][i][2:])
    else:
      newlabel.append(label[0][i][3:])

data = pd.DataFrame(np.round(mm, 2), columns=newlabel, index=newlabel)
print(data)

cx = sns.heatmap(data,
                 xticklabels=True, yticklabels=True, cmap='', annot=False,
                #cbar_kws ={'format': '%.1f','ticks': [-1.0, 0.0, 1.0]}
                )    # xticklabels/yticklabels x轴的titel  "Spectral"
cx.tick_params(labelsize=100, left=False, bottom=False)  # 控制去掉小刻度线
cx.set_xticklabels(newlabel, fontsize=4, font='Arial')# x轴上字体大小
cx.set_yticklabels(newlabel, fontsize=4, font='Arial')

cbar_3 = cx.collections[0].colorbar
cbar_3.ax.tick_params(labelsize=12, left=False, right=False)
#plt.savefig('FC.png', dpi=300, bbox_inches='tight')  #bbox_inches='tight' 字体展示完整

plt.show()
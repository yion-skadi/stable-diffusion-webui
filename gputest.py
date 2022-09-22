import torch

torch.device('cpu'), torch.device('cuda'), torch.device('cuda:1') # 分别是访问CPU，访问第0个GPU，访问第1个GPU。第 𝑖 块GPU（ 𝑖 从0开始）
print(torch.cuda.device_count()) # 查询可用gpu的数量。
print(torch.cuda.is_available())# 查询gpu是否可用。

import git
#==1.21.6
# -*- codeing = utf-8 -*-
# @Time : 2021-04-17 20:11
# @Author : 昆昆
# @File : text.py
# @Software : PyCharm

import torch

print(torch.__version__)
print('gpu:',torch.cuda.is_available())
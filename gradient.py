import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)#requires_grad允许跟踪关于其的计算
y = x + 2
print(y)
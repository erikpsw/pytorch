import torch
x = torch.empty(5, 3)
print(x)#不初始化
x = torch.zeros(5, 3, dtype=torch.long)
print(x)#全零填充
x = torch.rand(5, 3)
print(x)#随机初始化
x = torch.tensor([5.5, 3])
print(x)#带数值初始化
x = x.new_ones(5, 3, dtype=torch.float)
x = torch.randn_like(x, dtype=torch.float)
print(x)
# 相同大小
print(x.size())
y = torch.rand(5, 3)
print(x + y)#加法
print(torch.add(x, y))#使用方法
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)#赋值
y.add_(x)
print(y)#任何使张量会发生变化的操作都有一个前缀 '_'，此例中y会改变
x = torch.randn(4, 4)
y = x.view(16)#改变大小
print(x)
print(y)
print(x.size(),y.size())
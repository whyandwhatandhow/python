import numpy as np

# 生成随机数组矩阵，计算数组的最大值最小值和对数组排序

# 一维数组在1到100之间的10个数
a = np.random.randint(1, 101, 10, int)
# 一维数组在0-10
b = np.arange(1, 11)
# 一维数组，是01正态分布的10个随机数
c = np.random.randn(10)
# (1,4)的正态分布随机矩阵
d = np.random.randn(10) * 2 + 1

print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)

print('a的最大值',a.max())
print('a的最小值',a.min())
print('a的结构',a.shape)



a.sort()
print('排序后',a)






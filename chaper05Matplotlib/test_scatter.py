import matplotlib.pyplot as plt
import numpy as np

# 随机生成散点图

plt.figure(figsize=(10,6))
N=np.random.randint(10,100)
# scatter(x,y,s=半径，c=color,alpha=透明度)
plt.scatter(np.random.rand(N),np.random.rand(N),c='r',s=100,alpha=0.2)
plt.scatter(np.random.rand(N),np.random.rand(N),c='g',s=200,alpha=0.5)
plt.scatter(np.random.rand(N),np.random.rand(N),c='k',s=160,alpha=0.8)
plt.scatter(np.random.rand(N),np.random.rand(N),c='b',s=500,alpha=0.4)

plt.xlabel("x")
plt.ylabel("y")


plt.savefig("matplotlib_02",dpi=300,bbox_inches='tight')
plt.show()
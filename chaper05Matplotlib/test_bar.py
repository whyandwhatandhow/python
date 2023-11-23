import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# bar(x,height,width,bottom y轴起始位置,align对齐方式)

# 创建表格，用条形图显示

data_city={
    "beijing":[15600,17400],
    "shanghai":[12700,14800],
    "shangzhen":[4270,5200],
    "HongKong":[11300,12000],
    "guangzhou":[3620,4020]
}
bar_data=pd.DataFrame(data_city,index=[2016,2017])
print(bar_data)
x=np.arange(1,6)
plt.figure(figsize=(10,6))

bar1=plt.bar(x,bar_data.loc[2016],color='r',alpha=0.2,width=0.5,label='2016')
bar2=plt.bar(x+0.5,bar_data.loc[2017],color='b',alpha=0.2,width=0.5,label='2017')

plt.xlabel('Top5 city')
plt.ylabel("familyAmount")
plt.ylim([2500,20000])


#标注每座城市
plt.xticks(x,bar_data.columns)

# 标注哪个线是什么意思
plt.legend()


for bar_1 in bar1:
    height=bar_1.get_height()
    plt.text(bar_1.get_x()+bar_1.get_width()/2, height,'%d' % int(height),ha="center",va="bottom")

for bar_1 in bar2:
    height=bar_1.get_height()
    plt.text(bar_1.get_x()+bar_1.get_width()/2, height,'%d' % int(height),ha="center",va="bottom")

plt.savefig("matplotlib_03",dpi=300,bbox_inches="tight")

plt.show()


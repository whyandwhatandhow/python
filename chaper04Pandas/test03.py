# 统计在2017年7月11日，消费最低的10家银行，并且画出折线图

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

card_data=pd.read_excel('big_Num.xlsx','sheet2')

data_2017=card_data.loc[card_data['日期']=='2017/7/11  0:00:00']

# 消费金额后5的数据
bottom_5_data=data_2017['金额'].nsmallest(10)
print(bottom_5_data)

chart_bottom=data_2017.loc[bottom_5_data.index]
# print(chart_bottom)

plt.figure(figsize=(10,6))
x=np.arange(10)
bank_num=chart_bottom['card_id'].tolist()

plt.plot(x,chart_bottom['金额'],marker='x',label=bank_num)

#
# plt.annotate('Important Point', xy=(x, y), xytext=(x_text, y_text),
#              arrowprops=dict(facecolor='black', arrowstyle='->'))

for i, txt in enumerate(chart_bottom['金额']):
    plt.annotate(txt, (x[i], chart_bottom['金额'].iloc[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xticks(x,bank_num)
plt.xlabel('bank num')
plt.ylabel('economy')
plt.legend()
plt.show()

plt.savefig('bottom_10_2017',dpi=300,bbox_inches='tight')





# 根据给出的信用卡交易数据集，画出欺诈交易时间的折线图

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

creditcard_data=pd.read_csv('creditcard.csv')

# 诈骗交易
not_normal_transaction=creditcard_data[creditcard_data['Class']==1]

# 不同时间的交易
time_counts=not_normal_transaction['Time'].value_counts().sort_index()
print(time_counts)

plt.figure(figsize=(10,6))
plt.plot(time_counts.index,time_counts.values)
plt.xlabel("Transaction Time")
plt.ylabel("Frequency")
plt.savefig('not_normalTran',dpi=300,bbox_inches='tight')
plt.show()


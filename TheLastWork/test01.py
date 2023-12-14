# 根据给出的信用卡交易数据集，画出正常交易时间的柱状图;

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取csv文件
FraudDetection = pd.read_csv('creditcard.csv')
# 打印基本数据类型
FraudDetection.info()
# 描述表格基本值
FraudDetection.describe()

normal_transaction = FraudDetection[FraudDetection['Class'] == 0]

# 计算每个时间点的交易频率
time_counts = normal_transaction['Time'].value_counts().sort_index()
print(time_counts)

plt.figure(figsize=(10, 6))
plt.ylim(0, 10)
plt.bar(time_counts.index, time_counts.values, alpha=0.7)
plt.title('Histogram of Normal Transactions Time')
plt.xlabel('Transaction Time')
plt.ylabel('Frequency')
plt.savefig("normalTran", dpi=300, bbox_inches='tight')
plt.show()

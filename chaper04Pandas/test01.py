# 统计配发卡银行的消费金额，将消费最低的5家银行找出，并保存CSV文件，且画出折线图；

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv as cs

transRecord = pd.read_excel("D:\pyPrograming\FinancialDataMining\Data\ch04_case_transRecord.xlsx", 'Sheet1')
binNum = cs.reader(open("D:\pyPrograming\FinancialDataMining\Data\ch04_case_binNum.txt", 'r', encoding='UTF-8'))

# 将txt文件中的数据读出
card_data = []
for item in binNum:
    card_data.append(item)

# print(card_data) # 此时中间没有间隔

size = len(card_data[0])
card_id = []
card_name = []

n = 0
while n < size:
    if n % 2 == 0:
        card_id.append(card_data[0][n])
    if n % 2 == 1:
        card_name.append(card_data[0][n])
    n = n + 1

card = pd.DataFrame({'card_id': card_id, 'card_name': card_name})

# print(card)

# 保存为excel
# card.to_excel('big_Num.xlsx', index=False)

# 也是DataFrame
# print(transRecord)

transRecord['前六位'] = transRecord['卡号'].astype(str).str[:6]
card['前六位'] = card['card_id'].astype(str).str[:6]

merge_excel = pd.merge(transRecord, card, on='前六位', how='inner')


# with pd.ExcelWriter('big_Num.xlsx', engine='openpyxl', mode='a') as writer:
#     merge_excel.to_excel(writer, sheet_name='sheet2', index=False)

# 获取消费倒数5名
bottom_5 = merge_excel['金额'].nsmallest(5)

# 找出完整数据
bottom_data=merge_excel.loc[bottom_5.index]
print(bottom_data)

# 画出折线图
plt.figure(figsize=(10,6))
x=np.arange(5)
cardName=bottom_data['card_id'].tolist()

plt.plot(x,bottom_data['金额'],marker='o',label=cardName)

for i,text in enumerate(bottom_data['金额']):
    plt.annotate(text,(x[i],bottom_data['金额'].iloc[i]),xytext=(0,10), textcoords="offset points",ha='center')

plt.xlabel('bank')
plt.ylabel('finance')
plt.xticks(x,cardName)
plt.legend()
plt.show()
plt.savefig('bottom_five_city',dpi=300,bbox_inches='tight')



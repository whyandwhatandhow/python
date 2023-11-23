# 要求统计该时间段内刷卡交易金额排在前10位的银行名称。
import pandas as pd
import numpy as np
import csv as cs

# 读入xlsx文件和txt
transRecord = pd.read_excel("D:\pyPrograming\FinancialDataMining\Data\ch04_case_transRecord.xlsx", 'Sheet1')
binNum = cs.reader(open("D:\pyPrograming\FinancialDataMining\Data\ch04_case_binNum.txt", 'r', encoding='UTF-8'))

# 用来读取txt文件中的数据
carddata = []
code = []
card = []

# item is a list but binNum is an object
for item in binNum:
    carddata.append(item)
size = len(carddata[0])  # 5556

# 将奇数偶数分开来，并且存入DataFrame
count = 0
while (count < size):
    if count % 2 == 0:
        code.append(carddata[0][count])
    if count % 2 == 1:
        card.append(carddata[0][count])
    count = count + 1

code_card = pd.DataFrame({'code': code, 'codeinfo:': card})

print(code_card)


# 读取excel中的卡号与txt文件相匹配
transRecord['卡号前6位'] = transRecord['卡号'].astype(str).str[:6]
# print(transRecord['卡号前6位'][0])510529







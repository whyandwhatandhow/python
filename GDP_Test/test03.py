# # 3、	获取落后5个国家的近10年GDP数据；用柱状图表示。
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取数据
GDP_Data = pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\GDP_Data.xls", 'Data')

# 改变索引
GDP_Data.set_index('Country Code', inplace=True)

# 获取10年数据
gdp_decade = GDP_Data.loc[:, '2011':'2019']

# 求十年gdp平均值
gdp_decade['average'] = gdp_decade.mean(axis=1)

# 选后5个国家
bottom_5_countries = gdp_decade['average'].nsmallest(5)

# 获取这些国家在 gdp_decade 中的数据
selected_data = gdp_decade.loc[bottom_5_countries.index]
print(selected_data)
# 绘制柱状图
x = np.arange(10)
year = np.arange(2011, 2021)
plt.figure(figsize=(10, 6))

for i, country in enumerate(bottom_5_countries.index):
    plt.bar(x + 0.2 * i, selected_data.loc[country], width=0.2, alpha=0.7, label=country)

plt.xlabel('Year')
plt.ylabel('GDP')
plt.xticks(x + 0.2 * (len(bottom_5_countries) - 1) / 2, year)
plt.legend()
plt.savefig('last5',dpi=300,bbox_inches='tight')
plt.show()

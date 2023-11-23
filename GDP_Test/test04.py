# 对比分析我国与美国近20年GDP数据的变化，用折线图表示。

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

GDP_Data=pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\GDP_Data.xls",'Data')

china_gdp=GDP_Data.loc[GDP_Data['Country Name']=='中国','2002':'2022']
usa_gdp=GDP_Data.loc[GDP_Data['Country Name']=='美国','2002':'2022']

GDP_CO=pd.concat([china_gdp,usa_gdp])

print(GDP_CO)
x=np.arange(21)
year=np.arange(2002,2023)

plt.figure(figsize=(10,6))

for i,country in enumerate(GDP_CO.index):
    plt.bar(x+0.4*i,GDP_CO.loc[country],width=0.4,alpha=0.7,label=GDP_Data.loc[country,'Country Code'])

for i, country in enumerate(GDP_CO.index):
    plt.plot(x + 0.4 * i, GDP_CO.loc[country], marker='o', label=GDP_Data.loc[country, 'Country Code']+'Line')

plt.xticks(x+0.2*(len(GDP_CO)-1)/2,year)
plt.legend()
plt.xlabel("years")
plt.ylabel("GDP")

plt.savefig("comparePlot",dpi=300,bbox_inches='tight')
plt.show()
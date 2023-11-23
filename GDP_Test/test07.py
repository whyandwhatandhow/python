# 对比分析我国与俄罗斯近20年GDP的数据变化，并生成折线图。

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

GDP_Data=pd.read_excel('D:\pyPrograming\FinancialDataMining\DataMiningonFinance\PeopleGDP.xls','Data')

China_GDP=GDP_Data.loc[GDP_Data['CountryName']=='中国','2002':'2022']
ELS_GDP=GDP_Data.loc[GDP_Data['CountryName']=='白俄罗斯','2002':'2022']
Data_COCAT=pd.concat([China_GDP,ELS_GDP])
print(Data_COCAT)

x=np.arange(21)
year=np.arange(2002,2023)

plt.figure(figsize=(10,6))

for i,country in enumerate(Data_COCAT.index):
    mark= 'o' if i%2==0 else 'x'
    plt.plot(x,Data_COCAT.loc[country],marker=mark,label=GDP_Data.loc[country,'Country Code'])

plt.xlabel('year')
plt.ylabel('people Data')
plt.xticks(x,year)
plt.legend()
plt.grid()
plt.savefig('peopleData2',dpi=300,bbox_inches='tight')
plt.show()


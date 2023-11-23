# 我国与英国的数据对比
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

GDP_Data=pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\GDP_Data.xls",'Data')

china_gdp=GDP_Data.loc[GDP_Data['Country Name']=='中国','2002':'2022']
uk_gdp=GDP_Data.loc[GDP_Data['Country Name']=='英国','2002':'2022']

GDP_CO=pd.concat([china_gdp,uk_gdp])

print(GDP_CO)
x=np.arange(21)
year=np.arange(2002,2023)

plt.figure(figsize=(10,6))

for i,country in enumerate(GDP_CO.index):
    plt.bar(x+i*0.4,GDP_CO.loc[country],width=0.4,alpha=0.7,label=GDP_Data.loc[country,'Country Code'])
    # sns.barplot(x=x+i*0.4,y=GDP_CO.loc[country],label=GDP_Data.loc[country,'Country Code'])
    marker='o' if i%2==0 else 'x'
    plt.plot(x+i*0.4,GDP_CO.loc[country],marker=marker,label=GDP_Data.loc[country,'Country Code'])


plt.xticks(x,year)
plt.xlabel('year')
plt.ylabel('GDP')
plt.title('compare with english')
plt.legend()

plt.savefig("ChinaAndEnglish",dpi=300,bbox_inches='tight')
plt.show()
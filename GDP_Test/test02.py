# 	获取发展中国家近10年的GDP数据：中国、印度、巴西、俄罗斯，用柱状图表示
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1.读取文件
# 2.收集5国数据
# 3.合体
# 4.定义好坐标和图

country_data=pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\GDP_Data.xls",'Data')

china=country_data.loc[country_data['Country Name']=='中国','2010':'2020']
yindu=country_data.loc[country_data['Country Name']=='印度','2010':'2020']
baxi=country_data.loc[country_data['Country Name']=='巴西','2010':'2020']
nanFei=country_data.loc[country_data['Country Name']=='南非','2010':'2020']

total_gdp=pd.concat([china,yindu,baxi,nanFei])
print(total_gdp)

x=np.arange(11)
year=np.arange(2010,2021)

plt.figure(figsize=(10,6))

bar1=plt.bar(x-0.4,total_gdp.loc[40],color='r',alpha=0.2,width=0.2,label='china')
bar2=plt.bar(x-0.2,total_gdp.loc[109],color='b',alpha=0.2,width=0.2,label='yindu')
bar3=plt.bar(x,total_gdp.loc[29],color='k',alpha=0.2,width=0.2,label='baxi')
bar4=plt.bar(x+0.2,total_gdp.loc[263],color='yellow',alpha=0.5,width=0.2,label='nanFei')


plt.legend()
plt.xticks(x,year)
plt.title("Developing Country GDP")

plt.savefig('fourGDP',dpi=300,bbox_inches='tight')

plt.show()


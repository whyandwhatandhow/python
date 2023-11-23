# 	获取美国、英国、德国、瑞典、法国的近10年的GDP数据（2000-2020），用柱状图表示。
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

GDP_data=pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\GDP_Data.xls",'Data')
# print(GDP_data)

usa_gdp=GDP_data.loc[GDP_data['Country Name']=='美国','2010':"2020"]
uk_gdp=GDP_data.loc[GDP_data['Country Name']=='英国','2010':"2020"]
rui_gdp=GDP_data.loc[GDP_data['Country Name']=='瑞典','2010':"2020"]
fk_gdp=GDP_data.loc[GDP_data['Country Name']=='法国','2010':"2020"]
de_gdp=GDP_data.loc[GDP_data['Country Name']=='德国','2010':"2020"]
china_gdp=GDP_data.loc[GDP_data['Country Name']=='中国','2010':"2020"]

total_data=pd.concat([usa_gdp,uk_gdp,rui_gdp,fk_gdp,de_gdp,china_gdp])
print(total_data)

year=np.arange(2010,2021)
x=np.arange(11)


plt.figure(figsize=(12, 6))

bar1=plt.bar(x-0.2,total_data.loc[251],color='r',alpha=0.2,width=0.1,label='usa')
bar2=plt.bar(x-0.1,total_data.loc[81],color='b',alpha=0.5,width=0.1,label='uk')
bar3=plt.bar(x,total_data.loc[223],color='k',alpha=0.2,width=0.1,label='ruidian')
bar4=plt.bar(x+0.1,total_data.loc[77],color='yellow',alpha=0.2,width=0.1,label='faguo')
bar5=plt.bar(x+0.2,total_data.loc[55],color='blue',alpha=0.2,width=0.1,label='deguo')
bar6=plt.bar(x+0.3,total_data.loc[40],color='red',alpha=1,width=0.1,label='china')


plt.xlabel("years")
plt.ylabel("GDP")
plt.xticks(x,year)
plt.legend()
plt.title("Develop Country GDP")
# 太乱了
# for bar in bar1+bar2+bar3+bar4+bar5:
#     height=bar.get_height()
#     plt.text(x=bar.get_width()/2+bar.get_x(),y=height,s='%d' % int(height),va='bottom',ha='center')
plt.savefig('sixGDP',dpi=300,bbox_inches='tight')
plt.show()


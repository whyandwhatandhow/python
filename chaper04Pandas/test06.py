# 求配发银行卡2017年7月11日、2017年7月12日的消费金额。

import pandas as pd

card_data=pd.read_excel('big_Num.xlsx','sheet2')

date711=card_data.loc[card_data['日期']=='2017/7/11  0:00:00']
date712=card_data.loc[card_data['日期']=='2017/7/12  0:00:00']

twoDate=pd.concat([date711,date712])
print(twoDate)



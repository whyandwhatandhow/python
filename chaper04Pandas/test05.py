# 求购物最少的10张银行卡并且把消费地给显示出来
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

card_data=pd.read_excel("big_Num.xlsx",'sheet2')

brought=card_data.loc[card_data['分类']=='购物']

bottom_5=brought['金额'].nsmallest(10)
ten_card=card_data.loc[bottom_5.index]

print(ten_card)

with pd.ExcelWriter('big_Num.xlsx',engine='openpyxl',mode='a') as writer:
    ten_card.to_excel(writer,sheet_name='sheet4',index=False)

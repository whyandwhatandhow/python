# 查找一张银行卡在多地消费的记录，并且保存为excel文件。
import pandas as pd

card_data=pd.read_excel('big_Num.xlsx','sheet2')

group=card_data.groupby(['card_id','城市']).size().reset_index(name='消费次数')

print(card_data.groupby(['card_id','城市']))
duplicates=group[group['消费次数']>1]

print(duplicates)

with pd.ExcelWriter('big_Num.xlsx',engine='openpyxl',mode='a') as writer:
    duplicates.to_excel(writer,sheet_name='sheet3',index=False)





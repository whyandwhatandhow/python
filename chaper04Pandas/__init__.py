import pandas as pd

# 构造一维数组,每个元素都可以加索引,是通过list
series=pd.Series([100,'gduf',"Guangzhou"],index=['mark','University','City'])
print(series)


# 通过字典构造二维
dataFrame={'name':['python','java','cpp'],'score':[90,90,0],'year':[2017,2018,2019]}
print('字典为',dataFrame)

s3=pd.DataFrame(dataFrame)
print(s3)
print("s3.index",s3.index)
print("s3.shape",s3.shape)




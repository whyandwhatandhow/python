import numpy as np
import pandas as pd

# 创建一个二维数组
df_1 = pd.DataFrame({'A': 1.,
                     'B': pd.Timestamp('20231103'),
                     'C': pd.Series(1, index=range(4), dtype=float),
                     'D': np.array([3, 4, 5, 6], dtype=int),
                     'E': pd.Categorical(["test", "train", "test", "train"]),
                     'F': 'ymd'
                     }, index=[1, 2, 3, 4])

print("df_1")
print(df_1)

print("各个类型\n",df_1.dtypes)


print("df_1的描述")
print(df_1.describe())

print("按d排序")
print(df_1.sort_values(by='D',))


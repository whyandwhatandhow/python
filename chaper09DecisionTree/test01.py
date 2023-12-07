# 1、	根据第10章的促销记录信息，随机生成5个客户信息，利用决策树算法，给出5个客户的推销策略。

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


bank_data=pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\Ch10_NaiveBayes\ch10_bankMarketing_info.xlsx",'Sheet1')

# 随机5个客户
random_5custom=bank_data.sample(n=5)
print("随机5位客户数据:\n",random_5custom)


# 选择特征和目标变量
features = ['工龄', '岗位性质', '教育程度', '婚姻状态']
target = '销售结果'

# 处理数据，对类别变量进行编码
label_encoder = LabelEncoder()
for feature in features:
    random_5custom[feature] = label_encoder.fit_transform(random_5custom[feature])

# 构建决策树模型
model = DecisionTreeClassifier(random_state=42)
model.fit(bank_data[features], bank_data[target])

# 进行预测
predictions = model.predict(random_5custom[features])

# 输出预测结果
result_df = pd.DataFrame({'客户ID': random_5custom['客户ID'], '推销策略': predictions})
print("\n预测结果:\n", result_df)


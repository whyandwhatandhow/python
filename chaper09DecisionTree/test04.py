import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# 读取原有数据
existing_data = pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\Ch10_NaiveBayes\ch10_bankMarketing_info.xlsx", 'Sheet1')

# 选择特征和目标变量
features = ['工龄', '岗位性质', '教育程度', '婚姻状态']
target = '销售结果'

# 处理数据，对类别变量进行编码
existing_data[features] = existing_data[features].apply(lambda x: pd.Categorical(x).codes)

# 构建决策树模型
X_train = existing_data[features]
y_train = existing_data[target]
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 读取新生成的数据
new_data = pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\Ch10_NaiveBayes\ch10_bankMarketing_info_updated.xlsx")

# 处理数据，对类别变量进行编码
new_data[features] = new_data[features].apply(lambda x: pd.Categorical(x).codes)

# 进行预测
predictions = model.predict(new_data[features])

# 输出预测结果
result_df = pd.DataFrame({'推销策略': predictions})
print("\n预测结果:\n", result_df)

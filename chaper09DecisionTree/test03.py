import pandas as pd
from sklearn.naive_bayes import GaussianNB


# 读取原有数据
existing_data = pd.read_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\Ch10_NaiveBayes\ch10_bankMarketing_info.xlsx", 'Sheet1')

# 随机选择100个客户作为训练集
train_data = existing_data.sample(n=100, random_state=42)

# 选择特征和目标变量
features = ['工龄', '岗位性质', '教育程度', '婚姻状态']
target = '销售结果'

# 处理数据，对类别变量进行编码
train_data[features] = train_data[features].apply(lambda x: pd.Categorical(x).codes)

# 构建朴素贝叶斯模型
X_train = train_data[features]
y_train = train_data[target]
model = GaussianNB()
model.fit(X_train, y_train)

# 生成额外的1000个客户记录
additional_data = pd.DataFrame({
    '工龄': [2] * 1000,  # 用示例值替代，请根据实际情况调整
    '岗位性质': [3] * 1000,
    '教育程度': [2] * 1000,
    '婚姻状态': [1] * 1000
})

# 处理数据，对类别变量进行编码
additional_data[features] = additional_data[features].apply(lambda x: pd.Categorical(x).codes)

# 利用训练好的模型进行预测
predictions = model.predict(additional_data[features])

# 输出预测结果
result_df = pd.DataFrame({'推销策略': predictions})
print("\n预测结果:\n", result_df)

# 将预测结果插入到原有数据中
additional_data['销售结果'] = predictions

# 将新数据插入到Excel文件中
updated_data = pd.concat([existing_data, additional_data], ignore_index=True)
updated_data.to_excel("D:\pyPrograming\FinancialDataMining\DataMiningonFinance\Ch10_NaiveBayes\ch10_bankMarketing_info_updated.xlsx", index=False)
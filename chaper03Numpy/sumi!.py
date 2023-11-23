# i的阶乘求和

import numpy as np

def calculate_sum_of_factorials_np(i):
    nums = np.arange(1, i+1)
    factorials = np.cumprod(nums)  # 计算阶乘并累积
    result_sum = np.sum(factorials)
    return result_sum

# 在这里设置你想要的 i 值
i_value = 5

result_sum = calculate_sum_of_factorials_np(i_value)
print(f"The sum of factorials up to {i_value} is: {result_sum}")

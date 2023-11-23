import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 高中25.15 大专37.24 本科33。36 硕士3.68 其他0.57

plt.figure(figsize=(10, 6))

edu = {'HighSchool': 0.2515,
       'Others': 0.057,
       'Junior College': 0.3724,
       'Bachelor': 0.3336,
       'Master': 0.0368
       }

colors = ['r', 'g', 'b', 'gray', 'yellow']

edu_frame = pd.DataFrame(edu, index=['学历', '失业率'])
print(edu_frame)
plt.pie(x=edu.values(), explode=[0, 0, 0.1, 0, 0], colors=colors, labels=edu.keys(), radius=1.5,autopct='%.1f%%')
plt.axis('equal')  # 整圆


plt.savefig("matplotlib_04")
plt.show()

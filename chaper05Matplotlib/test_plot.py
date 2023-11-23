import matplotlib.pyplot as plt
import numpy as np

# 在直角坐标系绘制y=2*x+1 的图像 x[100,201)

x=np.arange(100,201)
y=2*x+1
plt.figure(figsize=(10,6))

plt.xlim(100,201)

# .plot绘制线性图
plt.plot(x,y)


# 设置标注
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.grid()

# 保存图片
# dpi: 表示每英寸点数（Dots Per Inch），即图像的分辨率。默认值为 100。较高的 dpi 值会产生更高分辨率的图像，但文件大小也会更大。300 dpi 是打印品质的推荐值。
#
# bbox_inches: 用于控制保存图像时图形的边界框（Bounding Box）。参数值可以是字符串或者 Bbox 类型对象，用于指定裁剪图形周围空白区域的方式。
#
# 'tight': 选择了最小限度的边界框，使得图形被保存时，空白边缘被裁剪掉。
# 这两个参数一起使用时，bbox_inches='tight' 会在保存图像时剪裁掉多余的空白区域，并且 dpi=300 指定了图像的分辨率为每英寸 300 点，从而保证图像在打印时有较高的质量。
plt.savefig("matplotlib_01.png",dpi=300,bbox_inches='tight')

plt.show()



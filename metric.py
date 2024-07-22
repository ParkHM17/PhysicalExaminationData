import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# my_font = FontProperties(fname=r"C:\windows\fonts\SimHei.ttf", size=12)


# 示例数据
times = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05']
values = [10, 15, 7, 10, 12]
# 创建折线图
plt.figure(figsize=(10, 6))  # 设置图表大小
plt.plot(times, values, marker='o')  # 绘制折线图，并设置数据点标记
# 添加数据标签
for i, (time, value) in enumerate(zip(times, values)):
    plt.text(i, value, f'{value}', ha='center', va='bottom')  # 在数据点上方添加标签
# 设置图表标题和坐标轴标签
plt.title('指标随时间变化图')
plt.xlabel('时间')
plt.ylabel('指标值')

plt.axhline(3)
plt.text(0, 3, "标准值上限=3")

# 显示图表
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# 创建角度数组（0到2π）
theta = np.linspace(0, 2*np.pi, 100)

# 计算单位圆上的点
x = np.cos(theta)
y = np.sin(theta)

# 创建图形和坐标轴
plt.figure(figsize=(8, 8))
ax = plt.subplot(111)

# 绘制单位圆
ax.plot(x, y, 'b-', linewidth=2, label='unit circle')

# 设置坐标轴
ax.axhline(y=0, color='k', linewidth=0.5)  # 水平轴
ax.axvline(x=0, color='k', linewidth=0.5)  # 垂直轴
ax.set_aspect('equal')  # 确保比例相等，圆看起来是正圆

# 添加网格
ax.grid(True, linestyle='--', alpha=0.7)

# 设置坐标轴范围
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# 添加标签和标题
ax.set_title('unit circle', fontsize=14)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)

InnerP_theta = np.linspace(0, 2*np.pi, 11)

InnerP_x = np.cos(InnerP_theta)
InnerP_y = np.sin(InnerP_theta)

ax.plot(InnerP_x, InnerP_y, '+', markersize=15)

# 显示图形
plt.tight_layout()
plt.show()
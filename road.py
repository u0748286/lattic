from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# 第一条曲线的参数
a1, b1, c1, d1, e1 = 1, -2, 3, -4, 5

# 定义L1
def L1(x):
    return a1*x**4 + b1*x**3 + c1*x**2 + d1*x + e1

# 在x=100处的条件值
y_100 = L1(100)
dy_100 = 4*a1*100**3 + 3*b1*100**2 + 2*c1*100 + d1
d2y_100 = 6*4*a1*100**2 + 3*2*b1*100 + 2*c1
d3y_100 = 6*4*3*a1*100 + 3*2*b1

# 设定第二条曲线在x=200处的目标y值小于y_100，确保L2递减
y_target = y_100 - 10  # 为了简化，这里直接选择了一个小于y_100的值

# 解方程组来找到第二条曲线L2的参数
def equations(vars):
    a2, b2, c2, d2, e2 = vars
    eq1 = a2*100**4 + b2*100**3 + c2*100**2 + d2*100 + e2 - y_100  # 在x=100处的条件
    eq2 = 4*a2*100**3 + 3*b2*100**2 + 2*c2*100 + d2 - dy_100      # 一阶导数条件
    eq3 = 6*4*a2*100**2 + 3*2*b2*100 + 2*c2 - d2y_100            # 二阶导数条件
    eq4 = 6*4*3*a2*100 + 3*2*b2 - d3y_100                        # 三阶导数条件
    eq5 = a2*200**4 + b2*200**3 + c2*200**2 + d2*200 + e2 - y_target  # 在x=200的目标y值
    return (eq1, eq2, eq3, eq4, eq5)

# 初始猜测值
initial_guess = [a1, 0, 0, 0, y_100]  # 假设初始猜测，保留a1为初始a2值

# 求解方程组
solution = fsolve(equations, initial_guess)
a2, b2, c2, d2, e2 = solution

# 定义L2
def L2(x):
    return a2*x**4 + b2*x**3 + c2*x**2 + d2*x + e2

# 生成绘图数据
x_range1 = np.linspace(0, 100, 500)
y_range1 = L1(x_range1)
x_range2 = np.linspace(100, 200, 500)
y_range2 = L2(x_range2)

# 绘制两条样条曲线
plt.figure(figsize=(12, 6))
plt.plot(x_range1, y_range1, label='Spline L1')
plt.plot(x_range2, y_range2, label='Spline L2', linestyle='--')
plt.legend()
plt.title("Two Joined Spline Curves with Decreasing L2")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

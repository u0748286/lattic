from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# ��һ�����ߵĲ���
a1, b1, c1, d1, e1 = 1, -2, 3, -4, 5

# ����L1
def L1(x):
    return a1*x**4 + b1*x**3 + c1*x**2 + d1*x + e1

# ��x=100��������ֵ
y_100 = L1(100)
dy_100 = 4*a1*100**3 + 3*b1*100**2 + 2*c1*100 + d1
d2y_100 = 6*4*a1*100**2 + 3*2*b1*100 + 2*c1
d3y_100 = 6*4*3*a1*100 + 3*2*b1

# �趨�ڶ���������x=200����Ŀ��yֵС��y_100��ȷ��L2�ݼ�
y_target = y_100 - 10  # Ϊ�˼򻯣�����ֱ��ѡ����һ��С��y_100��ֵ

# �ⷽ�������ҵ��ڶ�������L2�Ĳ���
def equations(vars):
    a2, b2, c2, d2, e2 = vars
    eq1 = a2*100**4 + b2*100**3 + c2*100**2 + d2*100 + e2 - y_100  # ��x=100��������
    eq2 = 4*a2*100**3 + 3*b2*100**2 + 2*c2*100 + d2 - dy_100      # һ�׵�������
    eq3 = 6*4*a2*100**2 + 3*2*b2*100 + 2*c2 - d2y_100            # ���׵�������
    eq4 = 6*4*3*a2*100 + 3*2*b2 - d3y_100                        # ���׵�������
    eq5 = a2*200**4 + b2*200**3 + c2*200**2 + d2*200 + e2 - y_target  # ��x=200��Ŀ��yֵ
    return (eq1, eq2, eq3, eq4, eq5)

# ��ʼ�²�ֵ
initial_guess = [a1, 0, 0, 0, y_100]  # �����ʼ�²⣬����a1Ϊ��ʼa2ֵ

# ��ⷽ����
solution = fsolve(equations, initial_guess)
a2, b2, c2, d2, e2 = solution

# ����L2
def L2(x):
    return a2*x**4 + b2*x**3 + c2*x**2 + d2*x + e2

# ���ɻ�ͼ����
x_range1 = np.linspace(0, 100, 500)
y_range1 = L1(x_range1)
x_range2 = np.linspace(100, 200, 500)
y_range2 = L2(x_range2)

# ����������������
plt.figure(figsize=(12, 6))
plt.plot(x_range1, y_range1, label='Spline L1')
plt.plot(x_range2, y_range2, label='Spline L2', linestyle='--')
plt.legend()
plt.title("Two Joined Spline Curves with Decreasing L2")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

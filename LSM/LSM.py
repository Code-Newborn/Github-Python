"""
Reference    :
ReferenceAuthor:
Year         :
             :
Descripttion :
version      :
Author       : ChenZhao
Date         : 2023-08-08 09:39:53
LastEditors  : ChenZhao
LastEditTime : 2023-08-08 10:06:05
"""
import matplotlib.pyplot as plt
import numpy as np


def Show_Circle(x=0, y=0, r=2):
    theta = np.arange(0, 2 * np.pi, 0.01)
    x = x + r * np.cos(theta)
    y = y + r * np.sin(theta)
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y)
    axes.axis("equal")
    plt.show()


def Fit_Circle(x=None, y=None):
    if x is None:
        x = [1, 0, -1, 0]
    if y is None:
        y = [0, 1, 0, -1]

    Y = []
    R = []

    for i in range(len(x)):
        R.append([-x[i], -y[i], -1])
        Y.append(np.square(x[i]) + np.square(y[i]))

    R = np.mat(R)
    Y = np.mat(Y).T
    A = np.dot(np.dot(np.linalg.inv(np.dot(R.T, R)), R.T), Y)
    A = np.array(A, dtype="float32").flatten()
    return (
        round(-(A[0] / 2), 2),
        round(-(A[1] / 2), 2),
        round(np.sqrt((np.square(A[0]) + np.square(A[1]))-4*A[2])/2, 2),
    )


if __name__ == "__main__":
    # 原数据
    a = [-51.7, -51.7, 29.8, 32.3]
    b = [-7.4, 25.6, 25.6, 1.8]
    x, y, r = Fit_Circle(x=a, y=b)  # 圆拟合
    print("拟合圆心坐标: (%.2f, %.2f) \t半径: %.2f"%(x,y,r))

    # 绘制圆数据
    theta = np.arange(0, 2 * np.pi, 0.01)
    X = x + r * np.cos(theta)
    Y = y + r * np.sin(theta)

    fig, ax = plt.subplots()  # 创建图像

    # 绘图属性设置
    ax.axis("equal")  # 坐标轴等长
    plt.xlim(-100, 100)  #
    plt.ylim(100, -100)  # Y轴反转

    plt.scatter(a, b, marker="o", c="green", s=50, alpha=1)  # 原数据点绘制
    plt.plot(X, Y)  # 绘制拟合圆
    plt.plot(x, y, marker="*", markersize=10, markeredgecolor="red", markerfacecolor="red")
    plt.axhline(0.0, color="black", linestyle="--")
    plt.axvline(0.0, color="black", linestyle="--")

    plt.show()  # 显示图像
    # Show_Circle(X, Y, R)

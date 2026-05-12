import numpy as np
from scipy.optimize import leastsq
def func(x,p):
    A,k,theta = p
    return A*np.sin(2*np.pi*k*x+theta)
def deviation(p,y,x):
    return y-func(x,p)
x = np.linspace(0,-2*np.pi,100)
A,k,theta = 10, 0.34, np.pi/6
y0 = func(x, [A,k,theta])
y1=y0+2*np.random.randn(len(x))
p0 = [7,0.2,0]
l = leastsq(deviation,p0,(y1,x))
print("真实参数:", [A, k, theta])
print("拟合参数:", l[0])
import matplotlib.pyplot as plt
import pylab as pl
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
pl.plot(x, y0, marker='+', label=u"真实数据")
pl.plot(x, y1, label=u"噪声数据")
pl.plot(x, func(x, l[0]), marker='.',label=u"拟合数据")
pl.legend()
pl.show()

# v0.1
# v0.1
# master
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.misc import derivative
from scipy.special import factorial


def round_up_to_odd(f):
    return f // 2 * 2 + 1


def function(x):
    return np.sin(x) / np.exp(x)

l = float(input())


def funccos(x, k):
    return function(x) * np.cos(np.pi * k * x / l)


def funcsin(k):
    def myfunc(x):
        return function(x) * np.sin(np.pi * k * x / l)
    return myfunc


def T(n):
    def tfunc(x):
        a0 = (1 / l) * integrate.quad(function, -l, l)[0]
        ak = list((1 / l) * integrate.quad(funccos, -l, l, args=k)[0] for k in range(1, n))
        bk = list((1 / l) * integrate.quad(funcsin(k), -l, l)[0] for k in range(1, n))
        #print("bk ", bk)
        asum = 0.0
        bsum = 0.0
        for k in range(1, n):
            asum += ak[k - 1] * np.cos(np.pi * k * x / l)
            bsum += bk[k - 1] * np.sin(np.pi * k * x / l)
        return a0 / 2 + asum + bsum
    return tfunc


def P(n):
    def pfunc(x):
        a0 = function(0.0)
        ak = list((derivative(function, 0.0, dx=0.2, n=k, order=round_up_to_odd(k+1))) for k in range(1, n))
        asum = 0.0
        for k in range(1, n):
            asum += ak[k - 1] / factorial(k) * x**k
        return a0 + asum
    return pfunc

x_steps = np.arange(-l, l, 2 * 1 / 1000)
y_steps = function(x_steps)
plt.figure()
plt.ion()
plt.rc('lines', linewidth=4)
plt.plot(x_steps, y_steps, color='r')
plt.title("Fourier")
plt.grid(True)
#  plt.show()
#print(integrate.quad(function, -l, l))
for n in range(2, 100):
    x_steps = np.linspace(-l, l, num=n, endpoint=True)
    y_steps = T(n)(x_steps)
    print("n ", n)
    print("x_steps ", x_steps)
    print("y_steps ", y_steps)
    plt.rc('lines', linewidth=1)
    plt.plot(x_steps, y_steps)
    plt.pause(0.2)

plt.show(block=True)

x_steps = np.arange(-l, l, 2 * 1 / 1000)
y_steps = function(x_steps)
plt.figure()
plt.ion()
plt.rc('lines', linewidth=4)
plt.plot(x_steps, y_steps, color='r')
plt.title("Fourier")
plt.grid(True)
#  plt.show()
#print(integrate.quad(function, -l, l))
for n in range(2, 100):
    x_steps = np.linspace(-l, l, num=n, endpoint=True)
    y_steps = P(n)(x_steps)
    print("n ", n)
    print("x_steps ", x_steps)
    print("y_steps ", y_steps)
    plt.rc('lines', linewidth=1)
    plt.plot(x_steps, y_steps)
    plt.pause(0.2)

plt.show(block=True)

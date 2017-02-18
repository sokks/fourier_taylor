import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.misc import derivative
from scipy.special import factorial


def function(x):
    return np.sin(x) / np.exp(x)
    #return np.exp(x)
    #return np.cos(x)


def round_up_to_odd(f):
    return f // 2 * 2 + 1

#  l = float(input())
l = 3
taylor_center = 1.0


def funccos(x, k):
    return function(x) * np.cos(np.pi * k * x / l)


def funcsin(x, k):
    return function(x) * np.sin(np.pi * k * x / l)


def T(n):
    def tfunc(x):
        a0 = (1 / l) * integrate.quad(function, -l, l)[0]
        ak = list((1 / l) * integrate.quad(funccos, -l, l, args=k)[0] for k in range(1, n))
        bk = list((1 / l) * integrate.quad(funcsin, -l, l, args=k)[0] for k in range(1, n))
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
        a0 = function(taylor_center)
        ak = list((derivative(function, 1.0, dx=0.01, n=k, order=2*k+1)) for k in range(1, n))
        asum = 0.0
        for k in range(1, n):
            asum += ak[k - 1] / factorial(k) * (x - taylor_center)**k
        return a0 + asum
    return pfunc

x_steps_test = np.linspace(-l, l, num=1000, endpoint=True)
y_steps_test = function(x_steps_test)
x_steps_test_taylor = np.arange(-l, l, 2 * 1 / 1000)
y_steps_test_taylor = function(x_steps_test_taylor)
plt.figure()
plt.ion()
plt.title("Fourier & Taylor")
plt.grid(True)
#print(integrate.quad(function, -l, l))

for n in range(2, 50):
    x_steps = np.linspace(-l, l, num=100, endpoint=True)
    y_steps = T(n)(x_steps)
    x_steps_taylor = np.linspace(-l, l, num=100, endpoint=True)
    # if n == 1:
    #     y_steps_taylor = function(taylor_center)
    # else:
    y_steps_taylor = P(n)(x_steps_taylor)
    plt.clf()
    plt.rc('lines', linewidth=4)
    plt.plot(x_steps_test, y_steps_test, color='r')
    plt.rc('lines', linewidth=2)
    plt.plot(x_steps, y_steps, color='b')
    plt.plot(x_steps_taylor, y_steps_taylor, color='g')
    plt.pause(0.2)
plt.show(block=True)



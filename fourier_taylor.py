import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.misc import derivative
from scipy.special import factorial

l = 3.0
taylor_center = 0.0

def function(x):
    #return np.sin(x) / np.exp(x)
    return np.exp(np.sin(x))
    #return np.exp(x)
    #return np.cos(x)


def funccos(x, k):
    return function(x) * np.cos(np.pi * k * x / l)


def funcsin(x, k):
    return function(x) * np.sin(np.pi * k * x / l)


def fourier(n):
    def tfunc(x):
        a0 = (1 / l) * integrate.quad(function, -l, l)[0]
        ak = [(1 / l) * integrate.quad(funccos, -l, l, args=(k))[0] for k in range(1, n)]
        bk = [(1 / l) * integrate.quad(funcsin, -l, l, args=(k))[0] for k in range(1, n)]
        asum = 0.0
        bsum = 0.0
        for k in range(1, n):
            asum += ak[k - 1] * np.cos(np.pi * k * x / l)
            bsum += bk[k - 1] * np.sin(np.pi * k * x / l)
        return a0 / 2 + asum + bsum
    return tfunc


x_steps_test = np.linspace(-l, l, num=1000, endpoint=True)
x_steps_fourier = np.linspace(-l, l, num=100, endpoint=True)
x_steps_taylor = np.linspace(-l, l, num=100, endpoint=True)
y_steps_test = function(x_steps_test)

plt.figure()
plt.ion()
plt.title("Fourier & Taylor")
plt.grid(True)

t0

n = 0
a0 = (1 / l) * integrate.quad(function, -l, l)[0] / 2
y_steps_fourier = np.linspace(a0, a0, num=len(x_steps_fourier))
plt.clf()
plt.rc('lines', linewidth=4)
plt.plot(x_steps_test, y_steps_test, color='r')
plt.rc('lines', linewidth=2)
plt.plot(x_steps_fourier, y_steps_fourier, color='b')
plt.pause(0.2)

n += 1
funccos1 = lambda x: function(x) * np.cos(np.pi * x / l)
funcsin1 = lambda x: function(x) * np.sin(np.pi * x / l)
a1 = (1 / l) * integrate.quad(funccos1, -l, l)[0]
b1 = (1 / l) * integrate.quad(funcsin1, -l, l)[0]
f1 = lambda x: a0 + a1 * np.cos(np.pi * x / l) + b1 * np.sin(np.pi * x / l)
y_steps_fourier = f1(x_steps_fourier)
plt.clf()
plt.rc('lines', linewidth=4)
plt.plot(x_steps_test, y_steps_test, color='r')
plt.rc('lines', linewidth=2)
plt.plot(x_steps_fourier, y_steps_fourier, color='b')
plt.pause(0.2)


for n in range(2, 25):
    y_steps_fourier = fourier(n)(x_steps_fourier)
    plt.clf()
    plt.rc('lines', linewidth=4)
    plt.plot(x_steps_test, y_steps_test, color='r')
    plt.rc('lines', linewidth=2)
    plt.plot(x_steps_fourier, y_steps_fourier, color='b')
    plt.pause(0.2)
plt.show(block=True)

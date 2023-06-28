import numpy as np
import matplotlib.pyplot as plt

dotn_4 = 417.5
dotn_5 = 465.7
dotn_10 = 259.5
dotn_11 = 211.3

comp_ee_4 = [0.48500,0.00500,0.51000,0.1e-8,0.1e-8,0.1e-8,0.1e-8,0.1e-8]
comp_ee_5 = [0.43263,0.00444,0.45264,0.00116,0.07256,0.00885,0.01964,0.00808]
comp_ee_10 = [0.1e-8,0.1e-8,0.1e-8,0.00222,0.13704,0.01669,0.47269,0.37136]

def PHI(y_5,F_5,x_10,F_10):
    phi = (y_5*F_5)/(x_10*F_10)
    return phi

phis = []
for i in range(len(comp_ee_5)):
    phis.append(PHI(comp_ee_5[i],dotn_5,comp_ee_10[i],dotn_10))


def dx_dt(x, t, phi, xi_10, dotn_10, yi_4, dotn_4, dotn_11):
    dx_dt = ((1-phi)*(xi_10*dotn_10 + yi_4*dotn_4) - x*dotn_11)/dotn_11
    return dx_dt


def euler(f, x0, y0, h, n, params):
    x = [x0]
    y = [y0]
    for i in range(n):
        y.append(y[-1] + h * f(x[-1], y[-1], *params))
        x.append(x[-1] + h)
    return x, y

params =  (phis[7], comp_ee_10[7], dotn_10, comp_ee_4[7], dotn_4, dotn_11)


# Parametros para solucion Euler
t0 = 0
x0 = 0.43828

# Define paso de solucion y tiempo
h = 0.00001
# t = np.arange(t0, 1+h, h)

x, y = euler(dx_dt, x0, t0, h, 100000, params)

# y = np.zeros(len(t))
# y[0] = x0
# for i in range(len(t)):
#     y[i] = y[i-1] + h*dx_dt(y[i-1],t[i-1],*params)

plt.plot(x,y)
plt.show()
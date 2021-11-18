# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:55:07 2020

@author: Dhanush Wagle
"""

import numpy as np
import matplotlib.pyplot as plt

def compute(a, b):
    x = np.zeros(5)
    y = np.zeros(5)
    e = 0
    for i in range(0, 5, 1):
        x[i] = i
        y[i] = a*x[i] + b
        e = e + ((a*x[i] + b - y[i])**2)
    return x, y, e

def user():
    
    a = int(input('Enter the value of a: '))
    b = int(input('Enter the value of b: '))
    x, y, e = compute(a, b)
    print('The error value is: ', e)
    
    plt.close('all')
    plt.figure(1)
    
    plt.plot(x, y, 'g')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(('function',))
    
    plt.show()

def fun_obj(params):
    a = params[0]
    b = params[1]
    x_obs_array, y_obs_array, e = compute(a, b)
    y_pred_array = a*x_array + b
    e_array = y_obs_array - y_pred_array
    sspe = sum(e_array*e_array)
    return sspe


x_array = np.array([0, 1, 2, 3, 4])
y_array = np.array([0.5, 2.0, 1.0, 1.5, 7.5])
    

N_resol_param = 100

a_lb = -10
a_ub = 10
a_array = np.linspace(a_lb, a_ub, N_resol_param)

b_lb = -10
b_ub = 10
b_array = np.linspace(b_lb, b_ub, N_resol_param)

sspe_min = np.inf
a_opt = 0
b_opt = 0


for a in a_array:

    for b in b_array:

        # Calc of objective function:
        params = np.array([a, b])
        sspe = fun_obj(params)  

        # Improvement of solution:
        if (sspe < sspe_min):
            sspe_min = sspe
            a_opt = a
            b_opt = b


print(f'a_opt = {a_opt:.3e}')
print(f'b_opt = {b_opt:.3e}')
print(f'sspe_min = {sspe_min:.3e}')

user()
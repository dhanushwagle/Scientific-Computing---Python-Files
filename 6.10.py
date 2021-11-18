# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:06:29 2020

@author: Dhanush Wagle
"""

from numpy import linspace, zeros, log
from trapezoidal import trapezoidal
import matplotlib.pyplot as plt

def adaptive_integration(f, a, b, eps):
    n_limit = 1000000 # Just a choice (used to avoid inf loop)
    n = 2
    integral_n = trapezoidal(f, a, b, n)
    integral_2n = trapezoidal(f, a, b, 2*n)
    diff = abs(integral_2n - integral_n)
    while (diff > eps) and (n < n_limit):
        integral_n = trapezoidal(f, a, b, n)
        integral_2n = trapezoidal(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        n *= 2
    # Now we check if acceptable n was found or not
    if diff <= eps: # Success
        print('The integral computes to: {:.7g}'.format(integral_2n))
        return n
    else:
        return -n # Return negative n to tell "not found"
    
def application():
    def f(x):
        return x**x
    eps = 1E-10
    a = 0.0 + 0.01;
    b = 4.0
    n = adaptive_integration(f, a, b, eps)
    n_limit = 1000000
    if n > 0:
        print('Sufficient n is: {:d}'.format(n))
    else:
        print('No n was found in {:d} iterations'.format(n_limit))
    # Plotting
    eps = linspace(1E-1,10E-10,10)
    n_t = zeros(len(eps))
    for i in range(len(n_t)):
        n_t[i] = adaptive_integration(f, a, b, eps[i])
    plt.plot(log(eps),n_t,'r-')
    plt.xlabel('log(eps)')
    plt.show()
if __name__ == '__main__':
    application()



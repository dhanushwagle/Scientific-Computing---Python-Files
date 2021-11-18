# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:41:42 2020

@author: Dhanush Wagle
"""

import sys
import math as m

def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/dfdx(x)
        except ZeroDivisionError:
            print('Error! - derivative zero for x = ', x)
            sys.exit(1)     # Abort with error

        f_value = f(x)
        iteration_counter = iteration_counter + 1

    # Here, either a solution is found, or too many iterations
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

def fixed_point_iteration(f, x0, eps, N):
    # Re-writing f(x)=0 to x = g(x)
    def g(x):
        return (m.exp(-x) - x**3) / 2
    
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > eps

    if flag==1:
        print('\nRoot found from Fixed Point Iteration method')
    else:
        print('\nNo Convergence')
    return x1, step
        
if __name__ == '__main__':
    def f(x):
        return (x**3 + 2*x - m.exp(-x) )
    
    def dfdx(x):
        return (3*x**2 + 2 + m.exp(-x))
    
    solution1, no_iterations1 = Newton(f, dfdx, x=1, eps=1.0e-6)
    solution2, no_iterations2 = fixed_point_iteration(f, x0=1, eps=1.0e-6, N=100)
    
    if no_iterations2 > 0:    # Solution found
        print('Number of iterations: {:d}'.format(1+2*no_iterations2))
        print('A solution is: {:f}'.format(solution2))
    else:
        print('Solution not found from Newtons Method')
    
    if no_iterations1 > 0:    # Solution found
        print('\nNewtons Method')
        print('Number of iterations: {:d}'.format(1+2*no_iterations1))
        print('A solution is: {:f}'.format(solution1))
    else:
        print('Solution not found from Fixed Point Iteration Method')
    
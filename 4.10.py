# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:08:05 2020

@author: Dhanush Wagle
"""

import numpy as np

def interpolate(t_input):
    y = np.zeros(5)
    n = int(input("Enter number of elements in y: "))
    print('Enter the elements one at a time')
    
    for i in range(0, n):
        a = float(input('num: '))
        y.append(a)
    
    t_start = int(input("Enter start time: "))
    t_stop = int(input("Enter end time: "))
    t = np.linspace(t_start, t_stop, n)
    
    for i in range(t_start, t_stop+1, 1):
        if t_input > i and t_input < (i+1):
            y_output = ((y[i+1] - y[i])/(t[i+1] - t[i]) * (t_input - t[i])) + y[i]
    
    return y_output

def find_y():
        
        t = float(input("Enter the time value to be interpolated: "))
        if(t>0):
            y = interpolate(t)
            print('the interpolated value of y is', y)
        else:
            print('the given time is negative')
        
if __name__ == '__main__':
    find_y()
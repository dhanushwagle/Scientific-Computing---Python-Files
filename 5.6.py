# -*- coding: utf-8 -*-

"""
Created on Sat Sep 26 12:58:17 2020

@author: Dhanush Wagle
"""
import matplotlib.pyplot as plt

def polyarea(x, y):
    n = len(x)
    A = 0
    for i in range(n):
        A = abs(A + 0.5*(x[i-1]*y[i]-y[i-1]*x[i]))
    return A

# Checking for triangle with base of unit 6 and height of unit 3; area should be 9 
x = [0, 6, 3]
y = [0, 0, 3]
area = polyarea(x, y)
print('area of polygon is: ', area)

# adding first element just for plotting the polygon
x1 = [0, 6, 3, 0]
y1 = [0, 0, 3, 0]

# plotting the points on graph
plt.close('all')
plt.figure(1)
    
plt.plot(x1, y1, 'g-')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('polygon',))
    
plt.show()
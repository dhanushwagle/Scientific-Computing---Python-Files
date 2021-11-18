# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:03:00 2020

@author: Dhanush Wagle
"""
import numpy as np
import matplotlib.pyplot as plt

# Time unit: 1 h
beta = 10./(40*8*24)
gamma = 3./(15*24)
dt = 0.1 # 6 min
D = 30 # Simulate for D days
N_t = int(D*24/dt) # Corresponding no of time steps

t = np.linspace(0, N_t*dt, N_t+1)
S = np.zeros(N_t+1)
I = np.zeros(N_t+1)
R = np.zeros(N_t+1)

S_H = np.zeros(N_t+1)
I_H = np.zeros(N_t+1)
R_H = np.zeros(N_t+1)

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

S_H[0] = 50
I_H[0] = 1
R_H[0] = 0

# Step equations forward in time
for n in range(N_t):
    #Forward Euler's Method
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n]

    #Heunn's Method
    S_star = S_H[n] - dt*beta*S_H[n]*I_H[n]
    I_star = I_H[n] + dt*beta*S_H[n]*I_H[n] - dt*gamma*I_H[n]
    R_star = R_H[n] + dt*gamma*I_H[n]
    
    S_H[n+1] = S_H[n] - 0.5*dt*beta*(S_H[n] + S_star)*(I_H[n] + I_star)
    I_H[n+1] = I_H[n] + 0.5*dt*beta*(S_H[n] + S_star)*(I_H[n] + I_star) - 0.5*dt*gamma*(I_H[n] + I_star)
    R_H[n+1] = R_H[n] + 0.5*dt*gamma*(I_H[n] + I_star)

# plot for forward euler's method
plt.close('all')
plt.figure(1)
plt.plot(t, S, t, I, t, R, t, S_H, t, I_H, t, R_H)
plt.legend(labels=('S', 'I', 'R', 'S_H', 'I_H', 'R_H'))
plt.xlabel('hours')
plt.show()
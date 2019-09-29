#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python program to implement Runge Kutta method 
''' this is range kutta method
I have created a function and called it for different
 value of h and n, function = y'=-64y
 in error caluclation I have calculated error at each iteration point''' 

import numpy as np
import matplotlib.pyplot as plt
import math

def ran_kutta(x0,y0,xn,h,n):
    x = np.linspace(x0, xn, n)

    y = np.zeros([n])
    y_exact = np.zeros([n])
    err=np.zeros([n])
    
    y_exact[0] = 1
    err[0] = 0
    y[0] = 1
    
    for i in range(1,n):
            k1 = (-64)*(h)* (y[i-1]) 
            k2 = (-64)*(h)* (y[i-1] + 0.5 * k1) 
            k3 =  (-64)*(h)* (y[i-1] + 0.5 * k2) 
            k4 =  (-64)*(h)*(y[i-1] + k3) 

            y[i] = y[i-1] + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
            y_exact[i] = math.exp(-64*i)
            err[i] = (y[i]-y_exact[i])


    for i in range (1,n):
        print(x[i], y[i])
        print('error is: ')
        print(err[i])

    plt.plot(x,y)
    plt.xlabel("x-axis, value of x")
    plt.ylabel('y-axis, value of y')
    plt.title('Approximation using forward euler method')
    plt.show()
    
ran_kutta(0,1,5,0.01,500)
print('this is for h=0.1: \n')
ran_kutta(0,1,5,0.1,50)
print('this is for h=0.2: \n')
ran_kutta(0,1,5,0.2,25)
print('this is for h=0.5: \n')
ran_kutta(0,1,5,0.5,10)


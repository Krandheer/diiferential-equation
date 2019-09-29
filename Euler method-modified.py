#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''this is modified euler method
 I have created a function and called it for different
 value of h and n, function = y'=-64y '''

import numpy as np
import matplotlib.pyplot as plt
import math

def mod_euler(x0,y0,xn,h,n):
    x = np.linspace(x0, xn, n)
    
    y = np.zeros([n])
    err = np.zeros([n])
    y_exact = np.zeros([n])
    y_exact[0] = 1
    err[0] = 0
    y[0] = 1
    
    for i in range(1,n):
        temp = y[i-1] + h*(-64*y[i-1])
        #modifies y for modified euler method below line
        y[i] = y[i-1] +0.5*h*(-64*y[i-1]-64*temp)
        y_exact[i] = math.exp(-64*i)
        err[i] = (y[i]-y_exact[i])

    for i in range (1,n):
        print(x[i], y[i])
        print('error is:')
        print(err[i])

    plt.plot(x,y)
    plt.xlabel("x-axis, value of x")
    plt.ylabel('y-axis, value of y')
    plt.title('Approximation using forward euler method')
    plt.show()
    
mod_euler(0,1,5,0.01,500)
print('this is for h=0.1:\n')
mod_euler(0,1,5,0.1,50)
print('this is for h=0.2:\n')
mod_euler(0,1,5,0.2,25)
print('this is for h=0.5:\n')
mod_euler(0,1,5,0.5,10)


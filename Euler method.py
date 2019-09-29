#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''this is euler method
I have created a function and called it for different
 value of h and n, function = y'=-64y
 while calculating error I have calculated it at each iteration point
 (hence local error)'''

import numpy as np
import matplotlib.pyplot as plt
import math

def euler(x0,y0,xn,h,n):
    x = np.linspace(x0, xn, n)

    y = np.zeros([n])
    y_exact = np.zeros([n])
    err = np.zeros([n])
    
    y_exact[0] = 1
    err[0] = 0
    y[0] = 1
    
    for i in range(1,n):
        y[i] = y[i-1] + h*(-64*y[i-1])
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

euler(0,1,5,0.01,500)
print('this is for h=0.1:\n')
euler(0,1,5,0.1,50)
print('this is for h=0.2:\n')
euler(0,1,5,0.2,25)
print('this is for h=0.5:\n')
euler(0,1,5,0.5,10)


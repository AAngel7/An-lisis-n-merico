#!/usr/bin/env python
# coding: utf-8

# In[105]:


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math


# In[118]:


def heron(x,y):
    return (1/2)*(x+y/x)
def h(n,y):
    fx=np.empty(n+1)
    fx[0]=1
    for i in range(1,n+1):
        fx[i]=heron(fx[i-1],y)
        print(fx[i])
def eh(n,y):
    fx=np.empty(n+1)
    fx[0]=1
    er=np.empty(n+1)
    for i in range(1,n+1):
        er[i]=heron(fx[i-1],y)-math.sqrt(y)
        print(er[i])


# In[121]:


h(5,49)
print("Error")
eh(5,49)


# In[123]:


a=np.arange(n+1)
plt.semilogy(a,fx,color='y',label='a')
plt.semilogy(a,er,color='r',label='e')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





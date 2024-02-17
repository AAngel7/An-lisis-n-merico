#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
x=sy.symbols('x')
f=7*sy.cos(x)+2*sy.sin(x)+sy.exp(x)
g=sy.series(f,x,0,3)
print(f)
print(g)


# In[9]:


orden=g.getO()
gx=g.removeO()
print(orden)
print(gx)
ffunc=sy.lambdify(x,f)
gfunc=sy.lambdify(x,g.removeO())
print(ffunc)
print(gfunc)
ffunc(3)


# In[10]:


x=np.linspace(0,5)
yf=ffunc(x)
yg=gfunc(x)
plt.plot(x,yf,color='r')
plt.plot(x,yg,color='b')
yer=np.abs(yf-yg)
yord=x**3
plt.plot(x,yer,color='y')
plt.plot(x,yord)
plt.legend(['yf','yg','error','orden'])
plt.show()


# In[ ]:





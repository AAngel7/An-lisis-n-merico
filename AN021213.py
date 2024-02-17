#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
x=sy.symbols('x')
f=7*sy.cos(x)+2*sy.sin(x)+sy.exp(x)
g=sy.series(f,x,0,3)
print(f)
print(g)


# In[3]:


orden=g.getO()
gx=g.removeO()
print(orden)
print(gx)
ffunc=sy.lambdify(x,f)
gfunc=sy.lambdify(x,g.removeO())
print(ffunc)
print(gfunc)
ffunc(3)


# In[4]:


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


# In[5]:


#Error de convergencia
n=50
y=np.empty(n+1)
y[0]=1
y[1]=1/5
for i in range(2,n+1):
    y[i]=(16/5)*y[i-1] - (3/5)*y[i-2]
x=np.arange(n+1)
plt.semilogy(x,y,'rx',label='a')
plt.semilogy(x,(1/5)**x,'bp',label='b')
plt.grid(True)
plt.show()


# In[ ]:





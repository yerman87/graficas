
# coding: utf-8

# In[52]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# $$f(x)=e^{x}-e{x}-e^{-x}/e^{x}+e^{-x}$$

# In[45]:

x = np.linspace(-5, 5)
e = np.e


# In[46]:

def f(x, e):
    return ((e ** x)-(e ** -x))/((e ** x)+(e ** -x))


# In[47]:

plt.plot(x, f(x, e), "x",color="y")
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.grid(True)


# In[36]:

def escalon(x, c):
    return np.piecewise(x, [x < 0, x > 0], [0, 1])


# In[37]:

c = np.linspace(0, 5) 
x = np.linspace(-5, 5)


# In[38]:

plt.plot(x, escalon(x,c),"--",color="g")
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.grid(True)


# In[39]:

sigma=0.01
x = np.linspace(-5,5)
e = np.e
pi = np.pi


# In[40]:

x = np.linspace(-200, 200)


# In[15]:

def f(x):
    return (1/np.sqrt(2*pi*sigma**2))*(e**-((x**2)/2*(sigma**2)))


# In[16]:

plt.plot(x, f(x),"h",color="r")
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.grid(true)


# In[50]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[55]:

x=np.arange(-3,3)
y=4*x+1 
plt.plot(x,y,)


# In[ ]:




# In[ ]:




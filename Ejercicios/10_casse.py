#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt


# Calculo PI con el metodo del círculo

# In[ ]:


def pi_circ(num_puntos=10000):
    puntos = np.random.random((num_puntos, 2))
    distancias = np.sum(puntos ** 2, axis=1)
    num_puntos_circulo = np.sum(distancias <= 1)
    pi = 4 * num_puntos_circulo / num_puntos
    return pi


# Calculo PI con el metodo de valor medio

# In[ ]:


def pi_med(num_puntos=10000):
    puntos = np.random.random(num_puntos)
    f_puntos = np.sqrt(1 - puntos**2)
    pi = 4 * f_puntos.mean()
    return pi


# In[ ]:


x=np.logspace(2,4.2,20,dtype="int")


# In[ ]:


pc=np.array([pi_circ(y) for y in x])
pm=np.array([pi_med(y) for y in x])    


# In[ ]:


plt.plot(x,pc,"-", label="Método de cociente de áreas", linewidth=2)
plt.plot(x,pc,"hb")
plt.plot(x,pm, "--r", label= "Método de valor medio",linewidth=3)
plt.plot(x,pm,"or")
plt.legend(loc="best", title="Referencias")
plt.xscale('log')
plt.ylim((2,4))
plt.xlabel("Nro de muestras")
plt.ylabel("Estimación de Pi")
plt.show()


# In[ ]:


hpc=np.array([pi_circ(15000) for i in np.arange(1000)])
hpm=np.array([pi_med(15000) for i in np.arange(1000)])   


# In[ ]:


plt.hist(hpm, density=True, bins=30,color="red", label="Método de valor medio")
plt.hist(hpc, density=True, bins=30, color="blue", label="Método de cociente de áreas",alpha=0.8)
plt.axvline(x=np.mean(hpm), color='black')
plt.legend(loc="best", title="Referencias")
plt.xlim(3.0,3.2)

# Calcular la desviación estándar y superponer una función Gaussiana
std_m = np.std(hpm)
mu_m = np.mean(hpm)
x = np.linspace(mu_m - 4*std_m, mu_m + 4*std_m, 1000)
y = 1/(np.sqrt(2*np.pi)*std_m) * np.exp(-(x - mu_m)**2/(2*std_m**2))
plt.plot(x, y, color='black',linewidth=2,alpha=0.9)

std_c = np.std(hpc)
mu_c = np.mean(hpc)
x = np.linspace(mu_c - 4*std_c, mu_c + 4*std_c, 1000)
y = 1/(np.sqrt(2*np.pi)*std_c) * np.exp(-(x - mu_c)**2/(2*std_c**2))
plt.plot(x, y, color='black',linewidth=2,alpha=0.9)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# Es el ejercicio 8.5

# In[1]:


import numpy as np
from math import sqrt
get_ipython().run_line_magic('matplotlib', 'tk')
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# In[2]:


def caida(h0=10,v0=0,grav=-1,puntos=20):
    """
    Modificación del ejercicio 8
    Ingresando altura inicial, velocidad inicial, valor de gravedad y cantidad de puntos,
    devuelve tiempo, altura y velocidad en formato de array de Numpy.
    No guarda los datos generados en archivo
    
    """
    ttot=(-v0-sqrt(v0*v0-2*grav*h0))/grav
    t=np.linspace(0,ttot,puntos)
    h=h0+v0*t+0.5*grav*t**2
    v=v0+grav*t
    #datos=np.column_stack((t,v,h))
    #header="t, v(t), h(t))"
    #archivo=f"caida_{v0}_{h0}.dat"
    #np.savetxt(archivo, datos, delimiter=',', header=header)
    return t,h,v


# In[3]:


#defino parámetros iniciales de la funcion caida
h0, v0, g,pts=100,0, -9.8, 50

#Genero los datos para graficar
t, h, v=caida(h0,v0,g,pts)
mh=max(h)

#Para generar cola fantasma de 3 puntos
for i in range(5):
    t=np.append(t,t[-1])
    h=np.append(h,h[-1])
    v=np.append(v,v[-1])
    pts+=1
    
#Completo los valores en X que va a tomar la gráfica, en este caso todos cero
x=np.zeros(pts)

#funcion de actualizacion
def actualizar(pos,x, t,v, h, line):
    if pos>5:
        line.set_data(x[pos-5:pos],h[pos-5:pos])
    else:
        line.set_data(x[pos],h[pos])
    #Actualizo los valores mostrados de tiempo, velocidad y altura
    t1.set_text("Tiempo:     {:.3f}\nVelocidad: {:.3f}\nAltura:       {:.1f}".format(t[pos],v[pos],h[pos]))
    return line,t1

#creo figura,ejes y la gráfica
fig, ax = plt.subplots()
punto,= plt.plot([], [], 'ro')

#Delimito ejes
ax.set_xlim(-1, 1)
ax.set_ylim(0, mh)
#Título y texto con valores
ax.set_title('Animación de caida libre')
t1= ax.text(0.2,mh*.8,"cargando...")

#Creo animacion
animacion=animation.FuncAnimation(fig, actualizar, pts, fargs=(x,t,v,h, punto), interval=50, blit=True)
plt.show()


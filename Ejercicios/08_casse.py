# %%
import numpy as np               

# %%
def trapz(x,y):
    total=0.0
    h=(x[-1]-x[0])/(len(x)-1)
        
    for i in y:
        total+=2*i
    total-=(y[0]+y[-1])
    resultado=h*0.5*total

    return resultado


# %%
def trapzf(f, a, b, npts=100):
    total=0.0
    h=(b-a)/(npts)
    
    for i in range(npts+1):
        fx=f(a+i*h)
        total+=2*f(a+i*h)
    total-=(f(a)+f(b))
    resultado=h*0.5*total

    return resultado

# %%
def funcion(t):
    return 1/(np.log(t))

# %%
npts=np.array([10,20,30,40,50,60])

# %%
for x in npts:
    print(f'Para {x} puntos, la integral log de Euler entre 2 y 10 es: {trapzf(funcion,2,10,x)}')



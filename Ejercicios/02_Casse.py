#!/usr/bin/env python
# coding: utf-8

# Presentación

# In[2]:


print("Juan Ignacio Casse","\n")
print("Clase 2", "\n")


# In[3]:


s = '''Aquí me pongo a cantar
Al compás de la vigüela,
Que el hombre que lo desvela
Una pena estraordinaria
Como la ave solitaria
Con el cantar se consuela.'''


# * Cuente la cantidad de veces que aparecen los substrings `es`, `la`, `que`, `co`,  en los siguientes dos casos: distinguiendo entre mayúsculas y minúsculas, y no distinguiendo. Imprima el resultado.

# In[18]:


#Distinguiendo entre mayusculas y minusculas
es=str(s.count("es",))
la=str(s.count("la"))
que=str(s.count("que"))
co=str(s.count("co"))
print("Distinguiendo:")
print('Cantidad "es": '+ es)
print('Cantidad "la": '+ la)
print('Cantidad "que": '+ que)
print('Cantidad "co": '+ co)
print("\n")

#Sin distinguir entre mayusculas y minusculas
sAux=s.lower()
es=str(sAux.count("es"))
la=str(sAux.count("la"))
que=str(sAux.count("que"))
co=str(s.count("co"))
print("Sin distinguir:")
print('Cantidad "es": '+ es)
print('Cantidad "la": '+ la)
print('Cantidad "que": '+ que)
print('Cantidad "co": '+ co)
print("\n")


#  * Cree una lista, donde cada elemento es una línea del string `s` y encuentre la de mayor longitud. Imprima por pantalla la línea y su longitud. (Posibles ayudas: busque información sobre funciones que aplican a *strings* y los métodos)

# In[24]:


lista=s.splitlines()
#detecto cual es el más largo
indice=0
Lmayor=0
for i in lista:
    if len(i)>len(lista[Lmayor]):
        Lmayor=indice       
    indice+=1
#y lo imprimo
print("la línea más larga es: '"+ lista[Lmayor] + "'. Longitud: "+ str(len(lista[Lmayor]))+"\n\n" )


#   * Forme un nuevo string de 10 caracteres que contenga los 5 primeros y los 5 últimos del string anterior `s`. Imprima por pantalla el nuevo string.

# In[8]:


Nuevostring=s[:5]+s[-5:]
print(Nuevostring+"\n\n")


#   * Forme un nuevo string que contenga los 10 caracteres centrales de `s` (utilizando un método que pueda aplicarse a otros strings también). Imprima por pantalla el nuevo string.

# In[9]:


CaracteresImprimir=10
CaracteresTotales=len(s)
CaracterInicial=(CaracteresTotales-CaracteresImprimir)//2
CaracterFinal=CaracterInicial + CaracteresImprimir
print("Cantidad a imprimir: ", CaracteresImprimir, ", desde el numero ", CaracterInicial, " hasta el ", CaracterFinal,"\n")

CadenaImprimir=s[CaracterInicial:CaracterFinal]
print(CadenaImprimir+"\n\n")


#  * Cambie todas las letras "m" por "n" y todas las letras "n" por "m" en `s`. Imprima el resultado por pantalla.

# In[10]:


r=s.replace("m","-")
r=r.replace("n","m")
r=r.replace("-","n")
print(r)


# In[ ]:





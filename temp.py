import numpy as np
import pylab as pl
#Vector (arreglo) con los valores del eje x
x=[6000,7000,8000,9000,10000]
#Vector (arreglo) con los valores del eje y
y=[73,80,85,87,89]
#Grafica el vector x contra el vector y
pl.plot (x, y)

# Crea un vector (arreglo) con los valores del eje X

x1 = [7000, 8000, 9000, 10000, 11000]
# Crea un vector (arreglo) con valores en el eje Y para cada valior en el eje X

y2 = [80, 83, 85, 86, 88]
# Grafica el vector x contra el vector y 

pl.plot(x1, y2)


pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia [%]')
# Guarda la grafica en formato png
pl.savefig('temp1.png')

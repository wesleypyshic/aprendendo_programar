import numpy as np 
import matplotlib.pyplot as plt
import calc_raizes as cr

a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

'''
def raizes(a,b,c): 

# eq. 2 grau
# encontrar as raizes 
# a*x**2 + b*x + c = 0
 
    delta = b**2 - 4*a*c

    if delta < 0:
        print('Não tem solução nos Reais.')
    else:
        x1 = (-b + np.sqrt(delta) )/(2*a)
        x2 =(-b - np.sqrt(delta) )/(2*a)
        print('As raizes são: x1 =', x1, ', x2 =', x2)

#vertice

    xv = -b/(2*a)
    yv = -delta/(4*a)
    print('coordenadas do vertice são:', (xv, yv))

    return x1, x2, xv, yv
 '''

cr.raizes(a,b,c)

x = np.linspace(-5, 5, 500)
y = (a*x**2 + b*x + c)

# grafico

plt.plot(x,y)
plt.title('eq. segundo grau')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim([-5,5])
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import calc_raizes as cr

a = float(input('a = '))
b = float(input('b = '))
x = np.linspace(0, 10, 100)
y = a*x + b

# gráfico função do primeiro grau

print((x, y))
plt.plot(x,y)
plt.title("Gráfico de y = ax + b")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# resolver ax + b = 0


if a == 0 and b == 0:
    print('inderteminado')
elif a == 0:
    print('Falha')
else:
    x = - b/a
    print('x =', x)


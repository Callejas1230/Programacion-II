import math
import numpy as np
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def coord_cartesianas(self):
        return [self.x, self.y]
    def coord_polares(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        return [r, theta]
    def __str__(self):
        return f'Punto(x={self.x}, y={self.y})'
punto1 = Punto(3, 1)
punto2 = Punto(1, 5)

#LINEA
x_coords = [punto1.x, punto2.x]
y_coords = [punto1.y, punto2.y]

plt.plot(x_coords, y_coords, label="Línea entre puntos", marker="o")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Línea en base a la Clase Punto')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

#----------------------------------------------------------------------

#CIRCUNFERENCIA

centro = Punto(2, 2)
radio = float(1.5)
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = centro.x + radio * np.cos(theta)
y_circle = centro.y + radio * np.sin(theta)

plt.plot(x_circle, y_circle, label=f'Circunferencia (Centro: {centro}, Radio: {radio})')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Circunferencia en base a la Clase Punto')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

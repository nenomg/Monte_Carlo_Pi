# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:45:57 2023

@author: Neno
"""

import random
import numpy as np
import math
import matplotlib.pyplot as plt

def monte_carlo(num_points):
    points_inside_circle = 0
    points_total = 0

    for _ in range(num_points):
        # Generar coordenadas aleatorias en el rango de -1 a 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Verificar si el punto está dentro del círculo de radio 1
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
        
        points_total += 1

    # Calcular la aproximación de pi
    pi_approximation = 4 * (points_inside_circle / points_total)

    return pi_approximation


def simulate():
    num_points=100
    res = []
    
    for i in range(0,100):
        num_points=num_points+5000
        approx_pi = monte_carlo(num_points)
        print(f"Aproximación de pi con {num_points} puntos: {approx_pi}")
        res.append(approx_pi)
        
    return res



res = simulate()

pi_actual = math.pi
y = np.abs(np.subtract(res, pi_actual))
X= np.arange(len(y))

plt.scatter(X,y)

# Generate x and y values
x2 = np.arange(len(y))
y2 = np.array(y)

# Perform linear regression to find the line of best fit
m, b = np.polyfit(x2, y2, 1)

# Create the line of best fit
line_of_best_fit = m * x2 + b

# Plot the data points and line of best fit
plt.scatter(x2, y2, color='b', label='Data Points')
plt.plot(x2, line_of_best_fit, color='r', label='Line of Best Fit')

# Add labels and title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line of Best Fit')

# Add legend
plt.legend()

# Display the plot
plt.show()
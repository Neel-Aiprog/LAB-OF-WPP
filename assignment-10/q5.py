import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return x**3 - 4*x - 9  
def find_initial_interval(f, lower=-10, upper=10, max_attempts=1000):
    for _ in range(max_attempts):
        a = random.uniform(lower, upper)
        b = random.uniform(lower, upper)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b
    raise Exception("Failed to find valid interval after many attempts")

# Bisection method
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    midpoints = []
    
    for i in range(max_iter):
        c = (a + b) / 2
        midpoints.append(c)
        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return np.array(midpoints)

a, b = find_initial_interval(f)
print(f"Initial interval found: a = {a:.4f}, b = {b:.4f}")

midpoints = bisection_method(f, a, b)

x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8)

for i, c in enumerate(midpoints):
    plt.plot(c, f(c), 'ro')
    plt.text(c, f(c), f'{i}', fontsize=8, ha='right')

plt.title("Bisection Method: Root Finding Process")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

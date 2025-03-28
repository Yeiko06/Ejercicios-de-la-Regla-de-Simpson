import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    
    return integral

# Parámetros del problema
k = 200  # N/m
a = 0.1  # m
b = 0.3  # m

# Función a integrar
def funcion(x):
    return k * x

# Solución analítica
def solucion_analitica(a, b):
    return (k/2) * (b**2 - a**2)

# Valores de n a probar
n_values = [6, 10, 20, 30]

# Resultados
print("Ejercicio 1: Cálculo del trabajo en un resorte")
print(f"Solución analítica: {solucion_analitica(a, b):.6f} J\n")

for n in n_values:
    resultado = simpson_rule(funcion, a, b, n)
    error = abs(resultado - solucion_analitica(a, b))
    print(f"n = {n}: Aproximación = {resultado:.6f} J, Error = {error:.6e}")

# Gráfica para n=10
n = 10
x_vals = np.linspace(a, b, 100)
y_vals = funcion(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = 200x$", color="blue")
plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(a, b, n+1), funcion(np.linspace(a, b, n+1)), color="red", label="Puntos de interpolación")
plt.xlabel("x (m)")
plt.ylabel("Fuerza (N)")
plt.title("Trabajo realizado por el resorte (Regla de Simpson, n=10)")
plt.legend()
plt.grid()
plt.savefig("ejercicio1_simpson.png")
plt.show()
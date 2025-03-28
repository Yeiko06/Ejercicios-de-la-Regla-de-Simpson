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
k = 0.5  # W/m·K
x1 = 0   # m
x2 = 2   # m

# Función de temperatura
def T(x):
    return 300 - 50 * x**2

# Derivada de la temperatura
def dTdx(x):
    return -100 * x

# Solución analítica
def solucion_analitica(x1, x2):
    return k * (T(x1) - T(x2))

# Valores de n a probar
n_values = [6, 10, 20, 30]

# Resultados
print("Ejercicio 3: Flujo de calor a través de una pared")
print(f"Solución analítica: {solucion_analitica(x1, x2):.6f} W\n")

for n in n_values:
    resultado = k * simpson_rule(dTdx, x1, x2, n)
    error = abs(resultado - solucion_analitica(x1, x2))
    print(f"n = {n}: Aproximación = {resultado:.6f} W, Error = {error:.4e}")

# Gráfica para n=10
n = 10
x_vals = np.linspace(x1, x2, 100)
dTdx_vals = dTdx(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, dTdx_vals, label=r"$\frac{dT}{dx} = -100x$", color="blue")
plt.fill_between(x_vals, dTdx_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(x1, x2, n+1), dTdx(np.linspace(x1, x2, n+1)), color="red", label="Puntos de interpolación")
plt.xlabel("Posición (m)")
plt.ylabel("Gradiente de temperatura (K/m)")
plt.title("Flujo de calor (Regla de Simpson, n=10)")
plt.legend()
plt.grid()
plt.savefig("ejercicio3_simpson.png")
plt.show()
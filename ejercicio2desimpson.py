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
C = 1e-6  # F
T = 5     # s

# Función a integrar
def V(t):
    return 100 * np.exp(-2 * t)

# Solución analítica
def solucion_analitica(T):
    return C * 100 * (1 - np.exp(-2 * T)) / 2

# Valores de n a probar
n_values = [6, 10, 20, 30]

# Resultados
print("Ejercicio 2: Cálculo de la carga eléctrica en un capacitor")
print(f"Solución analítica: {solucion_analitica(T):.10f} C\n")

for n in n_values:
    resultado = C * simpson_rule(V, 0, T, n)
    error = abs(resultado - solucion_analitica(T))
    print(f"n = {n}: Aproximación = {resultado:.10f} C, Error = {error:.4e}")

# Gráfica para n=10
n = 10
t_vals = np.linspace(0, T, 100)
V_vals = V(t_vals)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, V_vals, label=r"$V(t) = 100e^{-2t}$", color="blue")
plt.fill_between(t_vals, V_vals, alpha=0.3, color="cyan", label="Área aproximada")
plt.scatter(np.linspace(0, T, n+1), V(np.linspace(0, T, n+1)), color="red", label="Puntos de interpolación")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title("Carga en el capacitor (Regla de Simpson, n=10)")
plt.legend()
plt.grid()
plt.savefig("ejercicio2_simpson.png")
plt.show()
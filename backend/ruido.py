import math

def calcular_ruido(temperatura, frecuencia):
    """
    Calcula el ruido térmico (en watts) según la ecuación:
    N = k * T * f
    donde:
        k: constante de Boltzmann (1.38e-23)
        T: temperatura (Kelvin)
        f: frecuencia (Hz)
    """
    k = 1.38e-23  # constante de Boltzmann
    ruido_watts = k * temperatura * frecuencia
    return ruido_watts


def convertir_a_dbm(ruido_watts):
    """
    Convierte la potencia de ruido de Watts a dBm.
    Fórmula: 10 * log10(ruido_watts / 0.001)
    """
    if ruido_watts <= 0:
        return float('-inf')  # evitar logaritmo de 0 o negativo
    ruido_dbm = 10 * math.log10(ruido_watts / 0.001)
    return ruido_dbm


# --- Prueba del funcionamiento ---
if __name__ == "__main__":
    temperatura = float(input("Ingrese la temperatura en Kelvin: "))
    frecuencia = float(input("Ingrese la frecuencia en Hz: "))

    ruido_watts = calcular_ruido(temperatura, frecuencia)
    ruido_dbm = convertir_a_dbm(ruido_watts)

    print("\nResultados del cálculo de ruido:")
    print(f"Ruido térmico: {ruido_watts:.5e} W")
    print(f"Ruido térmico: {ruido_dbm:.2f} dBm")

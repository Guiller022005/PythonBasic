import math

# Constantes
H_pequeño = 47  # masa para un huevo pequeño en gramos
H_grande = 67   # masa para un huevo grande en gramos
ρ = 1.038       # densidad en g/cm^3
c = 3.7         # capacidad calorífica específica en J/g/K
K = 5.4e-3      # conductividad térmica en W/cm/K
Tw = 100        # temperatura de ebullición del agua en °C

def tiempo_para_alcanzar_temperatura(Temperatura_original, Ty):
    # Conversión de temperatura a Kelvin
    To_K = Temperatura_original + 273.15
    Tw_K = Tw + 273.15
    Ty_K = Ty + 273.15

    # Cálculo de la masa
    masa = H_pequeño if Temperatura_original < 70 else H_grande

    # Cálculo del tiempo
    tiempo = (masa**(2/3) * c * ρ**(1/3) * K * math.pi**2 * (4 * math.pi / 3)**(2/3) *
              math.log(0.76 * (To_K - Tw_K) / (Ty_K - Tw_K)))
    
    return tiempo

# Función principal
def main():
    # Entrada de temperatura original del huevo
    Temperatura_original = float(input("Ingrese la temperatura original del huevo (en grados Celsius): "))

    # Temperatura máxima para hacer un huevo a la copa
    Temperatura_max = 70

    # Cálculo del tiempo para alcanzar la temperatura máxima
    tiempo = tiempo_para_alcanzar_temperatura(Temperatura_original, Temperatura_max)

    # Salida del tiempo en segundos
    print(f"El tiempo en segundos que toma al centro de la yema alcanzar los {Temperatura_max}°C es: {tiempo:.2f} segundos.")

if __name__ == "__main__":
    main()





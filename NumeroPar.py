# Determina si un numero es par o impar
num = int(input("Ingresa un numero"))

residuo = num / 2

if residuo == 0:
    print(f"El numero: {num} es Par")

else:
    print(f"El numero: {num} es impar")

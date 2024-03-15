def division(dividendo, divisor):
    cociente = dividendo // divisor  # Calcula el cociente
    resto = dividendo % divisor  # Calcula el resto

    if (resto == 0):
        return True, cociente, resto
    else:
        return False, cociente, resto

def div():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))

    es_exacta, cociente, resto = division(dividendo, divisor)

    if es_exacta:
        print("La división es exacta.")
    else:
        print("La división no es exacta.")
    print("Cociente:", cociente)
    print("Resto:", resto)

if __name__ == "__main__":
    div()

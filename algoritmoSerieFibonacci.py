def fibonacci(num):
    serie = []
    a, b = 0, 1
    for _ in range(num):
        serie.append(a)
        a, b = b, a + b
    return serie

num_terminos = int(input("Ingresa un numero"))
resultado = fibonacci(num_terminos)
print("Serie de Fibonacci con", num_terminos, "es", resultado)
    

def tipo_de_triangulo(ladoDelTriangulo_a, ladoDelTriangulo_b, ladoDelTriangulo_c):
    if ladoDelTriangulo_a >= ladoDelTriangulo_b + ladoDelTriangulo_c or ladoDelTriangulo_b >= ladoDelTriangulo_a + ladoDelTriangulo_c or ladoDelTriangulo_c >= ladoDelTriangulo_a + ladoDelTriangulo_b:
        return "No es un triángulo válido."
    elif ladoDelTriangulo_a == ladoDelTriangulo_b == ladoDelTriangulo_c:
        return "El triángulo es equilátero."
    elif ladoDelTriangulo_a == ladoDelTriangulo_b or ladoDelTriangulo_a == ladoDelTriangulo_c or ladoDelTriangulo_b == ladoDelTriangulo_c:
        return "El triángulo es isósceles."
    else:
        return "El triángulo es escaleno."
    





# Solicitar entrada de los lados del triángulo
ladoDelTriangulo_a = float(input("Ingrese ladoDelTriangulo_a: "))
ladoDelTriangulo_b = float(input("Ingrese ladoDelTriangulo_b: "))
ladoDelTriangulo_c = float(input("Ingrese ladoDelTriangulo_c: "))

# Determinar y mostrar el tipo de triángulo
print(tipo_de_triangulo(ladoDelTriangulo_a, ladoDelTriangulo_b, ladoDelTriangulo_c))







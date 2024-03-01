h_1 = int(input("Ingresa la primer Hora"))
cantidad_h = int(input("Ingresa la cantidad de horas"))
nueva_hora = (h_1 + cantidad_h) % 12
if nueva_hora == 0:
    nueva_hora = 12
print(f"En {cantidad_h} horas, el reloj marcarà las {nueva_hora}")
nota_1 = int(input("Ingresa tu nota del certamen 1"))
nota_2 = int(input("Ingresa tu nota del certamen 2"))
nota_lab = int(input("Ingresa tu nota de laboratorio"))

promedio = (60 - (nota_lab * 0.3))/ (0.7)
nota_falt = round((promedio * 3) - (nota_1 + nota_2),1)

print(f"La nota que necesitas en el tercer examen para aprobar un ramo es:{nota_falt} ")
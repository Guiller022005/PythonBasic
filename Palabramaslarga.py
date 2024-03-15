palabra1 = str(input("Ingresa una palabra "))
palabra2 = str(input("Ingresa otra palabra "))
#Longitud
longitud1 = len(palabra1)
longitud2 = len(palabra2)
if longitud1 > longitud2:
    dif = longitud1 - longitud2
    print(f"La primer palabra ingresda: {palabra1} tiene {dif} letras mas q {palabra2}")
elif longitud2 > longitud1:
    dif = longitud2 - longitud1
    print(f"La primer palabra ingresda: {palabra2} tiene {dif} letras mas q {palabra1}")
elif longitud1 == longitud2:
    print("Las dos palabras ingresadas tienen igual cantidad de letras")
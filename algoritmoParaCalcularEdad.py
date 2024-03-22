from datetime import datetime

fecha_hoy = datetime.now()

dia_De_Nacimiento = int(input("Ingresa el día de tu nacimiento: "))
mes_De_Nacimiento = int(input("Ingresa el mes de tu nacimiento: "))
año_De_Nacimiento = int(input("Ingresa el año de tu nacimiento: "))

edad = fecha_hoy.year - año_De_Nacimiento

if fecha_hoy.month < mes_De_Nacimiento or (fecha_hoy.month == mes_De_Nacimiento and fecha_hoy.day < dia_De_Nacimiento):
    edad -= 1
    
else:
    print(f"\nTu edad es: {edad} años")




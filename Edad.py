from datetime import datetime

def Edad(dia_nacimiento, mes_nacimiento, año_nacimiento):
    fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)
    fecha_actual = datetime.now()

    if fecha_actual.month > mes_nacimiento or (fecha_actual.month == mes_nacimiento and fecha_actual.day >= dia_nacimiento):
        edad = fecha_actual.year - año_nacimiento
    else:
        edad = fecha_actual.year - año_nacimiento - 1

    return edad

def main():
    dia = int(input("Día de nacimiento: "))
    mes = int(input("Mes de nacimiento: "))
    año = int(input("Año de nacimiento: "))

    edad = Edad(dia, mes, año)
    print(f"Usted tiene {edad} años.")

if __name__ == "__main__":
    main()

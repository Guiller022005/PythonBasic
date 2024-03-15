año = int(input("Ingresa un año: "))
def año_bisiesto(año):
    if (año % 4) == 0:  # Si es divisible por 4
        if (año % 100) == 0:  # Si es divisible por 100
            if (año % 400) == 0:  # Si es divisible por 400
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    
if año_bisiesto(año):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")



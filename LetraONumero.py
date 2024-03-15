caracteres = input("Ingresa un caracter ")
if caracteres.isalpha():
    if caracteres.isupper(): 
        print(f"El caracter {caracteres} es una letra mayuscula ")
    else:
        print(f"El caracter {caracteres} es una letra minuscula ")
elif caracteres.isdigit():
    print(f"El caracter {caracteres} es un numero")
else:
    print(f"El caracter {caracteres} no es ni una palabra ni un numero")

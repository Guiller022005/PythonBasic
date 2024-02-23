numero1 = int(input("ingrese el 1 numero"))
numero2 = int(input("ingrese el 2 numero"))
numero3 = int(input("ingrese el 3 numero"))
noresult = 0
if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor de los tres numeros es ",numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El numero mayor de los tres numeros es ",numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("El numero mayor de los tres numeros es ",numero3)
elif numero3 == numero1 > numero2:
    print("El numero mayor de los tres numeros es ",numero3, numero1)
elif numero2 == numero1 > numero3:
    print("El numero mayor de los tres numeros es ",numero2, numero1)
elif numero3 == numero2 > numero1:
    print("El numero mayor de los tres numeros es ",numero3, numero2)
elif numero3 == numero2 == numero1:
    print("Ningun numero es mayor",noresult)
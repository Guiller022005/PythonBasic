numero = int(input("ingresa un numero"))
fact = 1
if numero < 0:
    print("El numero no se puede calcular")
for i in range(1,numero+1):
    fact*=i
print("el factorial de ",numero, "es:",fact)

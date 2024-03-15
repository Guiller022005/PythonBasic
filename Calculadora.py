numero1 = float(input("Ingresa un numero: "))
operador = input("Operador: ")
numero2 = float(input("Ingresa un numero: "))




if operador == '+':
    print(f"{numero1} + {numero2} = {numero1 + numero2}") 
elif operador == '-':
    print(f"{numero1} - {numero2} ={numero1 - numero2}") 
elif operador == '*':
    print(f"{numero1} * {numero2} = {numero1 * numero2}") 
elif operador == '/':
    print(f"{numero1} / {numero2} ={numero1 / numero2}")
else:
    print("Operador no válido.") 

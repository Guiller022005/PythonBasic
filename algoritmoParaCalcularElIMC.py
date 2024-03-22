# Solicitar entrada de datos
edad = int(input("Ingrese tu edad en años: "))
peso = float(input("Ingrese tu peso en kg: "))
estatura = float(input("Ingrese tu estatura en metros: "))


def Calcula_IMC(peso, estatura):
    return peso / (estatura ** 2)

def Riesgo(edad, imc):
    if edad < 45:
        if imc < 22.0:
            return "bajo"
        else:
            return "medio"
    else:
        if imc < 22.0:
            return "medio"
        else:
            return "alto"



# Calcular el IMC
imc = Calcula_IMC(peso, estatura)

# Determinar y mostrar la condición de riesgo
condicion = Riesgo(edad, imc)
print(f"\nLa condición de riesgo es: {condicion}")
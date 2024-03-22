def resultadosDelSet(juegos_A, juegos_B):
    if abs(juegos_A - juegos_B) < 2 or max(juegos_A, juegos_B) > 7:
        return "Invalido"
    elif juegos_A >= 6 and juegos_A - juegos_B >= 2:
        return "Gano A"
    elif juegos_B >= 6 and juegos_B - juegos_A >= 2:
        return "Gano B"
    elif juegos_A == 5 and juegos_B == 5:
        return "Aun no termina"
    elif juegos_A == 6 and juegos_B == 6:
        return "Aun no termina"
    elif juegos_A == 5 and juegos_B == 6:
        return "Aun no termina"
    elif juegos_A == 6 and juegos_B == 5:
        return "Aun no termina"
    else:
        return "Aun no termina"

# Ejemplos de uso
while True:
    juegos_ganados_A = int(input("Juegos ganados por A: "))
    juegos_ganados_B = int(input("Juegos ganados por B: "))

    resultado = resultadosDelSet(juegos_ganados_A, juegos_ganados_B)
    print(resultado)

    if resultado != "Aun no termina":
        break

if resultado == "Gano A":
    print("¡El jugador A ha ganado el set!")
elif resultado == "Gano B":
    print("¡El jugador B ha ganado el set!")





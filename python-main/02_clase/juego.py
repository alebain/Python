import random

def juego_piedra_papel_tijera():
    print("Bienvenido al juego de piedra, papel o tijera")
    print("Elegi una opcion: ")
    
    opciones = ["piedra", "papel", "tijera"] #lista de opciones
    
    contador_jugador = 0
    contador_computadora = 0
    contador_empate = 0

    while True:
        jugador = input("Escribir piedra, papel o tijera: ").lower()

        if jugador not in opciones:
            print("Opcion invalida")
            break

        computadora = random.choice(opciones)

        if jugador == computadora:
            print("empate")
            contador_empate += 1
        elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
            print("gana jugador")
            contador_jugador += 1 #contador_jugador = contador_jugador + 1
        else:
            print("gana computadora")
            contador_computadora += 1

        print("la computadora eligio: ", computadora)

        jugar_nuevamente = input("Jugar nuevamente? (s/n): ")

        if jugar_nuevamente != "s":
            break

    print("El jugador gano: ", contador_jugador)
    print("La computadora gano: ", contador_computadora)
    print("Empates: ", contador_empate)
    print("Gracias por jugar")


#ARRANCA NUESTRO PROGRAMA - EL PUNTO DE ENTRADA A NUESTRA APLICACION

juego_piedra_papel_tijera()

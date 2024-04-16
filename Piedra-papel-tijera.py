import random
victorias = 0
derrotas = 0
empates = 0
while True:
    user_action = input("piedra, papel o tijera: ")
    possible_actions = ["piedra", "papel", "tijera"]
    computer_action = random.choice(possible_actions)
    print(f"\nElegiste {user_action}, la computadora eligio {computer_action}.\n")
    if user_action == computer_action:
        print(f"Los dos jugadores eligieron {user_action}. Es un empate!")
        empates=empates+1
    elif user_action == "piedra":
        if computer_action == "tijera":
            print("piedra aplasta tijera! Ganaste!")
            victorias=victorias+1
        else:
            print("papel cubre piedra! Perdiste.")
            derrotas=derrotas+1
    elif user_action == "papel":
        if computer_action == "piedra":
            print("papel cubre piedra! Ganaste!")
            victorias=victorias+1
        else:
            print("tijera corta papel! Perdiste.")
            derrotas=derrotas+1
    elif user_action == "tijera":
        if computer_action == "papel":
            print("tijera corta papel! Ganaste!")
            victorias=victorias+1
        else:
            print("piedra aplasta tijera! Perdiste.")
            derrotas=derrotas+1
    elif user_action == "pistola":
        print("Ganaste, ahora no me mates por favor tengo familia.")
        victorias=victorias+1
    print(f"Victorias: {victorias}")
    print(f"Derrotas : {derrotas}")
    print(f"Empates: {empates}")
    play_again = input("Jugar de vuelta? (si/no): ")
    if play_again.lower() != "si":
        break
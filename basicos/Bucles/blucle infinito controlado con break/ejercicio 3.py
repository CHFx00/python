import random

numero_secreto = random.randint(1, 20)
while True:
    intento = input("Adivina el número (o escribe 'salir' para rendirte): ")
    
    if intento.lower() == "salir":
        print(f"El número secreto era {numero_secreto}. ¡Gracias por jugar!")
        break

    intento = int(intento)
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

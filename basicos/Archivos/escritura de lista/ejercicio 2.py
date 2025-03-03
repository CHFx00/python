
nombres = ["Ana", "Juan", "María", "Carlos", "Sofía"]


with open("nombres.txt", "w", encoding="utf-8") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")  # Escribir cada nombre en una nueva línea

print("Los nombres han sido guardados en nombres.txt.")

with open("origen.txt", "r", encoding="utf-8") as archivo_origen:
    contenido = archivo_origen.read()  # Leer el contenido completo

with open("destino.txt", "w", encoding="utf-8") as archivo_destino:
    archivo_destino.write(contenido)

print("El contenido ha sido copiado de origen.txt a destino.txt.")


palabra_buscada = input("Ingrese la palabra a buscar: ").lower()


with open("articulo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().lower()  # Convertir a minúsculas para evitar problemas de mayúsculas
    ocurrencias = contenido.count(palabra_buscada)  # Contar apariciones

print(f'La palabra "{palabra_buscada}" aparece {ocurrencias} veces en el archivo.')

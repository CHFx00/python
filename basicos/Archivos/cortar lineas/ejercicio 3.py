
with open("poema.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()  # Lee todas las líneas y las guarda en una lista
    print(f"El archivo tiene {len(lineas)} líneas.")  # Contar elementos de la lista



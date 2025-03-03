cadena = "Python es genial"
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for letra in cadena if letra in vocales)
print("Cantidad de vocales:", contador_vocales)

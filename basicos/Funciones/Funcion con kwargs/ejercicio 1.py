
def imprimir_detalles(**detalles):
    for clave, valor in detalles.items():
        print(f"{clave}: {valor}")


imprimir_detalles(nombre="Carlos", edad=28, ciudad="Madrid")
print("----")
imprimir_detalles(producto="Laptop", precio=1200, marca="Dell")

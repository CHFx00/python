productos_caros = [producto for producto, precio in productos.items() if precio > 1.0]
print("Productos con precio mayor a 1.0:", productos_caros)

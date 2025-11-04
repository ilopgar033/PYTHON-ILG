cesta = input("Introduce los productos de la cesta de la compra, separados por comas: ")
productos = cesta.split(',')

print("Productos en la cesta:")
for producto in productos:
    print(producto.strip())
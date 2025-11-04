edad = int(input("Edad del cliente: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10

if precio == 0:
    print("Entrada GRATIS")
else:
    print(f"Precio: {precio}€")
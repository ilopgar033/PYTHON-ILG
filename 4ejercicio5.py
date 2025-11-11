cantidad = float(input("¿Cantidad a invertir? "))
interes_anual = float(input("¿Interés porcentual anual? "))
anos = int(input("¿Número de años? "))
interes_decimal = interes_anual / 100
for i in range(1, anos + 1):
    cantidad = cantidad * (1 + interes_decimal)
    print("Capital tras el año", i, ":", round(cantidad, 2))
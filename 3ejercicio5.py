edad = int(input("Edad: "))
ingresos = float(input("Ingresos mensuales (€): "))
if edad > 16 and ingresos >= 1000:
    print("Debe tributar")
else:
    print("No debe tributar")
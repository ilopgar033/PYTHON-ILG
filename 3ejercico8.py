puntuacion = float(input("Puntuación: "))
base = 2400

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = "No válida"
    
if nivel != "No válida":
    dinero = puntuacion * base
    print(f"Nivel: {nivel}")
    print(f"Dinero a recibir: {dinero:,.2f}€")
else:
    print(nivel)
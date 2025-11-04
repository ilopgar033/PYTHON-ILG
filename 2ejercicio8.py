def descomponer():
    precio = input("Introduce el precio (ej: 12.34): ")
    
    if '.' in precio:
        euros, centimos = precio.split('.')
        print(f"Euros: {euros}")
        print(f"Céntimos: {centimos[:2]}")
    else:
        print("El formato debe incluir decimales (con punto).")

descomponer()
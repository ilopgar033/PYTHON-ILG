# Ejercicio 3
try:
    n1 = float(input("Dividendo: "))
    n2 = float(input("Divisor: "))
    if n2 == 0:
        print("Error: El divisor es cero.")
    else:
        print(n1 / n2)
except ValueError:
    print("Error de entrada.")
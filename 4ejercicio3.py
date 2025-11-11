numero = int(input("Introduce un número entero positivo: "))
impares = []

for i in range(1, numero + 1, 2):
    impares.append(str(i))

print(", ".join(impares))
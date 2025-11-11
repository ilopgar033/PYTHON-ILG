numero = int(input("Introduce un número entero positivo: "))
numeros_atras = []
for i in range(numero, -1, -1):
    numeros_atras.append(str(i))
print(", ".join(numeros_atras))
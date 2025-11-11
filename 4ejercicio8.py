n = int(input("Introduce un número entero: "))
for i in range(1, n + 1):
    numeros_fila = []
    impar_inicial = 2 * i - 1 
    for j in range(impar_inicial, 0, -2):
        numeros_fila.append(str(j))
    print(" ".join(numeros_fila))
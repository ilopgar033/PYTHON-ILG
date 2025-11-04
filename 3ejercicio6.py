nombre = input("Nombre: ").upper()
sexo = input("Sexo (M/H): ").upper()

if (sexo == 'M' and nombre < 'M') or (sexo == 'H' and nombre > 'N'):
    print("Grupo A")
else:
    print("Grupo B")
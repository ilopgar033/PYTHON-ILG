# Ejercicio 2
contrasena_almacenada = "contraseña"
contrasena_usuario = input("Introduce la contraseña: ")

if contrasena_almacenada == contrasena_usuario.lower():
    print("¡Contraseña correcta!")
else:
    print("Contraseña incorrecta.")
def cambiar_correo():
    correo = input("Introduce tu correo electrónico: ")
    
    if '@' in correo:
        nombre = correo.split('@')[0]
        nuevo_correo = nombre + "@ceu.es"
        print(f"Tu nuevo correo CEU es: {nuevo_correo}")
    else:
        print("Formato de correo no válido.")

cambiar_correo()
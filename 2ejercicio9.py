def desglosar_fecha():
    fecha = input("Fecha (dd/mm/aaaa): ")
    
    if '/' in fecha:
        dia, mes, anio = fecha.split('/')
        
        print(f"Día: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {anio}")
    else:
        print("Formato incorrecto.")

desglosar_fecha()
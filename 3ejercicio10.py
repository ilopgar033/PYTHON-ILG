tipo = input("¿Vegetariana (V) o No Vegetariana (N)? ").upper()

if tipo == 'V':
    print("Ingredientes vegetarianos: 1. Pimiento, 2. Tofu")
    ing = input("Elige (1 o 2): ")
    ing_extra = "Pimiento" if ing == '1' else "Tofu"
    tipo_pizza = "Vegetariana"
else:
    print("Ingredientes no vegetarianos: 1. Peperoni, 2. Jamón, 3. Salmón")
    ing = input("Elige (1, 2 o 3): ")
    if ing == '1': ing_extra = "Peperoni"
    elif ing == '2': ing_extra = "Jamón"
    else: ing_extra = "Salmón"
    tipo_pizza = "No Vegetariana"

print(f"Pizza {tipo_pizza} con: Mozzarella, Tomate, y {ing_extra}")
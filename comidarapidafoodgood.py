nombre = input("Bienvenido a FoodGood, Indiqueme su Nombre:")
print("Seleccione un Combo:")
print("1-Big Gloton       6500 8900")
print("2-Tocomples Full   3000 4500")
print("3-Fajitas Taliban  2400 3200")
print("4-Papas US Love    1450 2400")

opcion = int(input("Seleccione:"))
tamaño = input("Normal o XL:")
cant_c = int(input("Cuantas:"))

precio_c = 0
if opcion == 1:
    if tamaño == "Normal" or tamaño == "normal": precio_c = 6500
    else: precio_c = 8900
if opcion == 2:
    if tamaño == "Normal" or tamaño == "normal": precio_c = 3000
    else: precio_c = 4500
if opcion == 3:
    if tamaño == "Normal" or tamaño == "normal": precio_c = 2400
    else: precio_c = 3200
if opcion == 4:
    if tamaño == "Normal" or tamaño == "normal": precio_c = 1450
else: precio_c = 2400

bebida_sn = input("Desea Bebida:").lower()
precio_b = 0
cant_b = 0

if bebida_sn =="s":
print("1-Normal $1200")
print("2-Grande $2300")
print("3-XL     $3200")
opcion_b = int(input("Seleccione:"))
cant_b = int(input("Cuantas:"))
if opcion_b == 1: precio_b = 1200
if opcion_b == 2: precio_b = 2300
if opcion_b == 3: precio_b = 3200

cant_prod = cant_c + cant_b
neto = (precio_c * cant_c) + (precio_b * cant_b)
iva = neto * 0.19
total = neto + iva

print("\nCantidad de Productos:", cant_prod)
print("Total: $", int(neto))
print("Iva: $", int(iva))
print("--------------------")
print("Total $", int(total))

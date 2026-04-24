print("Bienvenido Al Cine")

nombre = input("Ingrese Nombre de Usuario:")
clave = input("Ingrese Contraseña:")

print("-" * 45)

publico = input("Indique el Tipo de Usuario(Normal, Estudiante, Adulto Mayor):")
sala = input("Tipo de Sala(Normal, 3D, 4DX):")
cantidad = int(input("Cantidad de Entradas:"))

tarifa = 0

if publico == "Normal":
    if sala == "Normal":
        tarifa = 5600
    elif sala == "3D":
        tarifa = 7800
    elif sala == "4DX":
        tarifa = 12000

elif publico == "Estudiante":
    if sala == "Normal":
        tarifa = 3400
    elif sala == "3D":
        tarifa = 4800
    elif sala == "4DX":
        tarifa = 7000
        
elif publico == "Adulto Mayor":
    if sala == "Normal":
        tarifa = 2500
    elif sala == "3D":
        tarifa = 3500
    elif sala == "4DX":
        tarifa = 4800
        
sub_total = tarifa * cantidad
iva = sub_total * 0.19
total = sub_total + iva

print("-" * 45)
print("Sub Total: $", int(sub_total))
print("Iva: $", int(iva))
print("-" * 45)
print("Total : $", int(total))
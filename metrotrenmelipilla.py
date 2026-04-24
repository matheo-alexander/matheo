usuario = input("Ingrese Tipo de Usuario(Estudiante, Adulto, Adulto Mayor):")
horario = input("Horario del viaje(Normal,Punta):")

if usuario == "Adulto":
    if horario == "Punta":
        print("La Tarifa a Pagar Sera de: $890")
    else:
        print("La Tarifa a Pagar Sera de: $790")

elif usuario == "Estudiante":
    if horario == "Punta":
        print("La Tarifa a Pagar Sera de: $590")
    else:
        print("La Tarifa a Pagar Sera de: $490")

elif usuario == "Adulto Mayor":
    if horario == "Punta":
        print("La Tarifa a Pagar Sera de: $490")
    else:
        print("La Tarifa a Pagar Sera de: $390")


print("Gracias por Viajar con nosotros")
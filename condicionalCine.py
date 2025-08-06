
edad = int(input("Ingresa tu edad: "))
print ("Tu edad es: ", edad)

if edad < 4:
    print("Entras Gratis.")
else:
    if edad>=4 and edad <=12:
        print("Pagaras un boleto infantil de: $40.00 .")
    else:
        if edad>=13 and edad <=59:
            print("Pagaras un boleto general de $70.00 .")
        else:
            print("Pagaras un boleto con descuento de $35.00 .")

print("\nPrograma que ingresa calificaciones y calcula promedio, (-1 para salir)")
numero = None
cont= -1
suma= 1
prom= 0
while numero != -1:
    numero = int(input("Ingresa la Calificacion: "))
    suma = suma + numero
    cont= cont + 1
print("Terminaste el ciclo.")
prom= suma/cont
print(" El total de Calificaciones ingresadas son: ", cont)
print("El promedio del Grupo es: ", prom)



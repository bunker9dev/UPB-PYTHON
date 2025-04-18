# Formatear cadenas 
''' 
x = 10
y = 35

print("Mis numero son " + str(x) + " y "+ str(y)) #antigua

print("Mis numero son {} y {}".format(x,y)) # funcion format

print("la suma de {} y {} es igual a {}".format(x,y,x+y)) # funcion format

'''

#nuevo

'''
color = "negro"

valor = 25000000

print(f" El auto es de color {color} y tiene un valor de {valor}")


'''
# Ejercicio 35
nombreAsociado = "Pedro Perez"
numeroAsociado = 785485

print(f"Estimado/a {nombreAsociado}, su número de asociado es: {numeroAsociado}")

# Ejercicio 36
puntosNuevos = 2556
puntosTotales = 45856

print(f"Has ganado {puntosNuevos} puntos! En total, acumulas {puntosTotales} puntos")

# Ejercicio 37
puntosAnteriores = 4582
puntosNuevos = 235

print(f"Has ganado {puntosNuevos} puntos! En total, acumulas {puntosAnteriores + puntosNuevos} puntos")
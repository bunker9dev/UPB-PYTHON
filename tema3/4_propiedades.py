# Los string son inmutables 

nombre = "carina" 

nombre = "Karina" 


print(nombre)

# Los string se pueden concatenar
n1 = "kari"
n2 = "na"

print(n1+n2)


# Los string se pueden multiplicar

print( "la" *5)


# Los string pueden ser multilineales sin utilizar \n

poema = """Detrás de un salmón
nada un tiburón,
lo caza en Alaska
cansados los dos. """

print(poema)

# Los string se puede verificar si contiene alguna palabra dentro del string

poema = """Detrás de un salmón
nada un tiburón,
lo caza en Alaska
cansados los dos. """

print("Alaska" in poema)


# Los string se puede calcular el largo del string

poema = """Detrás de un salmón
nada un tiburón,
lo caza en Alaska
cansados los dos. """

print(len(poema))


# Ejercicio 54

prueba1 = "Repetición"
print(prueba1 * 15)



# Ejercicio 55

prueba2 = """Asustado grita:
¡Nooo!, por favor,
mi vida es muy corta
¡Muestra compasión! """
print("muestra" not in prueba2)

# Ejercicio 56

prueba3 = "esternocleidomastoideo"
print(len(prueba3))


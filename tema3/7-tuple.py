
miTuple =  (1,2,3,4)

print(miTuple)
print(type(miTuple))

# puede contener datos de cualquier tipo

miTuple2 = (1,"hola", 0.5, ["a", "b", "c"] , {"color" : "negro", "edad" : 34} )

print(miTuple2)
print(type(miTuple2))

# averiguar que elemento esta en x indice
miTuple =  (1,2,3,4)

print(miTuple[-2])

# no se puede asignar o cambiar item
miTuple =  (1,2,3,4)

# se puede anidar tuples

miTuple2 = (1,"hola", 0.5, ["a", "b", "c"] , (10, 20, 30, 40), {"color" : "negro", "edad" : 34} )

print(miTuple2)
print(miTuple2[4])

# realizar casting con tuples
miTuple2 = tuple(miTuple2)
print(miTuple2)

# asignar valores a igual cantidad de variables

t = (1, 2, 3)
x,y,z = t

print(y)

#contar cuantass veces hay un elemento en en tuple
t = (1, 2, 3, 1)

print(t.count(1)) # debemos colcar el terminio que vamos a buscar
print(t.index(2)) #inidcar en que indice esta el elemeto a buscar


# ejercicio 63

dato1 = ( 2,   5,   2,   3,   5,   3,   5,   5,   3,   -5 ,  43,   2)

resultado = (dato1.count(5))
print(resultado)



# ejercicio 64

dato2 = ( 2,   5,   2,   3,   5,   3,   5,   5,   3,   -5 ,  43,   2)

print(dato2)
print(type(dato2))

miLista = list(dato2)

print(miLista)
print(type(miLista))

# ejercicio 65

dato3= (1, 2, 3, 4)

a,b,c,d = dato3

print(a,b,c,d )


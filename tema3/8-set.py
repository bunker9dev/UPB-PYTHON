''' 
miSet = set ((1,2,3,4,5))

print(type(miSet))
print(miSet)


# empleando {}

miSet2 = { 1, 2, 3}

print(type(miSet2))
print(miSet2)

# no se puede realizar
# miSet2[2] = 5


# colocando datos repetidos

miSet3 = { 1, 2, 3, 4, 5, 1, 2, 4, 3, 2, 1, }

print(miSet3)

# empelando tipos de daos

# no set
miSet3 = { "A", "B", 3.5, 4.8, True, False, (2, 4, 3, 2), 1 }

print(type(miSet3))
print(miSet3)



# relizar el conteo de cantidad e elementos
miSet3 = { "A", "B", 3.5, 4.8, True, False, (2, 4, 3, 2), 1 } 

print(len(miSet3))


# averiguar si un elemento esta dentro de mi set

print(2 in miSet3)

#unir dos set 
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# Agregar elementos a un set

s1 = {1,2,3}
print(s1)

s1.add(2)
print(s1)

# Eliminar un elemento del set
s1 = { 4, 7, "hola" }
print(s1)

s1.discard("hola")
print(s1)

# Eliminar aleatoriamente 
s1 = { 4, 7, "hola" }
print(s1)

s1.clear()
print(s1)
'''
# EJERCICIO 66

miSet1 = {1, 2, "tres", "cuatro"}
miSet2 = {"tres", 4, 5} 
miSet3 = miSet1.union(miSet2)
print(miSet3)

# EJERCICIO 67
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
eliminado = sorteo.pop()

print(sorteo)
print(eliminado)

# ejercicio 68
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}

sorteo.add("Arturo")

print(sorteo)
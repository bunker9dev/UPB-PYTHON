# Listas

miLista = ["a", "b", "c"]

miLista2 = ["hola" , 234, [True, "Clase", -45.85] ]


''' 

print(type(miLista))

print(type(miLista2))

print(len(miLista2))

# index

resultado = miLista2[0:2]

print (resultado)

# concatenacione de listas
miLista3 = ["d", "e", "f", "g", "h", "i"]
print(miLista + miLista3)
print(miLista )
print(miLista3 )

miLista4 = miLista + miLista3
print(miLista4)

#hay cosas que los styring no pueden hacer que las listas si, como alterar sus elementos

print(miLista)

miLista[0] = "alfa"

print(miLista)




# agregar elemento a las listas 
miLista3.append("j")

print(miLista3)



print("===========================================\n")
#ELimiiiiinar elementos de la lista
print(miLista3 )

elimniando = miLista3.pop(0)

print(miLista3 )

print(elimniando)



print("===========================================\n")
# ordenar listas 

listaAlf = ["g" , "t" , "b", "k", "o", "l", "a", "z"]

listAlf2 = ["c", "d", "e" , "f", "h"]
print (listaAlf)

listaAlf.sort()

print (listaAlf +listAlf2)


#orden inverso
listaAlf.reverse()
print (listaAlf)

'''

# Ejercicio 57

miLista = ["hola", 3, ["rojo", "negro"], -87, True]

print(miLista)
print("===========================================\n")

# Ejercicio 58

mediosTransporte = ["carro", "avión", "barco", "bicicleta"]

mediosTransporte.append("motocicleta")
print(mediosTransporte)

print("===========================================\n")

# Ejercicio 59

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
print(frutas)
eliminado = frutas.pop(2)
print(frutas)
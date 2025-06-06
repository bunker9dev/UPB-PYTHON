# cuantas veces aparece la letra a en la palabra banana

palabra = "banana"
contador = 0

for letra in palabra:
    if letra == "a":
        contador += 1

print("La letra 'a' aparece", contador, "veces.")


libros = {
    "Ana": "El Principito",
    "Luis": "Cien Años de Soledad",
    "María": "1984"
}

# Y quieres imprimir quién tiene qué libro, :

for nombre, titulo in libros.items():
    print(f"{nombre} tiene el libro '{titulo}'")


colores = {"obj1": "rojo", "obj2": "azul", "obj3": "rojo", "obj4": "verde"}
frecuencia = {}  # inicializamos un nuevo diccionario

for color in colores.values():   # Recorre solo los valores del diccionario
    if color in frecuencia:      # Si el color ya está en el diccionario frecuencia
        frecuencia[color] += 1   # ...incrementa su contador
    else:
        frecuencia[color] = 1   # ...si no, lo inicializa en 1

print(frecuencia)


lista = [1,2,3,4,]

cantidad = len(lista)
print(cantidad)
''' 
lista = ['a' , 'b' , 'c']

for letras in lista:
    print (letras)

#concatenar

for letras in lista:
    print ("letra : " + letras)

#ubicar el index

for letras in lista:
    numero_letra = lista.index(letras) + 1
    print (f"Letra {numero_letra} : {letras}")

#anidar un for con un if

lista2 = ["Antonio", "Laura", "Pedro",  "Andres", "Luis"]

for nombre in lista2:
    if nombre.startswith("A"):
        print(nombre)
    else:
        print ("El nombre no empieza por A")


# Importancia de la indentacion dentro del for

numeros = [1,2,3,4,5]
miValor = 0

for num in numeros:
    miValor = miValor + num
    print(miValor)

# Iterar en string
palabra = "Python es genial "

for letra in palabra:
    print(letra)

# hacer loop sopbre string sin utilizar variables 

for letra2 in "esto es otra forma":
    print(letra2)

# Iterar en una lista que contenga listas 
for a , b in [[1,2] , [3,4], [5,6] ] :
    print (a)
   

# Iterar dentro de un diccionario 
dicc = { "dato1" : 1 ,  "dato2" : 2 ,  "dato3" : 3 ,  "dato4" : 4 ,}

for item in dicc.items():
    print(item)

for a , b  in dicc.items():
    print(a, b)

 

# Sumar valores de un diccionario

ventas = {"enero": 1500, "febrero": 1800, "marzo": 1700}
total = 0

for valor in ventas.values():
    total += valor

print(f"Total ventas: {total}")




# Contar cuántas veces aparece cada letra en una palabra

palabra = "banana"
frecuencia = {}

for letra in palabra:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1

print(frecuencia)

   '''
# Filtrar elementos con valores mayores a un umbral
# indicar que estudiantes aprobaron la materia y el valor de la nota

notas = {"Juan": 4.5, "Ana": 2.8, "Luis": 3.9}

for estudiante, nota in notas.items():
    if nota >= 3.5:
        print(f"{estudiante} aprobó con {nota}")


# Contar cuántas personas hay por ciudad

personas = [
    {"nombre": "Ana", "ciudad": "Cali"},
    {"nombre": "Luis", "ciudad": "Bogotá"},
    {"nombre": "Marta", "ciudad": "Cali"}
]

conteo_ciudades = {}

for persona in personas:
    ciudad = persona["ciudad"]
    conteo_ciudades[ciudad] = conteo_ciudades.get(ciudad, 0) + 1

print(conteo_ciudades)

# Crear un diccionario de conteo de palabras

frase = "hola mundo hola mundo mundo"
palabras = frase.split() #split separa palabras
conteo = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)


# ejercicio 81

alumnos = ["Martha", "Pedro", "Juan", "Juanita", "Isabel", "Tomas", "Manuel", "Gloria", "Luz", "Carlos"]

for nombre in alumnos:
    print("Hola " + nombre )

print("\n")
# ejercicio 82

listaNumeros = [ 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
sumaNumeros = 0

for num in listaNumeros:
    sumaNumeros = sumaNumeros + num
print(sumaNumeros)

print("\n")
# ejercicio 83

listaNumeros = [ 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

sumaPar = 0
sumaImpar = 0

for num in listaNumeros:

    if num %2 == 0 :
        print(num)
        sumaPar = sumaPar + num
    else:
        sumaImpar = sumaImpar + num
print(f"la suma de los numeros pares es: {sumaPar}")
print(f"la suma de los numeros impares es: {sumaImpar}")


# Contar del 1 al 10

i = 1
while i <= 10:
    print(i)
    i += 1


# Contar hacia atrás del 10 al 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# Imprimir solo números pares del 1 al 20
i = 2
while i <= 20:
    print(i)
    i += 2

# Sumar los primeros 10 números naturales
i = 1
suma = 0
while i <= 10:
    suma += i
    i += 1
print("Suma:", suma)


# Leer números hasta que el usuario escriba 0

n = int(input("Ingresa un número (0 para salir): "))
while n != 0:
    print("Ingresaste:", n)
    n = int(input("Ingresa otro número (0 para salir): "))

# Adivinar un número secreto

secreto = 4
adivina = int(input("Adivina el número (entre 1 y 10): "))
while adivina != secreto:
    adivina = int(input("Incorrecto. Intenta otra vez: "))
print("¡Correcto!")


# Mostrar el menú hasta que el usuario elija salir

opcion = ""
while opcion != "4":
    print("1. Ver productos\n2. Comprar\n3. Ayuda\n4. Salir")
    opcion = input("Elige una opción: ")

# Pedir la contraseña hasta que sea correcta

clave = ""
while clave != "python123":
    clave = input("Introduce la contraseña: ")
print("¡Acceso concedido!")

# Contar cuántos números introduce el usuario hasta que digite -1

contador = 0
n = int(input("Ingresa un número (-1 para salir): "))
while n != -1:
    contador += 1
    n = int(input("Ingresa otro número (-1 para salir): "))
print("Ingresaste", contador, "números.")

# Tabla de multiplicar de un número

n = int(input("Tabla del número: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1


#  Contar cifras de un número

num = int(input("Número: "))
contador = 0
while num != 0:
    num //= 10 #cociente (division al piso) divide pir diez, va eliminando un numero
    contador += 1
print("Cantidad de cifras:", contador)

# Validar entrada hasta que esté en un rango

edad = int(input("Edad (10-50): "))
while edad < 10 or edad > 50:
    edad = int(input("Edad inválida. Intenta de nuevo: "))
print("Edad registrada:", edad)


# Cajero automático (retiro de dinero)
# Problema: Un usuario intenta retirar dinero, 
# pero no puede retirar más de lo que tiene. 
# El programa debe impedirlo hasta que ingrese 
# un valor válido.

saldo = 500000  # Saldo inicial

print("=== Cajero Automático ===")
print(f"Tu saldo es: ${saldo}")

retiro = int(input("¿Cuánto deseas retirar?: "))

while retiro > saldo:
    print("Fondos insuficientes.")
    retiro = int(input("Intenta con otro valor: "))

saldo -= retiro
print(f"Retiro exitoso. Saldo restante: ${saldo}")

# Lista de compras
# Problema: El usuario va agregando productos a una 
# lista hasta que escribe “fin”. 
# Luego se muestran todos los productos.
print("=== Lista de compras ===")
producto = input("Agrega un producto (escribe 'fin' para terminar): ")

lista = []

while producto.lower() != "fin":
    lista.append(producto)
    producto = input("Agrega otro producto (o 'fin'): ")

print("Productos en tu lista:")
for item in lista:
    print("-", item)
''' 
moneda = 10

while moneda > 0:
    print(f"tengo {moneda} monedas")
    moneda -= 1
else:
    print ( "Ya no hay mas monedas")


respuesta  = "s"
while respuesta == "s":
    respuesta = input( "quieres seguir? (s/ n)")
else:
    print("GRACIAS")



respuesta  = "s"
while respuesta == "s":

    pass

print("Buenas tardes medellin")

# BREAK
palabra = input( "escriba una palabra ")

for letra in palabra:

    if letra == "k":
        break
    print(letra)

    # CONTINUE
palabra = input( "escriba una palabra ")

for letra in palabra:

    if letra == "k":
        continue
    print(letra)


# Ejercicio 84

numero = 50

while numero >= 20:
    print(numero)
    numero -= 1


# Ejercicio 85

numero = 1000

while numero >= 900:
    if numero % 10 == 0:
        print(numero)
    numero -= 1


# Ejercicio 86

lista = [ 2,3,5,6,7,8,11,12,]
for num in lista:
    if num % 3 != 0:
        print(num)
    else:
        break

 
    # Ejercicio 87

num = 253

while num < 302:
     
    print(num)
    num +=4 
        
   
   '''
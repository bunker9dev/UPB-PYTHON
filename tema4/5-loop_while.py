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

    '''
    # Ejercicio 87

num = 253

while num < 302:
     
    print(num)
    num +=4 
        
       

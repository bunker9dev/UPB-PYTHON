#control de flujos
'''
# if

# Ejercicios Guiados
# Ejercicio No 1
a = 123
b = 56
if b < a :
   print (" b es menor que a")

# Ejercicio No 2
if True:
    print("imprime verdadero")


# Ejercicio No 3
disponible = True
if disponible:
    print("Disponible es verdadero")


# Ejercicio No 4
if False:
    print("imprime verdadero") #no imprime nada


# Ejercicio No 5
t = 586
l = 5645/ 85

if t >  l :
    print("podemos avanzar")


# Ejercicio No 6
i = 345
j = 345

if i == j :
    print("las dos varibles son iguales ")


# Ejercicio No 7

if 345 == 345 :
    print("los dos valores son iguales ")

# Ejercicio No 8

if 81 ** 0.5 == 9 :
    print("los dos valores son iguales ")


# Ejercicio No 9
i = 10
j = 20

if i + j == 30:
    print(f" {i} + {j} = 30")



# Ejercicio No 10
i = "Upb"
j = "Upb"

if i == j:
    print(f"Universidad Pontificia Bolivariana")

# Ejercicio No 11
i = 345
k = 245 + 110

if i == k :
    print("La operacion es correcta")


# Ejercicio No 12
i = "Upb"
j = "upb"

if i == j:
    print(f"Universidad Pontificia Bolivariana")



# Ejercicios para ser desarrollado por los estudiantes

# Ejercicio No 13
# Verifique si la raiz cuadrada de 213.16 es igual 14.6 si es verdadero, imprimir "la raiz cuadrada de 213.16 es igual 14.6"

#solucion
if 213.16 ** 0.5 == 14.6 :
    print("la raiz cuadrada de 213.16 es igual 14.6")

# Ejercicio No 14

# compare si la cantidad de letra que hay en la palabra " Software" es igual a la catidad e letra que hay en la palabra "programa"

letra1 = "software"
letra2 = "programa"

if len(letra1) == len(letra2) :
    print (f"la palabra {letra1} y {letra2} tienen la misma cantidad de letras")
    print ("la palabra " + letra1 + " y " + letra2 + " tienen la misma cantidad de letras")



# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================

# ELSE

# Ejercicio No 15
i = "Upb"
j = "upb"

if i == j:
    print(f"Universidad Pontificia Bolivariana")
else:
    print(f"Las palabras {i} y {j} son diferentes")


# Ejercicio No 16
i = "Upb"
j = "upb"

if i == j:
    print(f"Universidad Pontificia Bolivariana")
else:
    print(f"Las variables {i} y {j} son diferentes")
    j = "Upb"
    i = 34 + 56
    sede = "Laureles"


# Ejercicio No 17
multi =  45 * 8
suma = 485 +78

if multi > suma :
    print (f"""EL resultado de la multiplicacion es: {multi}
EL resultado de la suma es: {suma}
el valor del resultado de la multiplicacion es mayor al resultado de la suma""")

else:
    print (f"""EL resultado de la multiplicacion es: {multi}
EL resultado de la suma es: {suma}
el valor del resultado de la suma es mayor al resultado de la multiplicacion """)



# Ejercicios para ser desarrollado por los estudiantes

# Ejercicio No 18
# preguntar al usuario cuantos años tiene y almacenar la informacion en una varibale.
# hacer un programa que le indique si puede ingresar a la discoteca por ser mayor de edad(18 años)
# si es mayor de edad debe aparecer el siguiente menssaje: Puedes ingresar a la discoteca, "BIENVENIDOS". Incluyendo las comillas
# si no puede ingresar, decirle cuantos años le faltan para poder ingresar y salier el siguente mensaje

edad = int(input("cuantos años tienes? "))

if edad >= 18 :
    print('Puedes ingresar a la discoteca, "BIENVENIDOS"')
else:
    print(f'lo sentimos no puedes ingresar, te faltan {18 - edad} años ')


# Ejercicio No 19

# Mostar al usuario el siguiente mensaje:
#
# escriba v si es verdadero
# escriba f si es falso
# pregunta:
# los datos booleanos pueden tener los siguientes valores?:}
# True, False  y None


print ("""escribra V si es verdadero
escriba F si es falso

pregunta:
los datos booleanos pueden tener los siguientes valores?

True, False  y None
""")

respuesta = input("escriba su respuesta: ").lower()


if respuesta == "f":
    print("Felicitaciones, Respuesta correcta\n")
else:
    print(" Fallaste, solo pueden tener dos valores True o False \n")



# =============================================================================================
# =============================================================================================
# =============================================================================================
# =============================================================================================

# ELIF


# Ejercicio No 20
respuesta = input("escriba su respuesta: ").lower()

if respuesta == "f":
    print("Felicitaciones, Respuesta correcta\n")
elif respuesta == "v":
    print(" Fallaste, solo pueden tener dos valores True o False \n")
else:
    print("Respuesta no valida \n")



# Ejercicio No 21
# Hacer un menu donde se indique un numero y ese numero este relacionado a una materia
# 1 matematicas
# 2 sociales
# 3 ingles
# 4 Programacion

# pedirle al usuario ingrese un numero y cuando ingrese el numero aparezca en pantalla que materia seleccionaste


print("""\n MENU

INGRESE UN NUMERO PARA SELECCIONAR UNA MATERIA

1- MATEMATICAS
2- SOCIALES
3- TECNOLOGIA
4- INGLES
      """)

seleccion  = int(input ("Ingrese un numero: " ))


if seleccion == 1:
   print('Escogiste Matematicas')
elif seleccion == 2:
    print('Escogiste Sociales')
elif seleccion == 3:
    print('Escogiste Tecnologia')
elif seleccion == 4:
    print('Escogiste Ingles')
else:
    print('Dato no valido')


# Ejercicio No 22
# Pedirle al usuario que ingrese un numero y decir si ese nuemero es psotivo, negativo o es igual a cero

numero = float(input("Ingresa un número: "))

if numero > 0:
        print("El número es positivo.")

elif numero < 0:
        print("El número es negativo.")
else:
        print("El número es cero.")


'''
# EJERCICIO PARA DESARROLLAR EL ESTUDIANTE

# Ejercicio No 23 
# calcular el valor final de una factura si el cliente acepta adicionar la propina o no
# (valor de la propina 10%)
# debes de ingresar el valor de la venta y preguntar si incluyen el servicio si(S) o No(N)
# si incluye el servicio indicar cuanto seria el pago total
# y si no incluye la propina indicar el valor de la factura
# si escribe otro dato indicar que es una respuesta errónea


factura = int(input("INGRESE EL VALOR DEL SERVICIO: "))
propina = input("ADICIONAMOS EL SERVICIO SI(S) NO(N): ").lower()

if propina == "s":
     print(f"EL valor total de la factura es {factura + (factura*0.1)}")
elif propina == "N":
     print(f"EL valor total de la factura es {factura}")
else: 
     print(f"{propina} No es una respuesta correcta" )
    


# Ejercicio No 24
#	indicar si el número es menor o igual  a cero
# indicar si el número es mayor a cero y menor o igual a 10
# indicar si el número es mayor a 10 y menor o igual a 20
# indicar si el número es mayor a 20 y menor o igual a 30
# indicar si el número es mayor a 30


numero = int (input("ingrese un numero: "))

if numero <= 0:
     print(f"numero {numero} es menor o igual  a cero")
elif numero > 0 and numero <= 10 :
     print(f"numero {numero} es mayor a cero y menor o igual a 10")
elif numero > 10 and numero <= 20 :
     print(f"numero {numero} es mayor a 10 y menor o igual a 20")
elif numero > 20 and numero <= 30 :
     print(f"numero {numero} es mayor a 20 y menor o igual a 30")
else:
      print(f"numero {numero} es mayor a 30 ")


# Ejercicio No 25

# Crea un programa que le pida al usuario una moneda destino (USD, EUR o JPY) 
# y convierta un monto ingresado desde pesos colombianos (COP) a la moneda 
# seleccionada usando tasas predefinidas guardadas en un diccionario.

# Usar un diccionario para las tasas de conversión.
# Usar if, elif, else para manejar las opciones de moneda.
# Si el usuario escribe una moneda no válida, mostrar un mensaje de error.

tasas = {
    "USD": 0.00025,   # 1 COP = 0.00025 USD
    "EUR": 0.00021,   # 1 COP = 0.00021 EUR
    "JPY": 0.035      # 1 COP = 0.036 JPY
}

pesoCol = float(input("ingrese un valor en pesos Colombianos (COP: "))

cambio = input("¿A qué moneda desea convertir?  escriba (USD, EUR, JPY): ").upper()

if cambio == "USD":
     valor = pesoCol * tasas["USD"]
     print(f" el cambio de ${pesoCol} a Dolares es {valor:2f}USD")
elif cambio == "EUR":
     valor = pesoCol * tasas["EUR"]
     print(f" el cambio de ${pesoCol} a Euros es {valor:2f}EUR")
elif cambio == "JPY":
     valor = pesoCol * tasas["JPY"]
     print(f" el cambio de ${pesoCol} a yens {valor:2f}JPY")
else:
     print("Has ingresado un dato erroneo")
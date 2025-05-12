#control de flujos 

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
   




''' 
# Evaluar si es mayor de edad para que pueda ingresar a la discoteca 
edad = int(input("Ingrese su edad"))
if edad >= 18:
    print("puedes ingresar a la discotek")
else:
    print("Eres menor de edad, no puedes ingresar")
 

#  evalUar si la nota es mayor o igual a 3.5 indica que aprobo la materia
nota = float(input("Ingrese su nota"))
if nota >= 3.5:
	print("apobaste la materia")
else:
    print("Lo siento reprobaste la nota")




 
''' 
materia = 'Matematicas'
nota = 3.5

if materia == 'Matematicas':
   print('Te gusta Matematicas ')
elif materia == 'sociales':
   print('Te gusta sociales ')
else:
   print('No se que materia te gusta')

'''
numero = float(input("Ingresa un número: "))
if numero > 0:
        print("El número es positivo.")
    
elif numero < 0:
        print("El número es negativo.")
else:
        print("El número es cero.")


edad = 16
calificacion = 3.1

if edad < 18:
   print('Eres menor de edad')
   if calificacion >= 3:
      print('Aprobo la materia')
   else:
      print('Reprobo la materia')
else:
   print('eres adulto')


# ejercicio No 77

num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

# ejercicio No 78
# solucion 1

edad = int(input("ingrese la edad "))
tiene_licencia = input( "ingrese s si tiene licencia, ingrese n si no tiene licencia ").lower()

if edad >= 18 :
    if tiene_licencia == "s":
        print("puede Conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

# Una línea de declaración if else:
a = 2
b = 330
print("A") if a > b else print("B")

# Prueba si aes mayor que b, Y si c es mayor que a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("ambas condiciones son verdaderas")



# ejercicio No 78
    # solucion 2

edad = int(input("ingrese la edad "))

if edad < 18 :
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    
else:
    tiene_licencia =  input( "ingrese s si tiene licencia, ingrese n si no tiene licencia ").lower()
    if tiene_licencia == "s":
        print("puede Conducir")
    else:
        print("No puedes conducir. Necesitas contar con una licencia")

# ejercicio No 78
# solucion3
edad = int(input("ingrese la edad "))
tiene_licencia = input( "ingrese s si tiene licencia, ingrese n si no tiene licencia ").lower()

if edad >= 18 and tiene_licencia == "s":
    print("Puedes conducir")

elif edad >= 18 and tiene_licencia != "s":
    print("No puedes conducir. Necesitas contar con una licencia")

else:
    print ("No puedes conducir aún. Debes tener 18 años y contar con una licencia")





# ejercicio No 79

hablaIngles = True
sabePython = False

if hablaIngles == True and sabePython == True:
    print("Cumples con los requisitos para postularte")
elif hablaIngles == False and sabePython == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif hablaIngles == True and sabePython == False:
    print("Para postularte, necesitas saber programar en Python")

else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    


    # ejercicio No 80

usuarioOK = "python"
claveOk = "upb123"

usuario = input("Ingresa el usuario:")
clave = input("Ingresa la clave:")

if usuarioOK == usuario and claveOk == clave:
    print("Bienvenido")
elif usuarioOK != usuario and claveOk == clave:
    print("usuario incorrecto ")
elif usuarioOK == usuario and claveOk != clave:
    print("clave incorrecta ")
else:
     print("cuenta bloqueada")

'''
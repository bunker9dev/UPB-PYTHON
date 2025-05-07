#control de flujos

if True :
    print("es correcto")



x = True
if x:
    print ('Es Correcto')

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

if 5 == 2:
  print ('Es Correcto')
else:
   print('No es correcto')


mascota = 'Perro'

if mascota == 'gato':
   print('tienes un gato ')
elif mascota == 'Perro':
    print('tienes un perro ')
else:
   print('No se que animal tienes')


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

'''
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

''' 




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
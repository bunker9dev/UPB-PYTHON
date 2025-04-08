

# diccionario = { "c1" :  "valor1" , "c1" : "valor2"  }

# print(diccionario)

# print(type(diccionario))

'''  
cliente = { "nomnbre" : "Andres",
           "apellido" : "lozano",
           "edad":  16,
           "barrio" : "castilla",
           "estatura" : 56.6,
           "disponible" : True }
consulta = cliente["apellido"]

print(consulta)




midicc = {"dato1" : "hola",
          "dato2" : ["a", "b", "c",],
          "dato3" : ["d", "e", "f"],
          "dato4" : {"color" : "rojo", "vehiculo" : "carro", "puestos" : 7} }

print(midicc)

# busqueda dentro de diccionario

print(midicc["dato4"]["vehiculo"])

print(midicc["dato4"]["color"].upper())

diccNuevo = { 1: "a", 2: "b", 3:"c"}
print(diccNuevo)

# adicionar elemento al diccionario
diccNuevo[4] = "d"
print(diccNuevo)


# sobreescribir elemento de un diccionario

diccNuevo[2] = "B"
print(diccNuevo)

# trtaer todas las claves de un diccionario
print( diccNuevo.keys() )

# trtaer todas los valores  de un diccionario
print( diccNuevo.values() )

# mostrar todos los elementos de un diccionario
print(diccNuevo.items())


'''

# Ejercicio 60

miDic = {"nombre"	: 	"Fernando",
         "apellido"	: 	"Gómez",
         "edad"		: 	15,
         "ocupación"	: 	"Estudiante"
         }

print(miDic)
print(type(miDic))


# Ejercicio 61

miDict2 = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(miDict2["puntos"]["points2"][1])


# Ejercicio 62

miDic = {"nombre"	: 	"Fernando",
         "apellido"	: 	"Gómez",
         "edad"		: 	15,
         "ocupación"	: 	"Estudiante"
         }

print(miDic)

miDic["edad"] = 16
miDic["ocupación"] = "Estudiante Decimo"
miDic["materia"] = "programación"


print(miDic)

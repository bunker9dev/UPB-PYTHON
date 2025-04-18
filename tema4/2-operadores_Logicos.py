# operadores de comparacion
''' 
miBool = 4 > 5 < 6

print(miBool)


# utilizamos los operadores logicos 

miBool2 = 4 > 5 and 5 < 6
print(miBool2)

miBool3 = (5 == 3+2) and (5 < 6)
print(miBool3)

miBool4 = (5 == 6-1) and ("cinco" == "cinco")
print(miBool4)

miBool5 = 3 == 34 or 4 == 43
print(miBool5)

texto = "aprender Ptyhon es facil"

miBool6 =("aprender" in texto) or ("java" in texto)
print(miBool6)

miBool7 = not 345 == 345
print(miBool7)

''' 

# Ejercicio 74

num1 = 345
num2 = 987 / 34
num3 = 234

resultado1 = (num1 > num2) and num1 < num3
print (resultado1)
print(type(resultado1))


# Ejercicio 75

num1 = 345
num2 = 987 / 34
num3 = 234

resultado2 = (num1 > num2) or num1 < num3
print (resultado2)
print(type(resultado2))


# Ejercicio 76

palabra1 = "industria"
palabra2 = "digitales"

frase = "El mundo tecnológico, la industria del software y los servicios digitales están en constante desarrollo y crecimiento"

resultado3 = not (palabra1 in frase) and (palabra2 in frase)

print (resultado3)
print(type(resultado3))

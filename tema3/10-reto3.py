#Reto 3
texto = input("ingrese un texto: ").lower()

print("\n") # ingresar letras 

print("por favor Ingrese tres letras, una por una")
letra1 = input("ingrese la primera letra: ".lower())
letra2 = input("ingrese la segunda letra: ".lower())
letra3 = input("ingrese la tercera letra: ".lower())

print(f"usted ha ingresado las siguentes letras {letra1}, {letra2} y {letra3}")

texto2 = tuple(texto) #pasamos el texto a lista

print("\nRespuesta 1")

contador1 = texto2.count(letra1)
contador2 = texto2.count(letra2)
contador3 = texto2.count(letra3)

print(f"la letra {letra1} estan {contador1} veces dentro tu texto")
print(f"la letra {letra2} estan {contador2} veces dentro tu texto")
print(f"la letra {letra3} estan {contador3} veces dentro tu texto")

print("\nRespuesta 2")

palabras = texto.split(" ")
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\nRespuesta 3")

print(f' la primera letra del texto es la letra "{texto[0]}" y la ultima letra del texto es la letra "{texto[-1]}"')

print("\nRespuesta 4")

texto3 = palabras[::-1]
print(texto3)

print("\nRespuesta 5")


print(f'La Palabra "python" se encuentra en el texto? la respuesta es: {"python" in texto}')


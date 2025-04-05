
texto = "Este es el TEXTO de Antonio"

resultado = texto.replace("e", "x") # primer argumento, el texto que yo quiero 
                                    #reemplazar y el segundo arguamento es que palabra la voy a cambiar 

print(resultado)

# Ejercicio 51
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
prueba1 = frase.upper()
print(prueba1)

# Ejercicio 52
lista_palabras = ["La","legibilidad","cuenta."]
prueba2 = " ".join(lista_palabras)
print(prueba2)

# Ejercicio 53
frase1 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase2 = frase1.replace("difícil","fácil")
frase3 = frase2.replace("mala","buena")
print(frase3)
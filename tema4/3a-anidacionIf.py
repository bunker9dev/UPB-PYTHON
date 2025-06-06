# Explicacion No 1
hora = int(input("Introduce la hora (0-23): "))

if hora < 12:
    print("Buenos días")
    if hora < 6:
        print("¡Es muy temprano!")


# Explicacion No 2

temp = float(input("Temperatura en °C: "))

if temp > 30:
    print("Hace calor")
    if temp > 40:
        print("¡Cuidado! Temperatura peligrosa")


# Explicacion No 3

vidas = int(input("Vidas restantes: "))

if vidas > 0:
    print("Puedes seguir jugando")
    if vidas == 1:
        print("¡Última vida!")
else:
    print("Game Over")
    


# Ejercicio No 33
# Pide la edad del usuario. Si es menor de 18, 
# pregunta si tiene permiso de sus padres. 
# Si tiene permiso, muestra "Acceso permitido con permiso", 
# si no, "Acceso denegado". 
# Si es mayor o igual a 18, muestra "Acceso permitido".

edad = int(input("Introduce tu edad: "))

if edad < 18:
    permiso = input("¿Tienes permiso de tus padres? (s/n): ").lower()
    if permiso == "s":
        print("Acceso permitido con permiso")
    else:
        print("Acceso denegado")
else:
    print("Acceso permitido")

# Ejercicio No 34
# Solicita nombre de usuario. Si es "admin",
# pide la contraseña. Si la contraseña es "UPB", 
# muestra "Acceso completo". Si no, muestra "Contraseña incorrecta". 
# Si no es "admin", muestra "Usuario no autorizado".

usuario = input("Usuario: ").lower()

if usuario == "admin":
    clave = input("Introduce la contraseña: ")
    if clave == "UPB":
        print("Acceso completo")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no autorizado")
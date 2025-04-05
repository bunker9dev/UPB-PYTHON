# conversiones implicitas

# comentario en bloque ''' '''
''' 
num1 = 40
num2 = 15.5


num1 = num1 + num2

print(type(num1))
print(type(num2))

'''
# conversiones Explicitas
''' 
num1 = 4.7

print(num1)
print(type(num1))

num2 = int(num1)

print(num2)
print(type(num2))

'''
''' 
edad = input ("dime tu edad ")

print ("tu edad es: " + edad)
print(type(edad))

edad = int(edad)
print(type(edad))
nuevaEdad = edad + 1

print( "felicitaciones ahoras tienes" , nuevaEdad, "45 años")

'''
num1 = "24.89"
num2 = "45"

print(float(num1) + float(num2))
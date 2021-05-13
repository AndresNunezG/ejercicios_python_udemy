"""
Ejercicio 19.
    - Escribir una función lambda que indique si el usuario es mayor de edad
    - Escribir una función lambda que indique si un número es par o impar
"""

#### ITEM 1 ####
#Solicitad la edad y salir del programa si la entrada no es un entero
try:
    edad = int(input('Ingrese su edad: '))
except:
    print('Ingrese una edad válida')
    exit() 

#Crear función para verificar si es mayor de edad o no
#Usando una función anónima lambda para determinar el mensaje
mayor_edad = lambda edad: 'mayor de edad' if edad >= 18 else 'menor de edad'

print(f'El usuario con edad: {edad} es {mayor_edad(edad)}')

#### ITEM 2 ####
#Solicitar número
#Solicitad el número y salir del programa si la entrada no es un número
try:
    num = float(input('Ingrese un número: '))
except:
    print('Ingrese un número válido')
    exit() 

#Crear función para verificar si un número es par o impar
num_par = lambda num: 'par' if num % 2 == 0 else 'impar'

print(f'El número ingresado: {num} es {num_par(num)}')
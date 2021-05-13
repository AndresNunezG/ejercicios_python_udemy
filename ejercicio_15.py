"""
Ejercicio 15.
    - Solicitar dos números al usuario
    - Multiplicar dos números sin usar el símbolo de multiplicació '*'
    - Mostrar el resultado por pantalla
"""

#Solicitar los números al usuario
num_a = int(input('Ingrese el primer número: '))
num_b = int(input('Ingrese el segundo número: '))

#validar los signos de los números
if (num_a < 0 and num_b > 0) or (num_a > 0 and num_b < 0) or (num_a < 0 and num_b < 0):
    signo = True #habilitar la bandera para cambiar signo
    num_a = abs(num_a) #valor absoluto del número num_a
    num_b = abs(num_b) #valor absoluto del número num_b
else:
    signo = False #deshabilitar para mantener signo

#Multiplicar a * b
res = 0 #inicializar resultado en 0
for i in range(1, num_b + 1):
    res += num_a

if signo:
    res *= -1

#Mostrar resultado en pantalla
print(f'El resultado de la multiplicación {num_a} * {num_b} es igual a: {res}')
"""
Ejercicio 4.
    - Pedir dos (2) números al usuario
    - Hacer todas las operaciones básicas matemáticas
    - Mostrar el resultado en pantalla
"""

#Solicitar numeros al usuario
num_a = int(input('Ingrese el primer número: '))
num_b = int(input('Ingrese el segundo número: '))
 
#Operaciones básicas
suma = num_a + num_b
resta = num_a - num_b
mult = num_a * num_b

try:
    division = num_a / num_b
except:
    division = 'División entre 0 inválida'

print(f'La suma de {num_a} + {num_b} es: {suma}')
print(f'La resta de {num_a} - {num_b} es: {resta}')
print(f'El producto de {num_a} * {num_b} es: {mult}')
print(f'La division de {num_a} / {num_b} es: {division}')
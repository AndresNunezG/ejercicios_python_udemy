"""
Ejercicio 7.
    - Solicitar un rango de números al usuario
    - Mostrar en pantalla todos los números impares del rango
"""

#Solicitar rango
print('Definir rango.')
num_inicio = int(input('Ingrese el inicio del rango: '))
num_final = int(input('Ingrese el final del rango: '))
print('\n')

if num_inicio >= num_final:
    print(f'el rango introducido: [{num_inicio}, {num_final}], no es válido' )
    exit()

#Determinar números impares en el rango
print(f'Los números impares en el rango [{num_inicio}, {num_final}] son: ')
for i in range(num_inicio, num_final + 1):
    if i % 2 != 0:
        print(str(i) + ', ', end = '')
print('\n')

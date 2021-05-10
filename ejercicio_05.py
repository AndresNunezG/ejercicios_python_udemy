"""
Ejercicio 5.
    - Solicitar un rango de números al usuario (a, b)
    - Mostrar en pantalla los números que pertencen al rango
"""

#Solicitar rango
print('Ingrese el rango.')
num_inicio = int(input('Ingrese el número de inicio: '))
num_final = int(input('Ingrese el número final: '))

#Obtener números intermedios y mostrar en patalla
print('\n')
print(f'El rango seleccionado es [{num_inicio}, {num_final}]')
print('Los numeros entre el rango son:')

if num_inicio >= num_final:
    print(f'[{num_inicio}, {num_final}]: Rango no válido')
    print(f'El inicio {num_inicio} es mayor al final {num_final}')
else:
    for j in range(num_inicio, num_final + 1):
        print(str(j) + ', ', end = '')
    print('')
"""
Ejercicio 6.
    - Mostrar todas las tablas de multiplicar del 1 al 10.
    - Mostrar el título de la tabla
    - Las operaciones van del 1 al 10 también.
"""

for i in range(1, 11):
    print(f'Tabla del {i}')
    for j in range(1, 11):
        print(f'{i} X {j} = {i * j}')
    print('\n')
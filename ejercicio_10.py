"""
Ejercicio 10.
    - Pedir al usuario las notas 5 alumnos
    - Mostrar en pantalla el número de aprobados y suspendidos
    - Mostrar en pantalla la nota más alta
    - Mostrar en pantalla la nota más baja
    - Mostrar en pantalla la nota promedio
El rango de  notas es de 0.0 a 5.0
Se aprueba con 3.0
"""
#Variables necesarias
cant_notas = 5
cont_aprobado = 0
cont_suspendido = 0
nota_max = 0.0
nota_min = 5.0
nota_prom = 0

for i in range(cant_notas):
    nota = float(input('Ingrese la nota: '))
    if (nota < 0) or (nota > 5):
        nota = float(input('Ingrese nota válida: '))

    if nota > 3.0:
        cont_aprobado += 1
    else:
        cont_suspendido += 1
    
    nota_max = nota if nota > nota_max else nota_max
    nota_min = nota if nota < nota_min else nota_min

    nota_prom += nota

nota_prom /= cant_notas

print('=== INFORME ===')

print(f'Cantidad de suspendidos: {cont_suspendido}')
print(f'Cantidad de aprobados: {cont_aprobado}')

print(f'Nota máxima: {nota_max}')
print(f'Nota mínima: {nota_min}')
print(f'Nota promedio: {nota_prom}')


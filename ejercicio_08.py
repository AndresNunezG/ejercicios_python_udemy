"""
Ejercicio 8.
    - Solicitar al usuario un número real 'a'
    - Solicitar al usuario un número 'b' entre 0 y 100
    - El programa debe responder a la pregunta:
        ¿Cuál es el porcentaje 'b' del número 'a'?
"""

#Solicitar número 'a'
num_a = float(input('Ingrese el número: '))

#Solicitar el porcentaje número 'b'
num_b = float(input('Ingrese el porcentaje (ej: 80 para el 80%): '))
if num_b < 0: #validar si el num_b es positivo
    print('El porcentaje ingresado no es válido')
    exit()

#Calcular y Mostrar resultado
res = num_a * (num_b / 100)
print(f'El {num_b}% de {num_a} es: {res}')

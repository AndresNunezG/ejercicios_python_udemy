"""
Ejercicio 21.
    - Escribir una aplicación que reciba una cantidad infinita de números hasta el usuario escriba 'basta'
    - El recibir el stop, devolver la suma de los números ingresados
"""

def ciclo_inf():
    resultado = 0
    while True:
        entrada = input('Ingrese número: ')
        if entrada == 'basta': #terminar el ciclo si la entrada es 'basta'
            print('Entrada: basta. Ciclo terminado')
            print(f'El acumulado total es: {resultado}')
            break #romper el ciclo
        else:
            try:
                entrada = float(entrada) #casting a flotante
                resultado += entrada #acumular entradas válidas
            except: #notificar y omitir si la entrada no es un número
                print(f'{entrada}, no es válido')

ciclo_inf()
"""
Ejercicio 9:
    - Solicitar al usuario números indefinidamente
    - Mostrar el cuadraro de los números en pantalla
    - Detener el proceso si el usuario ingresa el número '111'
"""
print('Inicio del ciclo')
while True: #empezar un ciclo infinito
    num = float(input('Ingrese número: ')) #Solicitar número
    if num == 111.0: #verificar si el número ingresado es 111
        print('Número 111 detectado') 
        break #romper el ciclo infinito
    else:
        print(f'El cuadrado del número {num} es { num ** 2}') #calcular y mostrar el cuadrado
print('Fin del ciclo')
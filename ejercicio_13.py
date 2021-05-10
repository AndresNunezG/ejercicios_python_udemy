"""
Ejercicio 13.
    - Crear un script que tenga 4 variables:
        - List, String, Int y Bool.
    - Imprimir un mensaje según el tipo de dato de la variable
    - Se deben usar funciones
"""

lst_var = ['manzana', 1990, 'c', 1.0]
bln_var = True
int_var = 100
str_var = 'Pythonic'

#Utilizando una función Lambda ƛ para obtener el tipo de dato
obtener_clase = lambda var: type(var)

#Función para traducir tipo
def traducir_tipo(var):
    if obtener_clase(var) == list:
        return 'Lista (list)'
    if obtener_clase(var) == bool:
        return 'Booleano (bool)'
    if obtener_clase(var) == int:
        return 'Entero (int)'
    if obtener_clase(var) == str:
        return 'String (str)'
    else:
        return 'Indefinido (Undefined)'

#Función con parámetro tipo *args
def imprimir_tipos(*variables):
    for i in variables:
        print(f'Variable: {i}; Tipo de dato: {traducir_tipo(i)}')

#Llamar imprimir_tipos
print('\nLos tipos de datos de las variables son:')
imprimir_tipos(lst_var, bln_var, int_var, str_var)
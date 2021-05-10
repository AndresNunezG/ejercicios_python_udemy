"""
Ejercicio 13.
    - Comprobar si una variable tipo string está vacía
    - Si lo está completarlo con un texto en minísculas
    - Mostrar este texto en mayúsculas
"""

#Definir variable vacía
str_var = ''

#Comprobar si es vacía o no y actuar respecto a esto
if str_var == '':
    print(f'La variable: {str_var}, está vacía')
    str_var_txt = 'LlenarVariableVacia'
    str_var = str_var_txt.lower() #Asignar texto en minúscula
    print(f'La variable vacía, cambia a: {str_var.upper()}') #Mostrar texto en mayúscula
else:
    print(f'La variable no está vacia, el contenido es: {str_var}') #Mostrar texto si no es vacía
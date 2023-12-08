"""
Proyecto: [Devorador de vocales]
Autor: Jamith Garcia
Profesión: Desarrollador de Software
GitHub: https://github.com/djkdevise
LinkedIn: www.linkedin.com/in/jamithgarcia

Descripción:
Este programa cuenta las letras de una palabra ingresada por el usuario, omitiendo las vocales.
Utiliza bucles 'for' para iterar a través de cada letra de la palabra, 'if' anidados para verificar
si la letra es una vocal, y la sentencia 'continue' para omitir la ejecucion de las demas validaciones
e ir a la siguiente letra de la palabra en el else imprime las consonantes.

Versión: 1.0
Fecha: 2023-12-02
"""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.


user_word = input("Ingresa una palabra: ").upper()

# Completa el cuerpo del bucle for.
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter);
    
    

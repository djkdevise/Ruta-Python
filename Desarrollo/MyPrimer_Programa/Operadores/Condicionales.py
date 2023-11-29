##Condiciones y ejecución condicional
# Se leen dos números

##Ejemplo 1:
##Comenzaremos con el caso más simple - ¿cómo identificar el mayor de los dos números?:
    
##number1 = int(input("Ingresa el primer número: "))
##number2 = int(input("Ingresa el segundo número: "))
##
### Elige el número más grande
##if number1 > number2:
##    larger_number = number1
##else:
##    larger_number = number2
##
### Imprime el resultado
##print("El número más grande es:", larger_number)


## (no es necesario que aparezca una línea con sangría después de la palabra clave)

### Se leen dos números
##number1 = int(input("Ingresa el primer número: "))
##number2 = int(input("Ingresa el segundo número: "))
##
### Elige el número más grande
##if number1 > number2: larger_number = number1
##else: larger_number = number2
##
### Imprime el resultado
##print("El número más grande es:", larger_number)

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))


##encontrar el número más grande comparando todos los pares de números posibles 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)




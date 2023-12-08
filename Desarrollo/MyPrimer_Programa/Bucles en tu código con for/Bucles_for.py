##Bucles en tu código con for

##ejemplo
##for i in range(10):
##    print("El valor de i es", i)

##for i in range(2, 8):
##    print("El valor de i es", i)

##Las sentencias break y continue: más ejemplos
##largest_number = -99999999
##counter = 0
##
##while True:
##    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
##    if number == -1:
##        break
##    counter += 1
##    if number > largest_number:
##        largest_number = number
##
##if counter != 0:
##    print("El número más grande es", largest_number)
##else:
##    print("No has ingresado ningún número.")



##Y ahora la variante con continue:
##largest_number = -99999999
##counter = 0
##
##number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
##
##while number != -1:
##    if number == -1:
##        continue
##    counter += 1
##
##    if number > largest_number:
##        largest_number = number
##    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
##
##if counter:
##    print("El número más grande es", largest_number)
##else:
##    print("No has ingresado ningún número.")


##La sentencia break - atrapado en un bucle

secret_Palabra = "Chupacabra"


while True:
    
    palabra = input("Ingresa una palabra para salir del bucle: ")
    if palabra == secret_Palabra:
        print("Has dejado el bucle con éxito.")
        break
    else:
        continue

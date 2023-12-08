secret_number = 777


print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number_user = int(input("Ingresa un numero para participar: "))

while number_user != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number_user = int(input("Intenta ingresa un numero para salir del bucle: "))
    
    
print("¡Bien hecho, muggle! Eres libre ahora.")

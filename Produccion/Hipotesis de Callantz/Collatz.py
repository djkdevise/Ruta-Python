"""
Proyecto: [  LAB   La hipótesis de Collatz]
Autor: Jamith Garcia
Profesión: Desarrollador de Software
GitHub: https://github.com/djkdevise
LinkedIn: www.linkedin.com/in/jamithgarcia

Descripción:
La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.
Por supuesto, es una tarea extremadamente compleja usar una computadora para probar la hipótesis de cualquier número natural (incluso puede requerir inteligencia artificial), pero puede usar Python para verificar algunos números individuales. Tal vez incluso encuentres el que refutaría la hipótesis.
Escribe un programa que lea un número natural y ejecute los pasos anteriores siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.

Versión: 1.0
Fecha: 2023-12-05
"""

numero_inicial = int(input("Ingresa un número natural: "))
n = numero_inicial
steps = 0
while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1

    print(n,"\n")  # Imprime el último valor (siempre será 1)
    
print(f"\nSe necesitaron {steps} pasos para alcanzar 1 desde {numero_inicial}.")




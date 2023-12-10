"""
Proyecto: [LAB   Pila contadora]
Autor: Jamith Garcia
Profesión: Desarrollador de Software
GitHub: https://github.com/djkdevise
LinkedIn: www.linkedin.com/in/jamithgarcia

Descripción:
La clase Stack puede contar todos los elementos
que son agregados (push) y quitados (pop).

Versión: 1.0
Fecha: 2023-12-09
"""


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Inicializa la clase base y el contador a cero
        super().__init__()
        self.__counter = 0

    def get_counter(self):
        # Devuelve el valor actual del contador
        return self.__counter

    def pop(self):
        # Realiza un pop en la clase base y actualiza el contador
        val = super().pop()
        self.__counter += 1
        return val


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

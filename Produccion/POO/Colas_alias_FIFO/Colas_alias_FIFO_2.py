"""
Proyecto: [ LAB   Colas alias FIFO: parte 2 ]
Autor: Jamith Garcia
Profesión: Desarrollador de Software
GitHub: https://github.com/djkdevise
LinkedIn: www.linkedin.com/in/jamithgarcia

Descripción:
implementa la clase Queue con dos operaciones básicas:

put(elemento), que coloca un elemento al final de la cola.
get(), que toma un elemento del principio de la cola y lo
devuelve como resultado (la cola no puede estar vacía para
realizarlo correctamente).

Sigue las sugerencias:

put() debe agregar elementos al principio de la lista, mientras que get()
debe eliminar los elementos del final de la lista.
Define una nueva excepción llamada QueueError (elige una excepción de la
cual se derivará) y generala cuando get() intente operar en una lista vacía.

Parte 2:
crea un método sin parámetros que devuelva True si la cola está vacía y False
de lo contrario.


Versión: 1.0
Fecha: 2023-12-09
"""

class QueueError(IndexError):  # Elegir IndexError como la clase base para la nueva excepción.
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if not self.__queue:
            raise QueueError("La cola está vacía")
        return self.__queue.pop()
    
    def is_empty(self):
        return not bool(self.__queue)

# Crear una instancia de la cola
que = Queue()

# Agregar elementos a la cola
que.put(1)
que.put("perro")
que.put(False)

# Intentar obtener elementos de la cola
try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print(f"Error de cola: {e}")

# Verificar nuevamente si la cola está vacía
print(que.is_empty())  # Salida esperada: True

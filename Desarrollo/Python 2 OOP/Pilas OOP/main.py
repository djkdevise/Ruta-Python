##Pila (FIFO )segun el enfoque orientado a objetos

class Stack:

    def __init__ (self): ##contructor de la clase. selft es un parametro (por defecto) que representa el objeto recien creado
        self.__stack_list = [] ##Dos guiones bajos (__) indican que el atributo se ha ocultado (privado) y no se puede acceder desde acuera de la clase


    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
 



##subclases
class Addingstack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object_1 = Addingstack()
stack_object_2 = Addingstack()
stack_object_3 = Addingstack()

for i in range(5):
    stack_object_1.push(i)

   
print(stack_object_1.get_sum())


for i in range(5):
    print(stack_object_1.pop())









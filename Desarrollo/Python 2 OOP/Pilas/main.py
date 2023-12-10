##Pila Procedimental Basica
##crear una lista para almacenar los elementos que llegaran a la pila o lifo
stack = []


##Funcion que agrga un elemnto a la pila
def push(val):
    stack.append(val)

##funcion que elimina un elemnto de la pila
def pop():
    val=stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(stack)

print(pop())
print(pop())
print(pop())

print(stack)


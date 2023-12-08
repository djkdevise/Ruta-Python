"""
Proyecto: [  PROYECTO   Tic-Tac-Toe]
Autor: Jamith Garcia
Profesión: Desarrollador de Software
GitHub: https://github.com/djkdevise
LinkedIn: www.linkedin.com/in/jamithgarcia

Descripción:
Simple programa que simula jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
El ejemplo del programa es el siguiente:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
Versión: 1.0
Fecha: 2023-12-07
"""

from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print(f"|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print(f"|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))
            if 1 <= move <= 9 and isinstance(board[(move-1)//3][(move-1)%3], int):
                board[(move-1)//3][(move-1)%3] = 'O'
                break
            else:
                print("Movimiento no válido. Inténtalo de nuevo.")
        except ValueError:
            print("Debes ingresar un número entero.")

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = randrange(len(free_fields))
        i, j = free_fields[move]
        board[i][j] = 'X'

if __name__ == "__main__":
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("¡Has Ganado!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("¡La Máquina ha Ganado!")
            break
        if len(make_list_of_free_fields(board)) == 0:
            display_board(board)
            print("Empate")
            break

print('ДОБРО ПОЖАЛОВАТЬ!')

def instruction():
    if input('ВВЕДИТЕ "Y", ЕСЛИ ХОТИТЕ ПРОЧИТАТЬ ИНСТРУКЦИЮ') == 'y':
        print('__________________________________________________________________________')
        print("Для осуществления хода введите координаты хода в свою очередь.")
        print("Первый игрок ходит фигурой - Х, второй игрок фигурой - О")
        print("Игроки делают ход по очереди.")
        print("Для победы необходимо заполнить 3 клетки игрового поля своей фигурой")
        print('__________________________________________________________________________')
    else:
        return False
instruction()

field = [['-'] * 3 for i in range(3)]
def tab():
    print(f' 0 1 2')
    for i in range(3):
        print(f'{i} {field[i][0]} {field [i][1]} {field [i][2]}')
def step():
    while True:
        c = input('   Введите координаты хода через пробел: ').split()

        if len(c) != 2:
            print("введите 2 координаты")
            continue

        x, y = c

        if not(x.isdigit()) or not(y.isdigit()):
            print('введите числа')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('координаты вне диапазона')
            continue

        if field[x][y] != '-':
            print('клетка занята')
            continue
        return x, y

def win_check():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл крестик')
            return True
        elif symbols == ['O', 'O', 'O']:
            print('Выиграл О')
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл крестик')
            return True
        elif symbols == ['O', 'O', 'O']:
            print('Выиграл О')
            return True


    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ['X', 'X', 'X']:
        print('Выиграл крестик')
        return True
    elif symbols == ['O', 'O', 'O']:
        print('Выиграл О')
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ['X', 'X', 'X']:
        print('Выиграл крестик')
        return True
    elif symbols == ['O', 'O', 'O']:
        print('Выиграл О')
        return True

num = 0
while True:
    num += 1
    tab()
    if num % 2 == 1:
        print('Ходит крестик')
    else: print("Ходит нолик")

    x, y = step()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if win_check():
        break

    if num == 9:
        print('Ничья')
        break


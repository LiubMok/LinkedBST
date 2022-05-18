from board import Board

board = Board()
flag = True
while flag:
    print(board)
    row = int(input('Please enter the row: '))
    column = int(input('Please enter the column: '))
    board.make_move((row, column), 'x')
    if board.get_status() == 'x':
        print('User is winner!!')
        print()
        print(board)
        flag = False
        break
    board.make_computer_move()
    if board.get_status() == '0':
        print('Computer is the winer!!!')
        print()
        print(board)
        flag = False
        break

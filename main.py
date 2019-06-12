import copy

Dir_Left = 0
Dir_Right = 1
Dir_Top = 2
Dir_Down = 3
Dir_LeftTop = 4
Dir_RightTop = 5
Dir_LeftDown = 6
Dir_RightDown = 7

board = [[' ' for x in range(3)] for x in range(3)]


def showBoard(board):
    row_edges = ' '
    for _ in range(len(board) * 4 + 1):
        row_edges += '-'
    for row in board:
        row_string = ''
        for letter in row:
            row_string += ' | '
            row_string += letter
        row_string += ' |'
        print(row_edges)
        print(row_string)
    print(row_edges)


def isBoardFull(board):
    for row in board:
        for letter in row:
            if letter == ' ':
                return False
    return True


def isWinner(board, letter):
    for row_position, row in enumerate(board):
        for col_position, _ in enumerate(row):
            if checkWinner(board, [row_position, col_position], letter):
                return True

    return False


def checkWinner(board, checkPoint, letter):
    if check(board, checkPoint, letter, Dir_Left) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_Right) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_Top) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_Down) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_LeftTop) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_RightTop) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_LeftDown) >= 3:
        return True
    if check(board, checkPoint, letter, Dir_RightDown) >= 3:
        return True
    return False


def check(board, checkPoint, letter, dir):
    if (checkPoint[0] >= len(board)
        or checkPoint[1] >= len(board)
        or checkPoint[0] < 0
        or checkPoint[1] < 0
            or board[checkPoint[0]][checkPoint[1]] != letter):
        return 0

    connectPointCount = 0
    if dir == Dir_Left:
        connectPointCount = check(
            board, [checkPoint[0], checkPoint[1] - 1], letter, dir)
    elif dir == Dir_Right:
        connectPointCount = check(
            board, [checkPoint[0], checkPoint[1] + 1], letter, dir)
    elif dir == Dir_Top:
        connectPointCount = check(
            board, [checkPoint[0] - 1, checkPoint[1]], letter, dir)
    elif dir == Dir_Down:
        connectPointCount = check(
            board, [checkPoint[0] + 1, checkPoint[1]], letter, dir)
    elif dir == Dir_LeftTop:
        connectPointCount = check(
            board, [checkPoint[0] - 1, checkPoint[1] - 1], letter, dir)
    elif dir == Dir_RightTop:
        connectPointCount = check(
            board, [checkPoint[0] - 1, checkPoint[1] + 1], letter, dir)
    elif dir == Dir_LeftDown:
        connectPointCount = check(
            board, [checkPoint[0] + 1, checkPoint[1] - 1], letter, dir)
    elif dir == Dir_RightDown:
        connectPointCount = check(
            board, [checkPoint[0] + 1, checkPoint[1] + 1], letter, dir)
    return connectPointCount + 1


def playerMove(board):
    while(True):
        try:
            col_position = int(
                input('Please input 1 number of position(col nubmer)')) - 1
            row_position = int(
                input('Please input 1 number of position(col number)')) - 1
            break
        except:
            continue
    insertLetter(board, row_position, col_position, 'x')


def insertLetter(board, row_position, col_position, letter):
    board[row_position][col_position] = letter


def computerMove(board):
    _, move = calculateMove(board, 9, 'o', True)
    if len(move) != 0:
        insertLetter(board, move[0], move[1], 'o')


def calculateMove(board, depth, letter, max):
    Min_Value = 100
    Max_Value = -100
    score, move = 0, []
    score = depth
    if depth < 0:
        return score, move

    enemy_letter = ' '
    for chooseletter in ['x', 'o']:
        if chooseletter != letter:
            enemy_letter = chooseletter
            break
    possibleMoves = [[row_position, col_position] for row_position,
                     row in enumerate(board) for col_position,
                     letter in enumerate(row) if letter == ' ']

    for position in possibleMoves:
        boardCopy = copy.deepcopy(board)
        insertLetter(boardCopy, position[0], position[1], letter)
        if isWinner(boardCopy, letter):
            move = position
            Max_Value = 100
            return Max_Value, move
        else:
            value, tmp_move = calculateMove(
                boardCopy, depth - 1, enemy_letter, not max)
            # if len(tmp_move) != 0:
            if max:
                if Min_Value >= value:
                    move = position
                    Min_Value = value
                    score, move = Min_Value, move
            else:
                if Max_Value >= value:
                    move = position
                    Max_Value = value
                    score, move = Max_Value, move

    return score, move


def main():
    showBoard(board)
    while not isBoardFull(board):
        if not isWinner(board, 'x'):
            playerMove(board)
            showBoard(board)
        else:
            print('X WIN')

        if not isWinner(board, 'o'):
            computerMove(board)
            showBoard(board)
        else:
            print('O WIN')


main()

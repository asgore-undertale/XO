board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
PLAYERS = 'XO'
inv_message = 'Invalid location, Try again.\n'
win_message = 'Wins!!'
dul_message = 'Duel...'

def print_board():
    print('    a    b    c')
    for i in range(len(board)): print(i + 1, board[i])

def check(board, round):
    if not round > 2: return
    for _ in range(len(board)):
        if (board[_][0] != ' ') and board[_][1] is board[_][0] is board[_][2]: return True
        if (board[0][_] != ' ') and board[0][_] is board[1][_] is board[2][_]: return True
    if (board[1][1] != ' ') and board[0][0] is board[1][1] is board[2][2] or (board[1][1] != ' ') and board[0][2] is board[1][1] is board[2][0]:
        return True

def play(loc, player):
    if len(loc) != 2: return True

    if loc[1] in '1234567890': loc = loc[::-1]
    if loc[1] not in 'abc': return True
    loc = loc.replace('a', '1').replace('b', '2').replace('c', '3')

    if int(loc[0]) + int(loc[1]) > 6: return True
    if board[int(loc[0]) - 1][int(loc[1]) - 1] != ' ': return True

    board[int(loc[0]) - 1][int(loc[1]) - 1] = player
    print_board()
    return

def turn(player):
    loc = ''
    while True:
        loc = input(f'Player {player} turn. ')
        print('')
        if play(loc, player): print(inv_message)
        else: break

if __name__ == '__main__':
    print_board()
    for round in range(1, 5):
        for player in PLAYERS:
            turn(player)
            if check(board, round):
                print('\n', board[1][1], win_message)
                break
            if round == 5:
                print(dul_message)
                break
        if check(board, round): break
    input()
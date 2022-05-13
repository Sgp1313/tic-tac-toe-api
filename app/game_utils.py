'''
[Module] Tic-tac-toe utilities.
'''


def create_empty_board() -> list:
    '''
    Creates an empty 3x3 tictactoe board, filled with "-" as default values.
    '''

    board = []
    for i in range(3):
        board.append(['-'] * 3)

    return board


def update_board(board: list, player_id: str, row: int, column: int) -> list:
    '''
    Creates a copy of the current board and draws the player symbol in the specified position.
    '''
    new_board = board
    new_board[row][column] = player_id

    return new_board


def check_for_winner(board: list, player_id: str) -> bool:
    '''
    Evaluates if a player has won.
    '''
    winning_boards = [
                        [(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(2, 0), (1, 1), (0, 2)]
                    ]

    for win_board in winning_boards:
        if board[win_board[0][0]][win_board[0][1]] == player_id \
        and board[win_board[1][0]][win_board[1][1]] == player_id \
        and board[win_board[2][0]][win_board[2][1]] == player_id:

            return True

    return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\n GAME BOARD: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")

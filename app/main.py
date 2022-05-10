from fastapi import FastAPI
import game_utils as utils
from random import randint
from time import sleep


app = FastAPI()

# Game init
board = utils.create_empty_board()
# Players   "X"   "O"
players = [None, None] 
turn = None
winner = None
# Print initial board
utils.print_board(board)


@app.get("/registry", tags=["tic-tac-toe"])
def is_registry_open() -> bool:
    
    global turn

    if turn is None:
        print("Current players:", players)
        return True
    
    print("Current players:", players)
    return False


@app.post("/register_player/{name}", tags=["tic-tac-toe"])
def register_player(name: str) -> any:

    global players, turn
    x = players[0]
    o = players[1]
  
    if x is None and o is None:

        symbol = randint(0,1)
        players[symbol] = name

        if symbol == 0:
            print("Current players:", players)
            return "X"
        
        print("Current players:", players)
        return "O"

    if x is None:
        players[0] = name
        print("Current players:", players)

        if players[0] is not None and players[1] is not None:
            # Both players are ready to play, turn is set to "X"
            turn = "X"
            print("Current turn:", turn)

        return "X"

    if o is None: 
        players[1] = name
        print("Current players:", players)

        if players[0] is not None and players[1] is not None:
            # Both players are ready to play, turn is set to "X"          
            turn = "X"
            print("Current turn:", turn)

        return "O"

    return None


@app.get("/turn/{player_id}", tags=["tic-tac-toe"])
def get_player_turn(player_id: str) -> bool:
    
    global turn
    print("Current turn:", turn)
    
    if player_id == "X" and turn == "X":
        return True
    
    if player_id == "O" and turn == "O":
        return True

    return False


@app.get("/board", tags=["tic-tac-toe"])
def get_board():

    global board

    board_string = board[0][0] + board[0][1] + board[0][2] \
                    + board[1][0] + board[1][1] + board[1][2] \
                    + board[2][0] + board[2][1] + board[2][2]

    return board_string


@app.post("/move/{player_id}/{row}/{column}", tags=["tic-tac-toe"])
def make_move(player_id: str, row: int, column: int) -> bool:
    
    global board, turn, winner
    # Updates board with move received
    board = utils.update_board(board, player_id, row, column)
    # Prints new board
    utils.print_board(board)
    # Checks for any winner
    x_has_won = utils.check_for_winner(board, "X")
    o_has_won = utils.check_for_winner(board, "O")
    
    if x_has_won or o_has_won:

        if x_has_won:
            winner = "X"
            turn = None
            print("\n\nGAME OVER, winner: X\n\n")
        else:
            winner = "O"
            turn = None
            print("\n\nGAME OVER, winner: O\n\n")

    #Changes current turn
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"

    print("Current turn:", turn)
    return True
        

@app.get("/winner/{player_id}", tags=["tic-tac-toe"])
def get_winner(player_id: str) -> bool:

    global board

    is_winner = utils.check_for_winner(board, player_id)

    return is_winner


@app.get("/continue", tags=["tic-tac-toe"])
def does_game_continue():

    global winner 

    if winner is None:
        return True 
    
    return False

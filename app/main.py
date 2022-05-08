from fastapi import FastAPI
import game_utils as utils
from random import randint
from time import sleep


app = FastAPI()

''' Game start '''
board = utils.create_empty_board()
# players   "X"   "O"
players = [None, None] 
turn = None
winner = None


@app.get("/registry", tags=["tic-tac-toe"])
def is_registry_open() -> bool:

    if turn is None:
        return True
    
    return False


@app.post("/register_player/{name}", tags=["tic-tac-toe"])
def register_player(name: str) -> any:

    x = players[0]
    o = players[1]
  
    if x is None and o is None:

        symbol = randint(0,1)
        players[symbol] = name

        if symbol == 0:
            return "X"
        
        return "O"

    if x is None:
        players[0] = name

        if x != None and o != None:
            # Both players are ready to play, turn is set to "X"
            turn = "X"

        return "X"

    if o is None: 
        players[1] = name

        if x != None and o != None:
            # Both players are ready to play, turn is set to "X"
            turn = "X"

        return "O"

    return None


@app.get("/turn/{player_id}", tags=["tic-tac-toe"])
def get_player_turn(player_id: str) -> bool:
    
    if player_id == "X" and turn == "X":
        return True
    
    if player_id == "O" and turn == "O":
        return True

    return False


@app.get("/board", tags=["tic-tac-toe"])
def get_board():

    return board


@app.post("/move/{player_id}/{row}/{column}", tags=["tic-tac-toe"])
def make_move(player_id: str, row: int, column: int):
    
    # Updates board with move received
    board = utils.update_board(board, player_id, row, column)
    # Checks for any winner
    x_has_won = utils.check_for_winner(board, "X")
    o_has_won = utils.check_for_winner(board, "O")
    
    if x_has_won or o_has_won:

        if x_has_won:
            winner = "X"
        else:
            winner = "O"

        sleep(500)

    #Change turn
    if turn == "X":
        turn = "O"
    
    if turn == "O":
        turn = "X"
        

@app.get("/winner/{player_id}", tags=["tic-tac-toe"])
def get_winner(player_id: str):

    is_winner = utils.check_for_winner(board, player_id)

    return is_winner

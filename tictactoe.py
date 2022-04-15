from os import system
import random
import time

def valid_move(move, board):
    if move.isdigit():
        move = int(move)
        if move in range(1, 10) and move not in board:
            return True
    return False

def play_move(player_type, moves, board):
    turn = len(board) + 1
    if turn % 2 == 1:
        player = "Player 1"
    else:
        player = "Player 2"
    if player_type == "human":
        while True:
            move = input(f"{player}: ")
            if valid_move(move, board):
                move = int(move)
                break
            print("Invalid move!")
    if player_type == "ai":
        move = ai_move(board)
        print(f"{player}: {move}")
        time.sleep(2)
    moves.append(move)
    board.append(move)

def display_board(x, o):
    move = 1
    for i in range(3):
        for j in range(3):
            if move in x:
                print('x', end=' ')
            elif move in o:
                print('o', end=' ')
            else:
                print(' ', end=' ')
            move += 1
        print()

def combination(x):
    combinations = []
    for i in range(len(x) - 2):
        for j in range(i, len(x) - 1):
            for k in range(j, len(x)):
                combinations.append({x[i], x[j], x[k]})
    return combinations
    
def check_win(x, o):
    win_condition = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    if len(x) < 3:
        return 0
    x_combinations = combination(x)
    for combo in x_combinations:
        if combo in win_condition:
            return 1
    if len(o) < 3:
        return 0
    o_combinations = combination(o)
    for combo in o_combinations:
        if combo in win_condition:
            return 2
    return 0

def ai_move(board):
    while True:
        move = random.choice([i for i in range(1, 10)])
        if move not in board:
            break
    return move

    
def main():
    x = []
    o = []
    board = []
    player1_type = "human"
    player2_type = "ai"
    system('cls')
    for turn in range(1, 10):
        display_board(x, o)
        print(f"\n{board}\n")
        if turn % 2 == 1:
            play_move(player1_type, x, board)
        else:
            play_move(player2_type, o, board)
        system('cls')
        status = check_win(x, o)
        if status:
            break

    display_board(x, o)
    print(f"\n{board}\n")
    if status:
        print(f"Player {status} wins!")
    else:
        print("Draw")

main()


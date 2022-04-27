import random

def level_1(board):
    #randomly picks move
    while True:
        move = random.choice([i for i in range(1, 10)])
        if move not in board:
            break
    return move


def x_moves(board):
    x = []
    for i in range(len(board)):
        if i % 2 == 0:
            x.append(board[i])
    return x

def o_moves(board):
    o = []
    for i in range(len(board)):
        if i % 2 == 1:
            o.append(board[i])
    return o

def near_wins(player_moves, board):
    win_condition = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    near_wins = []
    #finding win conditions with only 2/3 moves played by one side
    for condition in win_condition:
        count = 0
        for move in player_moves:
            if move in condition:
                count += 1
        if count == 2:
            for move in condition:
                if move not in player_moves and move not in board:
                    near_wins.append(condition)
                    break
    return near_wins

def complete_win(condition, player_moves):
    for move in condition:
        if move not in player_moves:
            return move
    
def level_2(board):
    player_moves = {}
    player_moves['x'] = x_moves(board)
    player_moves['o'] = o_moves(board)
    turns = len(board)
    if turns % 2 == 0:
        next_player = 'x'
        curr_player = 'o'
    else:
        next_player = 'o'
        curr_player = 'x'

    near_wins_next = near_wins(player_moves[next_player], board)
    near_wins_curr = near_wins(player_moves[curr_player], board)
    #takes win if available
    if len(near_wins_next):
        move = complete_win(near_wins_next[0], player_moves[next_player])
    #blocks opponent's win
    elif len(near_wins_curr):
        move = complete_win(near_wins_curr[0], player_moves[curr_player])
    #randomly picks move
    else:
        center = 5
        corners = [1, 3, 7, 9]
        edges = [2, 4, 6, 8]
        probabilities = []
        #setting probabilities
        for i in range(1, 10):
            if i == center:
                probabilities.append(.50)
            elif i in corners:
                probabilities.append(.10)
            elif i in edges:
                probabilities.append(.025)
        #gives preference to center, corners
        move_list = random.choices([i for i in range(1, 10)], weights=probabilities, k=100)
        while True:
            move = random.choice(move_list)
            if move not in board:
                break
    return move

            
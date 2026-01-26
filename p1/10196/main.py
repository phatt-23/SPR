import sys

def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

def board_is_empty(board):
    for row in board:
        for cell in row:
            if cell != '.':
                return False
    return True

def in_bound(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board)

def add_attack_cells(board, f):
    positions = []
    for i in range(1,len(board)):
        px, py = f(x, y, i)
        positions.append((px, py))
        if not in_bound(board, px, py) or board[py][px] != '.':
            break
    return positions

def is_attacking_king(board, cell, y, x) -> bool:
    '''
    Is this cell attacking the king of the other player?
    '''

    is_white = cell.isupper()
    attack_cells = []

    if cell in 'pP':
        attack_cells += [(x - 1, y - 1), (x + 1, y - 1)] if is_white else [(x - 1, y + 1), (x + 1, y + 1)]
    if cell in 'nN':
        attack_cells += [(x - 2, y - 1), (x + 2, y - 1), (x - 2, y + 1), (x + 2, y + 1),
                            (x - 1, y - 2), (x + 1, y - 2), (x - 1, y + 2), (x + 1, y + 2)]
    if cell in 'bB' or cell in 'qQ':
        attack_cells += add_attack_cells(board, lambda x,y,i: (x+i, y+i))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x-i, y+i))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x+i, y-i))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x-i, y-i))

    if cell in 'rR' or cell in 'qQ':
        attack_cells += add_attack_cells(board, lambda x,y,i: (x+i, y))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x-i, y))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x, y+i))
        attack_cells += add_attack_cells(board, lambda x,y,i: (x, y-i))

    for ky,row in enumerate(board):
        for kx,cell in enumerate(row):
            if (cell == 'K' and not is_white) or (cell == 'k' and is_white):
                if (kx,ky) in attack_cells:
                    return True
                else:
                    return False

    return False

if __name__ == "__main__":
    stdin_lines = [line.strip() for line in sys.stdin.readlines() if line.strip() != '']
    boards = chunk_list(stdin_lines, 8)

    for i, board in enumerate(boards):
        if board_is_empty(board):
            break
        
        outcome = "no king is in check."
        found_outcome = False

        for y,row in enumerate(board):
            for x,cell in enumerate(row):
                if is_attacking_king(board, cell, y, x):
                    if cell.isupper():
                        outcome = "black king is in check."
                    else:
                        outcome = "white king is in check."
                    found_outcome = True
                    break

            if found_outcome:
                break

        print(f"Game #{i + 1}:", outcome)

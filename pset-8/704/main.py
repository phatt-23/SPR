import sys

FINAL = (
    [0,3,4,3,0,5,6,5,0,1,2,1], 
    [0,7,8,7,0,9,10,9,0,1,2,1]
)

# can do one of 4 moves
# but if i do R and R' it cancels out
# 1: R R'
# 2: RR R'R'
# 3: RRR R'R'R'
# 4: RRRR R'R'R'R'
# 5: RRRRR R'R'R'R'R'
# 6: RRRRRR
# and counter-clockwise
# and for the left side as well
# that is 6 * 2 * 2 = 24 cases where we prune
# or just check that if the previous move was R then the next one cannot be R'
# and that R isn't repeated 6 times
# (R) = R'R'R'R'R'
# (RR) = R'R'R'R'
# (RRR) = (R'R'R')
# RRRR = (R'R')
# RRRRR = (R')
# make sure one movement isn't done more than 3 times, because it can be done in less if done anti-clockwise
# if we did R, then we are allowed to do L, L' or R if R was done less 3 times before
# top cap is 3 ** 16 of possible scrambles = 43_046_721
# bottom cap is 2 ** 16 = 65_536
"""
1
Left Wheel Clockwise rotation
2
Right Wheel Clockwise rotation
3
Left Wheel Counter-Clockwise rotation
4
Right Wheel Counter-Clockwise rotation
"""

def print_moves(moves):
    for m in moves:
        match m:
            case 0:
                print("L", end="")
            case 1:
                print("R", end="")
            case 2:
                print("L'", end="")
            case 3:
                print("R'", end="")
    print()


def apply_move(scramble: tuple[list[int], list[int]], move: int) -> tuple[list[int], list[int]]:
    left, right = scramble  # unpack

    # LEFT
    if move == 0:
        left = left[-2:] + left[:-2]
        right[-3:] = left[-3:]
    # RIGHT
    elif move == 1:
        right = right[-2:] + right[:-2]
        left[-3:] = right[-3:]
    # LEFT'
    elif move == 2:
        left = left[2:] + left[:2]
        right[-3:] = left[-3:]
    # RIGHT'
    elif move == 3:
        right = right[2:] + right[:2]
        left[-3:] = right[-3:]

    return (left, right)  # repack as tuple

def find_sol(scramble, moves, same_move_count = 0):
    # print_moves(moves)
    print(scramble, moves)

    if scramble == FINAL:
        return moves
    elif len(moves) == 16:
        return None

    for move in range(4):
        # prune: checks for L with L' and R with R'
        if len(moves) == 0 or moves[-1] != ((move + 2) % 4):
        
            # prune: increase count if move is repeated
            if len(moves) == 0: 
                new_same_move_count = 1
            elif move == moves[-1]:
                new_same_move_count = same_move_count + 1
            else:
                # if it's different move, then reset the counter
                new_same_move_count = 0

            if new_same_move_count >= 3:
                continue
            
            # local change
            moves.append(move)
            
            # recurse
            if find_sol(apply_move(scramble, move), moves, new_same_move_count):
                return moves
            
            # undo
            moves.pop()

    return None

def solve(puzzle_config):
    print(puzzle_config)
    scramble = (puzzle_config[:12], puzzle_config[12:])
    solution = find_sol(scramble, [])
    print( solution )

if __name__ == "__main__":
    data = [int(a) for a in sys.stdin.read().split()]
    idx = 0
    N = data[idx]
    idx += 1
    for _ in range(N):
        puzzle_config = data[idx:idx+24]
        solve(puzzle_config)
        idx += 24

import sys
from collections import deque

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

FINAL = [
    0,3,4,3,0,5,6,5,0,1,2,1, 
    0,7,8,7,0,9,10,9,0,1,2,1
]

MOVES = {
    0: [10,11,0,1,2,3,4,5,6,7,8,9,
        12,13,14,15,16,17,18,19,20,7,8,9],
    1: [0,1,2,3,4,5,6,7,8,23,12,13,
        14,15,16,17,18,19,20,21,22,23,12,13],
    2: [2,3,4,5,6,7,8,9,10,11,0,1,
        12,13,14,15,16,17,18,19,20,11,0,1,],
    3: [0,1,2,3,4,5,6,7,8,19,20,21,
        22,23,12,13,14,15,16,17,18,19,20,21],
}

def apply_move(scramble: list[int], move: int) -> list[int]:
    return [scramble[i] for i in MOVES[move]]

def find_sol(scramble, moves, same_move_count):

    if scramble == FINAL:
        return moves
    elif len(moves) == 16:
        return None
    else:
        for move in range(4):
            # prune: checks for L with L' and R with R'
            if len(moves) == 0 or moves[-1] != ((move + 2) % 4):
            
                # prune: increase count if move is repeated
                if len(moves) != 0 and move == moves[-1]:
                    new_same_move_count = same_move_count + 1
                    # prune if the move has been done 3 or more times already
                    if new_same_move_count >= 3:
                        continue
                else: 
                    # if it's a different move OR there wasn't a move yet, reset the counter
                    new_same_move_count = 0
                
                # local change
                moves.append(move)
                
                # recurse
                new_scramble = apply_move(scramble, move)
                if find_sol(new_scramble, moves, new_same_move_count):
                    return moves
                
                # undo
                moves.pop()

    return None

def solve(scramble):
    moves = []
    same_move_count = 0
    solution = find_sol(scramble, moves, same_move_count)
    
    if solution is None:
        print("NO SOLUTION WAS FOUND IN 16 STEPS")
    elif len(solution) == 0:
        print("PUZZLE ALREADY SOLVED")
    else:
        print("".join(str(i + 1) for i in solution))
    
if __name__ == "__main__":
    data = [int(a) for a in sys.stdin.read().split()]
    idx = 0
    N = data[idx]
    idx += 1
    for _ in range(N):
        scramble = data[idx:idx+24]
        solve(scramble)
        idx += 24


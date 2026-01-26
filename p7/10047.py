import sys
from pprint import pprint

# dp[len(len(maze[0]))][len(maze)][direction][color]
# dp[x                ][y        ][         ][     ]
# monocyklista na kazdem poli muze byt nasmerovan 4 smery (0,1,2,3 nebo N,E,S,W)
# na kazdem poli pro kazdy smer se priradi se barva+1 (0,1,2,3,4)
# brute force:
# projit graf pomoci BFS, postupne najit nejkratsi cesty 
# u kazde iterace: 
#   1) jet dopredu (pocet kroku + 1)
#   2) zatocit doleva (pocet kroku + 2)
#   3) zatocit doprava (pocet kroku + 2)
# pokud se narazi na cilovy uzel a barva == 0, vyhladavani se ukonci a vrati se pocet kroku ("minimum time = %d sec")
# pokud se projede celym grafem a na cilovem uzlu nikdy nebyla barva == 0, tak vratit "destination not reachable"
# lze pouzit i memo pokud pouziju rekurzivni pristup, ale neni duvod

class Node():
    x: int
    y: int
    dir: int
    color: int
    dur: int

    def __init__(self, x, y, dir, color, dur):
        self.x = x
        self.y = y
        self.dir = dir
        self.color = color
        self.dur = dur

    def __str__(self):
        return f"{self.x = }, {self.y = }, {self.dir = }, {self.color = }, {self.dur = }"

DIR = [
    (0, -1),  # N
    (1,  0),  # E
    (0,  1),  # S
    (-1, 0),  # W
]

def solve(maze, Sx, Sy, Tx, Ty):
    # pprint(maze)
    # print(f"{Sx = }, {Sy = }, {Tx = }, {Ty = }")
    cols, rows = len(maze), len(maze[0])

    # dp = int[ len(maze[0]) ][ len(maze) ][ 4 ][ 5 ]  # pocet kroku na poli (x, y), kdyz je natoceny nejakym z 4 smeru a stoji na jedne ze 5 barev
    dp = [[[[-1 for _ in range(5)] for _ in range(4)] for _ in range(cols)] for _ in range(rows)]  # zkurveny python
    
    q = [Node(Sx, Sy, 0, 0, 0)]
    dp[Sx][Sy][0][0] = 0

    while len(q) != 0:
        curr = q.pop(0)

        # print(curr)

        if curr.x == Tx and curr.y == Ty and curr.color == 0:
            return curr.dur

        # jede vpred
        new_x = curr.x + DIR[curr.dir][0]
        new_y = curr.y + DIR[curr.dir][1]
        new_dur = curr.dur + 1

        # pokud tam neni bariera a jeste nebylo navstivene
        if 0 <= new_y < cols and 0 <= new_x < rows and maze[new_y][new_x] != "#":
            new_color = (curr.color + 1) % 5
            # print(f"jedu dal z ({curr.x}, {curr.y}) na ({new_x}, {new_y}) smerem {curr.dir} s barvou {new_color}")
            if dp[new_x][new_y][curr.dir][new_color] == -1:
                dp[new_x][new_y][curr.dir][new_color] = new_dur
                q.append(Node(new_x, new_y, curr.dir, new_color, new_dur))
        
        # otoc doprava
        # pokud novy smer jeste nebyl prozkouman
        new_dir = (curr.dir + 1) % 4
        if dp[curr.x][curr.y][new_dir][curr.color] == -1:
            dp[curr.x][curr.y][new_dir][curr.color] = new_dur
            q.append(Node(curr.x, curr.y, new_dir, curr.color, new_dur))

        # otoc doleva
        new_dir = (curr.dir - 1) % 4
        if dp[curr.x][curr.y][new_dir][curr.color] == -1:
            dp[curr.x][curr.y][new_dir][curr.color] = new_dur
            q.append(Node(curr.x, curr.y, new_dir, curr.color, new_dur))

    # pprint(dp)

    return None


if __name__ == "__main__":
    data = sys.stdin.read().split()
    idx = 0
    case = 1
    while True:
        rows, cols = int(data[idx]), int(data[idx + 1])
        if rows == cols == 0:
            break
        elif idx != 0:
            print()

        idx += 2
        
        Sx, Sy, Tx, Ty = -1, -1, -1, -1 

        maze = []
        for i in range(rows):
            cols = len(data[idx + i])
            maze.append([0] * cols)
            for j in range(cols):
                maze[i][j] = data[idx + i][j]
                if maze[i][j] == "S":
                    Sx, Sy = j, i
                if maze[i][j] == "T":
                    Tx, Ty = j, i

        result = solve(maze, Sx, Sy, Tx, Ty)
        
        print(f"Case #{case}")
        if result is None:
            print("destination not reachable")
        else:
            print(f"minimum time = {result} sec")

        case += 1
        idx += rows



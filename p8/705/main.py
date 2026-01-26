import sys
from pprint import pprint

def solve(maze):
    pprint(maze)

if __name__ == "__main__":
    data = sys.stdin.readlines()
    idx = 0

    while True:
        x, y = (int(i) for i in data[idx].split())
        if x == y == 0:
            break
        idx += 1
        maze = [i.strip() for i in data[idx:idx + y]]
        solve(maze)
        idx += y


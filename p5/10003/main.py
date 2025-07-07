import sys

def sticks(n, cuts):
    pass

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    while data[idx] != 0:
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        cuts = [0] * m
        for i in range(m):
            cuts[i] = data[idx + i]
        idx += m
        result = sticks(n, cuts)
        print(f"The minimum cutting is {result}.")
    

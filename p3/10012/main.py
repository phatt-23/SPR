import sys
from math import sqrt

def read_line():
    return sys.stdin.readline()

def read_int():
    return int(read_line())

def read_words():
    return read_line().split()

def howbig_dfs(radii, idx, n, path, visited, xs, left, right, min_width, sqrt_cache):
    # space = '  '*idx

    if idx == n:
        # print(space, path, right - left)
        return right - left
    else: 
        for vert in range(n):
            if visited[vert]:
                continue

            # print(space, vert)
            # apply local change
            path[idx] = vert

            max_dist = 0.0
            for j in range(idx):
                dist = xs[j] + sqrt_cache[path[idx]][path[j]]
                max_dist = max(max_dist, dist)
            xs[idx] = max_dist
            new_left = min(left, xs[idx] - radii[path[idx]])
            new_right = max(right, xs[idx] + radii[path[idx]])
            
            if new_right - new_left >= min_width:
                continue

            visited[vert] = True

            # recurse
            new_width = howbig_dfs(radii, idx + 1, n, path, visited, xs, new_left, new_right, min_width, sqrt_cache)
            min_width = min(min_width, new_width)
            
            # backtrack
            visited[vert] = False
            xs[idx] = 0.0
            path[idx] = None

    return min_width

def howbig(radii):
    n = len(radii)

    idx = 0
    path = [None] * n
    visited = [False] * n
    xs = [0.0] * n
    left = float('+inf')
    right = float('-inf')
    min_width = float('+inf')

    sqrt_cache = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i):
            sqrt_cache[i][j] = sqrt_cache[j][i] = 2 * sqrt(radii[i] * radii[j])

    return howbig_dfs(radii, idx, n, path, visited, xs, left, right, min_width, sqrt_cache)

if __name__ == "__main__":
    n_cases = read_int() 

    for _ in range(n_cases):
        radii = [float(w) for w in read_words()[1:]]
        result = howbig(radii)
        print("%.3f" % (result, ))


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

            # apply local change
            # print(space, vert)
            path[idx] = vert

            # must expect that smaller circles can "below" bigger circles. 
            # must iterate trough all previous xs_i where 0 <= i < current 
            # and add the distance between current circle and i-th circle
            max_dist = 0.0
            for j in range(idx):
                dist = xs[j] + sqrt_cache[path[idx]][path[j]]
                max_dist = max(max_dist, dist)
            xs[idx] = max_dist
            # the same goes for left and right overhang distances
            # doesn't have to be iterated
            new_left = min(left, xs[idx] - radii[path[idx]])
            new_right = max(right, xs[idx] + radii[path[idx]])
            
            # if the new length is worse than the current min_width
            # prune the search
            if new_right - new_left >= min_width:
                continue

            # mark visited only after it sure that it can lead to a more optimal solution
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
    xs = [0.0] * n  # holds distances between circles, x axis
    left = float('+inf')
    right = float('-inf')
    min_width = float('+inf')

    # caches the distance between two circles when they are pressed together and both are touching the ground
    # derivation of the formula:
    # r1 = a, r2 = b
    # (r1 + r1) ** 2 = (r1 - r2) ** 2 + d ** 2
    # r1**2 + 2r1r2 * r2**2 = r1**2 - 2r1r2 + r2**2 + d**2
    # 4r1r2 = d**2
    # d = 2 * sqrt(r1 * r2)
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


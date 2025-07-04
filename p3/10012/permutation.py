from copy import copy

def quick_perm(arr):
    n = len(arr)
    a = copy(arr)
    p = [None] * n

    def display(x):
        print(x)
    
    for i in range(n):
        p[i] = 0

    i = 1

    display(a)

    while i < n:
        if p[i] < i:
            j = (i % 2) * p[i]
            a[i], a[j] = a[j], a[i]

            display(a)

            p[i] += 1
            i = 1
        else:
            p[i] = 0
            i += 1

def dfs_perm(idx, n, used=None, path=None):
    if used is None:
        used = [False] * n
    if path is None:
        path = []

    if idx == n:
        print(path)
        return

    for i in range(n):
        if used[i]:
            continue
        new_path = copy(path)
        new_path.append(i)
        print('  '*idx, i, end=None)
        used[i] = True
        dfs_perm(idx + 1, n, used, new_path)
        used[i] = False

if __name__ == "__main__":
    # quick_perm(list(range(12)))
    # dfs_perm(0, 12)
    pass
    
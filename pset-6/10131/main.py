import sys
from pprint import pprint

def lis(elephants):
    n = len(elephants)
    dp = [0] * (n + 1)
    dp[0] = 1
    prev = [-1] * (n + 1)

    for i in range(1, n + 1):
        longest_sub = 0
        longest_prev_idx = -1
        for j in range(i):
            if elephants[i - 1][1] > elephants[j - 1][1]:
                if longest_sub < dp[j]:
                    longest_sub = dp[j]
                    longest_prev_idx = j
        prev[i] = longest_prev_idx
        dp[i] = 1 + longest_sub

    # print(dp)
    # print(prev)

    lis_idx = 0
    for i in range(1, n + 1):
        if dp[lis_idx] < dp[i]:
            lis_idx = i
    m = dp[lis_idx]

    path = [-1] * m
    path_idx = 0
    while lis_idx >= 0:
        path[path_idx] = elephants[lis_idx - 1][0]
        path_idx += 1
        lis_idx = prev[lis_idx]

    # print(path)
    print(m)
    for p in reversed(path):
        print(p)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = len(data)
    idx = 0
    elephants = []
    while idx < n:
        elephants.append((len(elephants) + 1, data[idx], data[idx + 1])) 
        idx += 2

    # pprint(elephants)
    elephants = sorted(elephants, key=lambda el: -el[2])
    # print(elephants)
    lis(elephants)
    

import sys

def ds_rec(x, z, n, m):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    elif x[n - 1] == z[m - 1]:
        pick = ds_rec(x, z, n - 1, m - 1)
        skip = ds_rec(x, z, n - 1, m)
        return pick + skip
    else:
        return ds_rec(x, z, n - 1, m)

def distinct_subseq(x, z):
    n = len(x)
    m = len(z)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == z[j - 1]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    res = dp[n][m]

    return res

if __name__ == '__main__':
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx])
    for _ in range(n):
        x = data[idx + 1]
        z = data[idx + 2]
        idx += 2

        result = distinct_subseq(x, z)
        print(result)

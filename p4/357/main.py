import sys

def ways_rec(denoms, r, d):
    if r == 0:
        return 1
    elif r < 0:
        return 0
    else:
        w = 0
        for i in range(d + 1):
            w += ways_rec(denoms, r - denoms[i], i)
        return w

def ways_memo(denoms, r, d, memo):
    if r == 0:
        return 1
    elif r < 0:
        return 0
    elif memo[r][d] != -1:
        return memo[r][d]
    else:
        w = 0
        for i in range(d + 1):
            w += ways_memo(denoms, r - denoms[i], i, memo)
        memo[r][d] = w
        return w

denoms = [1,5,10,25,50]
m = len(denoms)
max_amount = 30_000
dp = [[-1] * m for _ in range(max_amount + 1)]

def count_ways(amount):
    if dp[amount][m - 1] != -1:
        return dp[amount][m - 1]
    else:
        # precompute everything
        for i in range(max_amount + 1):
            dp[i][0] = 1
        for i in range(m):
            dp[0][i] = 1

        for r in range(1, max_amount + 1):
            for d in range(1, m):
                if dp[r][d] != -1:
                    continue

                if r - denoms[d] < 0:
                    # if one denom option is added, 
                    # then we still can get the value at least previous number of times
                    dp[r][d] = dp[r][d - 1]
                else:
                    # plus if the amount - new denom is positive, 
                    # then we can get this remainder dp[r - denoms[d]][d] times
                    dp[r][d] = dp[r][d - 1] + dp[r - denoms[d]][d]

        return dp[amount][m - 1]

if __name__ == "__main__":
    for amount in list(map(int, sys.stdin.readlines())):
        result = count_ways(amount)

        if result == 1:
            print(f"There is only 1 way to produce {amount} cents change.")
        else:
            print(f"There are {result} ways to produce {amount} cents change.")

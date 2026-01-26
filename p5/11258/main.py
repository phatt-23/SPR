import sys

def part_memo(xs, n, memo):
    if n == 0: 
        return 0
    elif memo[n] != -1:
        return memo[n]
    else:
        max_sum = 0

        # cut the shit up
        for i in reversed(range(0, n)):
            take = int(xs[i:n])
            # skip if next number we take is too big
            if take > 0x7fffffff:
                break
            
            max_sum = max(max_sum, take + part_memo(xs, i, memo))

        memo[n] = max_sum
        return memo[n]

def part_dp(xs):
    n = len(xs)
    dp = [0] * (n + 1)
    for m in range(1, n + 1):
        max_sum = 0
        for i in reversed(range(0, m)):
            take = int(xs[i:m])
            if take > 0x7fffffff:
                break
            else:
                if i == 0:
                    max_sum = max(max_sum, take)
                else:
                    max_sum = max(max_sum, dp[i] + take)
        dp[m] = max_sum
    return dp[n]

def partition(xs):
    n = len(xs)
    memo = [-1] * (n + 1)
    result = part_memo(xs, n, memo)

    # result = part_dp(xs)
    return result

if __name__ == '__main__':
    data = sys.stdin.read().split()
    n = int(data[0])
    for i in range(1, n + 1):
        result = partition(data[i])
        print(result)

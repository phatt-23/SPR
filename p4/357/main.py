import sys
from copy import copy

def read_int():
    return int(sys.stdin.readline())

def count_ways(amount):
    dp = [[]] * (amount + 1) 
    dp[0].append(set())   # amount = 0 can be done by having [] cents => 1 way

    denoms = [50, 25, 10, 5, 1] 

    for i in range(1, amount + 1):
        for d in denoms:
            if i - d >= 0:
                prev_ways = [copy(w) for w in dp[i - d]]
                for pw in prev_ways:
                    pw.add(d)
                    if pw not in dp[i]:
                        dp[i].append(pw)

    print(dp)

    return dp[amount]

if __name__ == "__main__":
    for amount in list(map(int, sys.stdin.readlines())):
        result = count_ways(amount)

        if result == 1:
            print(f"There is only 1 way to produce {amount} cents change.")
        else:
            print(f"There are {result} ways to produce {amount} cents change.")

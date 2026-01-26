import sys

def cutting(start, end, cuts, cut_start, cut_end, memo):
    if cut_start == cut_end:
        return 0
    elif memo[cut_start][cut_end] != -1:
        return memo[cut_start][cut_end]
    else:
        stick_len = end - start
        min_cutting = -1
        for i in range(cut_start, cut_end):
            cut = cuts[i]
            left_stick = cutting(start, cut, cuts, cut_start, i, memo)
            right_stick = cutting(cut, end, cuts, i + 1, cut_end, memo)
            if min_cutting == -1:
                min_cutting = stick_len + left_stick + right_stick
            else:
                min_cutting = min(min_cutting, stick_len + left_stick + right_stick)
        memo[cut_start][cut_end] = min_cutting
        return min_cutting

memo = [[-1] * 50 for _ in range(50)]

def sticks(amount, cuts):
    n = len(cuts)
    for i in range(n):
        for j in range(n):
            memo[i][j] = -1

    result = cutting(0, amount, cuts, 0, n, memo) 
    return result

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    idx = 0
    while data[idx] != 0:
        amount = data[idx]
        cut_count = data[idx + 1]
        idx += 2
        cuts = [0] * cut_count
        for i in range(cut_count):
            cuts[i] = data[idx + i]
        idx += cut_count
        result = sticks(amount, cuts)
        print(f"The minimum cutting is {result}.")
    

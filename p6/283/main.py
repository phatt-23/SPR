import sys
from math import log2, ceil

INF = 0xffff_ffff_ffff_ffff

def assign_bits(freq, n, max_step, bits, idx, code_length, memo, best_total):
    if idx >= n:
        return 0
    elif memo[idx][code_length] != -1:
        return memo[idx][code_length]
    else:
        for step in range(1, max_step + 1):
            remaining = n - idx 

            max_assignable = 1 << step
            if idx + max_assignable < n:
                max_assignable -= 1 

            assign_now = min(max_assignable, remaining)
            
            current_code_length = code_length + step
            coded_chars = 0

            # local change
            for i in range(assign_now):
                bits[idx + i] = current_code_length
                coded_chars += freq[idx + i]

            # recurse
            sub_total = assign_bits(freq, n, max_step, bits, idx + assign_now, current_code_length, memo, best_total)
            
            best_total = min(current_code_length * coded_chars + sub_total, best_total)

            # backtrack
            for i in range(assign_now):
                bits[idx + i] = current_code_length

        memo[idx][code_length] = best_total
        return best_total

def encode(word):
    if len(word) == 0:
        return 0

    freq = {}
    for w in word:
        if w not in freq:
            freq[w] = 0
        freq[w] += 1

    freq = sorted(freq.values(), key=lambda x: -x)
    n = len(freq)
    max_step = max(1, ceil(log2(n)))
    bits = [0] * n
    idx = 0
    code_length = 0
    memo = [[-1] * n for _ in range(n)]
    best_total = INF

    result = assign_bits(freq, n, max_step, bits, idx, code_length, memo, best_total)
    return result

if __name__ == "__main__":
    data = [line.replace('\n', '') for line in sys.stdin.readlines()]
    n = len(data)
    problems = int(data[0])
    idx = 1
    while idx < n:
        m = int(data[idx])
        idx += 1

        word = ""
        for i in range(m):
            word += data[idx + i]

        result = encode(word)
        print(result)

        idx += m

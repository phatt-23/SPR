import sys
from math import log2, ceil

INF = 0xffff_ffff_ffff_ffff

FREQ = {}                   # frequency of character occurence
CHAR_CNT = 0                # unique character count
MEMO: list[list[int]] = []  # memo for [assigned][code_len] -> min_size

def assign_bits(
    assigned: int,          # start from 0 until n, how many chars have been coded
    code_len: int,          # number of bits the current code has
):
    if assigned >= CHAR_CNT:
        return 0
    if MEMO[assigned][code_len] != -1:
        return MEMO[assigned][code_len]
    else:
        # minimization problem
        min_size = INF 

        # number of chars still not coded
        remaining = CHAR_CNT - assigned

        # number of bits sufficient enough to code all chars in the text with codes of the same length
        max_bits = max(ceil(log2(remaining)), 1)

        # try to code the remaining chars with 1 until max_bits bits
        for b in range(1, max_bits + 1):
            # max amount of codes that can be produced by b bits
            max_code_cnt = 1 << b

            # how many chars can we assign with b bits considering the number of remaining chars we have left
            # if we cannot assign all remaining chars with b bits
            # then the last code must be the extension for longer codes
            now_assigning = remaining if max_code_cnt >= remaining else (max_code_cnt - 1)

            # these chars we are now assigning are going to have curr_code_len long codes
            curr_code_len = code_len + b

            # the number of chars in the whole text have we have just coded
            # with curr_code_len long codes
            now_coded_cnt = 0
            for i in range(now_assigning):
                now_coded_cnt += FREQ[assigned + i]

            # continue through the remaining chars with the curr_code_len long extensions
            sub_size = assign_bits(assigned + now_assigning, curr_code_len)
           
            min_size = min(min_size, (now_coded_cnt * curr_code_len + sub_size))

        MEMO[assigned][code_len] = min_size
        return min_size

def encode(word):
    global FREQ, CHAR_CNT, MEMO

    if len(word) == 0:
        return 0

    FREQ = {}
    for w in word:
        if w not in FREQ:
            FREQ[w] = 0
        FREQ[w] += 1

    FREQ = sorted(FREQ.values(), key=lambda x: -x)
    CHAR_CNT = len(FREQ)
    MEMO = [[-1] * CHAR_CNT for _ in range(CHAR_CNT)]

    return assign_bits(0, 0)
    

if __name__ == "__main__":
    data = [line.replace('\n', '') for line in sys.stdin.readlines()]

    problems = int(data[0])
    idx = 1

    while idx < len(data):
        m = int(data[idx])
        idx += 1

        word = ""
        for i in range(m):
            word += data[idx + i]

        result = encode(word)
        print(result)

        idx += m

